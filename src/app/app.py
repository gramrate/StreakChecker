from src.db.gateway.session import *
from src.db.gateway.streak import *
from src.app.utils.text_utils import *
from src.app.utils.time_utils import *


def app(chat_id: int, user: int):
    date = get_time()
    is_streak_now = False
    is_lost_streak = False

    session = get_session_by_chat_id(chat_id)
    if not session:
        if user == chat_id:
            create_session_on_chat_id(chat_id, recipient_message_date=date)
        elif user == user_id:
            create_session_on_chat_id(chat_id, sender_message_date=date)
        session = get_session_by_chat_id(chat_id)
    if user == session.sender:
        session.sender_message_date = date
    elif user == session.recipient:
        session.recipient_message_date = date
    if check_session_time(session.recipient_message_date, session.sender_message_date):
        streak = get_streak_by_chat_id(chat_id)
        if not streak:
            create_streak_on_chat_id(chat_id, date)
            streak = get_streak_by_chat_id(chat_id)
            streak.streak = 1
            is_streak_now = True
        else:
            streak.last_connect = date
            if check_streak_time_into(streak.last_connect, streak.streak_date):
                streak.streak_date = date
                streak.streak += 1
                print('new streak')
                is_streak_now = True
            elif check_streak_time_over(streak.last_connect, streak.streak_date):
                streak.streak_date = date
                is_streak_now = True
                is_lost_streak = True
                print('lose streak')
                streak.streak = 1
            elif check_streak_time_under(streak.last_connect, streak.streak_date):
                pass

        update_streak_by_chat_id(streak)
        print(date, streak.streak_date)
    update_session_by_chat_id(session)

    text = ''
    if is_streak_now:
        text = get_text_by_streak(streak.streak, lost=is_lost_streak) # СЕРИЯ 0, я хз
    return text
