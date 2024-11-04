import sqlite3
from sqlite3 import Cursor, Connection
from src.config.consts import *


def new_connection(database) -> Connection:
    return sqlite3.connect(database)


def new_cursor(conn: Connection) -> Cursor:
    return conn.cursor()


def init_db(cursor: Cursor, conn: Connection):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER UNIQUE,
        recipient INT,
        sender INT,
        recipient_message_date VARCHAR(20) DEFAULT 0,   --2024/12/31-24:59:59
        sender_message_date VARCHAR(20) DEFAULT 0       --2024/12/31-24:59:59
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS streaks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER UNIQUE,
        streak INT DEFAULT 0,
        streak_date VARCHAR(20) DEFAULT 0,   --2024/12/31-24:59:59
        last_connect VARCHAR(20) DEFAULT 0   --2024/12/31-24:59:59
    )''')

    conn.commit()

conn = new_connection(database)
cursor = new_cursor(conn)
init_db(cursor, conn)