# models/Purchases.py
from db import conn, cursor

class Purchase:
    TABLE_NAME = "purchases"

    def __init__(self, user_id, product_id, date, quantity, total_price, id=None):
        self.id = id
        self.date = date
        self.quantity = quantity
        self.total_price = total_price
        self.user_id = user_id
        self.product_id = product_id

    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (user_id, product_id, date, quantity, total_price)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.user_id, self.product_id, self.date, self.quantity, self.total_price))
        conn.commit()
        self.id = cursor.lastrowid

        return self

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                product_id INTEGER,
                date TEXT,
                quantity INTEGER,
                total_price INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(product_id) REFERENCES products(id)
            )
        """
        cursor.execute(sql)
        conn.commit()

Purchase.create_table()
