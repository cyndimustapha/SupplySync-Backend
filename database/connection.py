import sqlite3
from sqlite3 import Error

class DatabaseConnection:
    def __init__(self, db_file):
        self.conn = None
        self.cursor = None
        self.db_file = db_file

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_file, check_same_thread=False)
            self.cursor = self.conn.cursor()
            return self.cursor
        except Error as e:
            print(e)

    def close(self):
        if self.conn:
            self.conn.close()
