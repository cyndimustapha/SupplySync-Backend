import sqlite3

# Database file path
DATABASE_NAME= 'db.sqlite'

def get_db_connection():
    """
    Function to establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(DATABASE_NAME, check_same_thread=False)
    return conn

