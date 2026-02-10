import sqlite3
import os

APP_ROOT = os.getcwd()
DB_DIR = os.path.join(APP_ROOT, "database")
DB_PATH = os.path.join(DB_DIR, "data.db")

def connect():
    os.makedirs(DB_DIR, exist_ok=True)

    connection = sqlite3.connect(DB_PATH, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    return connection
