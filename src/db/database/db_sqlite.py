import sqlite3
from src.db.init.init_db import conn, cursor

def create_session(
                   chat_id: int, recipient: int, sender: int, recipient_message_date: str,
                   sender_message_date: str):
    cursor.execute('''
    INSERT INTO sessions (chat_id, recipient, sender, recipient_message_date, sender_message_date)
    VALUES (?, ?, ?, ?, ?)
    ''', (chat_id, recipient, sender, recipient_message_date, sender_message_date))
    conn.commit()


def get_session(
                chat_id: int):
    cursor.execute('''
        SELECT * 
        FROM sessions
        WHERE `chat_id` = ?
        ''', (chat_id,))
    session = cursor.fetchone()
    return session


def update_session(
                   chat_id: int, recipient_message_date: str, sender_message_date: str):
    cursor.execute('''
        UPDATE sessions 
        SET recipient_message_date = ?, sender_message_date = ? 
        WHERE chat_id = ?
    ''', (recipient_message_date, sender_message_date, chat_id))

    conn.commit()


def create_streak(
                  chat_id: int, streak: int, streak_date: str, last_connect: str):
    cursor.execute('''
    INSERT INTO streaks (chat_id, streak, streak_date, last_connect)
    VALUES (?, ?, ?, ?)
    ''', (chat_id, streak, streak_date, last_connect))
    conn.commit()


def get_streak(
               chat_id: int):
    cursor.execute('''
        SELECT * 
        FROM streaks
        WHERE `chat_id` = ?
        ''', (chat_id,))
    session = cursor.fetchone()

    return session


def update_streak(
                  chat_id: int, streak: int, streak_date: str, last_connect: str):
    cursor.execute('''
        UPDATE streaks 
        SET streak = ?, streak_date = ?, last_connect = ? 
        WHERE chat_id = ?
    ''', (streak, streak_date, last_connect, chat_id))

    conn.commit()
