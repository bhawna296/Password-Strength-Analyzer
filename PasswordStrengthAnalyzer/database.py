import sqlite3
import hashlib

DATABASE = "passwords.db"

def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_password(password):
    password_hash = hash_password(password)
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO passwords (password_hash) VALUES (?)', (password_hash,))
    conn.commit()
    conn.close()

def password_exists(password):
    password_hash = hash_password(password)
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM passwords WHERE password_hash = ?', (password_hash,))
    result = cursor.fetchone()
    conn.close()
    return result is not None