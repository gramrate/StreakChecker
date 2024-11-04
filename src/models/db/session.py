class Session:
    def __init__(self,
                 id: int,
                 chat_id: int,
                 recipient: int,
                 sender: int,
                 recipient_message_date: str,
                 sender_message_date: int,
                 ):

        self.id = id
        self.chat_id = chat_id
        self.recipient = recipient
        self.sender = sender
        self.recipient_message_date = recipient_message_date
        self.sender_message_date = sender_message_date
