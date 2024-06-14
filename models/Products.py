from db import conn, cursor

class Product:
    TABLE_NAME = "products"

    def __init__(self, name, sku, price, stock, id=None):
        self.id = id
        self.name = name
        self.sku = sku
        self.price = price
        self.stock = stock

    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (name, sku, price, stock)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.sku, self.price, self.stock))
        conn.commit()
        self.id = cursor.lastrowid

        return self

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sku TEXT NOT NULL UNIQUE,
                price INTEGER NOT NULL,
                stock INTEGER NOT NULL
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
