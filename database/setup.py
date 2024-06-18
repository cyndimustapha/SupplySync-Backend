from .connection import DatabaseConnection

def create_tables(db_file):
    conn = DatabaseConnection(db_file)
    cursor = conn.connect()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            sku TEXT,
            description TEXT,
            quantity INTEGER,
            price REAL,
            supplier TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity INTEGER,
            timestamp TIMESTAMP,
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            companyName TEXT,
            country TEXT,
            city TEXT
        )
    ''')

    conn.close()

if __name__ == '__main__':
    create_tables('../db.sqlite')
    print("Database tables created successfully.")
