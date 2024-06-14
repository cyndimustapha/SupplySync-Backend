from db import conn, cursor

class User:
    TABLE_NAME = "users"

    def __init__(self, email, password, company_name, country, city, id=None):
        self.id = id
        self.email = email
        self.password = password
        self.company_name = company_name
        self.country = country
        self.city = city

    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (email, password, company_name, country, city)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.email, self.password, self.company_name, self.country, self.city))
        conn.commit()
        self.id = cursor.lastrowid

        return self

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                company_name TEXT,
                country TEXT,
                city TEXT
            )
        """
        cursor.execute(sql)
        conn.commit()

User.create_table()
