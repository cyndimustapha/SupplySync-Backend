# /models/Products.py
from database.connection import DatabaseConnection

class Product:
    TABLE_NAME = "products"

    def __init__(self, name, sku, description, quantity, price, supplier, id=None):
        self.id = id
        self.name = name
        self.sku = sku
        self.description = description
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    def save(self, db_file):
        conn = DatabaseConnection(db_file)
        cursor = conn.connect()

        if self.id is None:
            sql = f"""
                INSERT INTO {self.TABLE_NAME} (name, sku, description, quantity, price, supplier)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (self.name, self.sku, self.description, self.quantity, self.price, self.supplier))
            self.id = cursor.lastrowid
        else:
            sql = f"""
                UPDATE {self.TABLE_NAME}
                SET name=?, sku=?, description=?, quantity=?, price=?, supplier=?
                WHERE id=?
            """
            cursor.execute(sql, (self.name, self.sku, self.description, self.quantity, self.price, self.supplier, self.id))

        conn.close()

    @classmethod
    def update_quantity(cls, product_id, quantity_change, db_file):
        conn = DatabaseConnection(db_file)
        cursor = conn.connect()

        sql = f"""
            UPDATE {cls.TABLE_NAME}
            SET quantity = quantity + ?
            WHERE id = ?
        """
        cursor.execute(sql, (quantity_change, product_id))

        conn.close()

    @classmethod
    def find_all(cls, db_file):
        conn = DatabaseConnection(db_file)
        cursor = conn.connect()

        cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}")
        rows = cursor.fetchall()

        conn.close()
        products = []
        for row in rows:
            product = cls(*row)  # Instantiate Product objects from database rows
            products.append(product.__dict__)
        return products

    @classmethod
    def find_low_stock(cls, threshold, db_file):
        conn = DatabaseConnection(db_file)
        cursor = conn.connect()

        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
            WHERE quantity <= ?
        """
        cursor.execute(sql, (threshold,))
        rows = cursor.fetchall()

        conn.close()
        low_stock_products = []
        for row in rows:
            product = cls(*row)  # Instantiate Product objects from database rows
            low_stock_products.append(product.__dict__)
        return low_stock_products
