# models/Products.py
from db import conn, cursor

class Product:
    TABLE_NAME = "products"

    def __init__(self, name, sku, price, description, quantity, supplier, id=None):
        self.id = id
        self.name = name
        self.sku = sku
        self.price = price
        self.description = description
        self.quantity = quantity
        self.supplier = supplier

    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (name, sku, description, quantity, price, supplier)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.sku, self.description, self.quantity, self.price, self.supplier))
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
                description TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price INTEGER NOT NULL,
                supplier TEXT NOT NULL,     
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
