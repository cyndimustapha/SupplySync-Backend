from db import conn, cursor

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

    def save(self):
        if self.id is None:
            sql = f"""
                INSERT INTO {self.TABLE_NAME} (name, sku, description, quantity, price, supplier)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (self.name, self.sku, self.description, self.quantity, self.price, self.supplier))
            conn.commit()
            self.id = cursor.lastrowid
        else:
            sql = f"""
                UPDATE {self.TABLE_NAME}
                SET name=?, sku=?, description=?, quantity=?, price=?, supplier=?
                WHERE id=?
            """
            cursor.execute(sql, (self.name, self.sku, self.description, self.quantity, self.price, self.supplier, self.id))
            conn.commit()

    @classmethod
    def update_quantity(cls, product_id, quantity_change):
        sql = f"""
            UPDATE {cls.TABLE_NAME}
            SET quantity = quantity + ?
            WHERE id = ?
        """
        cursor.execute(sql, (quantity_change, product_id))
        conn.commit()

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                sku TEXT,
                description TEXT,
                quantity INTEGER,
                price INTEGER,
                supplier TEXT
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def find_all(cls):
        cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}")
        rows = cursor.fetchall()
        return rows

Product.create_table()
