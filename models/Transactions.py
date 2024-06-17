# models/Transactions.py
from db import conn, cursor

class Transaction:
    TABLE_NAME = "transactions"

    def __init__(self, user_id, product_id, date, quantity, total_price, type, id=None):
        self.id = id
        self.date = date
        self.quantity = quantity
        self.total_price = total_price
        self.user_id = user_id
        self.product_id = product_id
        self.type = type

    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (user_id, product_id, date, quantity, total_price, type)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.user_id, self.product_id, self.date, self.quantity, self.total_price, self.type))
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
                type TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(product_id) REFERENCES products(id)
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def find_all(cls):
        cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}")
        rows = cursor.fetchall()
        return rows

Transaction.create_table()
