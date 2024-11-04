from src.db.database.db_sqlite import *
from src.config.consts import *
from src.models.db.session import Session


def create_session_on_chat_id(chat_id, recipient_message_date='2007/07/29-00:00:00', sender_message_date='2007/07/29-00:00:00'):
    create_session(chat_id=chat_id, recipient=chat_id, sender=user_id, recipient_message_date=recipient_message_date, sender_message_date=sender_message_date)

def get_session_by_chat_id(chat_id) -> Session:
    session = get_session(chat_id=chat_id)
    if session:
        return Session(*session)
    return False


def update_session_by_chat_id(session: Session):
    update_session(chat_id=session.chat_id, recipient_message_date=session.recipient_message_date, sender_message_date=session.sender_message_date)
