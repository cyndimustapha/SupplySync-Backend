# /models/Transactions.py

from database.connection import DatabaseConnection

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

    def save(self, db_file):
        conn = DatabaseConnection(db_file)
        cursor = conn.connect()

        sql = f"""
            INSERT INTO {self.TABLE_NAME} (user_id, product_id, date, quantity, total_price, type)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.user_id, self.product_id, self.date, self.quantity, self.total_price, self.type))
        self.id = cursor.lastrowid

        conn.close()

    @classmethod
    def find_all(cls, db_file):
        conn = DatabaseConnection(db_file)
        cursor = conn.connect()

        cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}")
        rows = cursor.fetchall()

        conn.close()
        transactions = []
        for row in rows:
            transaction = cls(*row)  
            transactions.append(transaction.__dict__)
        return transactions
