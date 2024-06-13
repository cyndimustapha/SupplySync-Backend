import sqlite3

def init_db():
    conn = sqlite3.connect('test.db')

    cursor = conn.cursor()

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

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS PRODUCTS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sku TEXT NOT NULL UNIQUE,
                price INTEGER NOT NULL,
                stock INTEGER NOT NULL, 
            )       
            
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS purchases(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                product_id INTEGER, 
                date TEXT,
                quantity INTEGER,
                total_price INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(products_id) REFERENCES products(id),
            )     
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                product_id INTEGER, 
                date TEXT,
                quantity INTEGER,
                total_price INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(products_id) REFERENCES products(id),
            )     
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                product_id INTEGER, 
                date TEXT,
                quantity INTEGER,
                total_price INTEGER,
                type TEXT
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(products_id) REFERENCES products(id),
            )     
    ''')

    conn.commit()
    conn.close()

init_db()