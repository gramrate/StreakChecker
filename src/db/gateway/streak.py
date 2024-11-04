from src.db.database.db_sqlite import *
from src.models.db.streak import Streak


def create_streak_on_chat_id(chat_id, date):
    create_streak(chat_id=chat_id, streak=0, streak_date=date, last_connect=date)


def get_streak_by_chat_id(chat_id) -> Streak:
    streak = get_streak(chat_id=chat_id)
    if streak:
        return Streak(*streak)
    return False


def update_streak_by_chat_id(streak: Streak):
    update_streak(chat_id=streak.chat_id, streak=streak.streak, streak_date=streak.streak_date,
                  last_connect=streak.last_connect)