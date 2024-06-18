from database.connection import DatabaseConnection

class User:
    TABLE_NAME = "users"

    def __init__(self, email, password, companyName, country, city, id=None):
        self.id = id
        self.email = email
        self.password = password
        self.companyName = companyName
        self.country = country
        self.city = city

    def save(self, db_file):
        conn = DatabaseConnection(db_file)
        cursor = conn.connect()

        sql = f"""
            INSERT INTO {self.TABLE_NAME} (email, password, companyName, country, city)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.email, self.password, self.companyName, self.country, self.city))
        self.id = cursor.lastrowid

        conn.close()
        return self

    @classmethod
    def create_table(cls, db_file):
        conn = DatabaseConnection(db_file)
        cursor = conn.connect()

        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                companyName TEXT,
                country TEXT,
                city TEXT
            )
        """
        cursor.execute(sql)
        conn.close()

    @classmethod
    def find_by_email_and_password(cls, email, password, db_file):
        conn = DatabaseConnection(db_file)
        cursor = conn.connect()

        sql = f"SELECT * FROM {cls.TABLE_NAME} WHERE email = ? AND password = ?"
        cursor.execute(sql, (email, password))
        user = cursor.fetchone()

        conn.close()
        return user
