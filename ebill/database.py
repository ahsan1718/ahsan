import sqlite3

def create_database():
    connection = sqlite3.connect('ebill.db')
    cursor = connection.cursor()

    # Create a table for users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Create a table for bills
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            amount REAL,
            due_date TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_database()
