class Streak:
    def __init__(self,
                 id: int,
                 chat_id: int,
                 streak: int,
                 streak_date: str,
                 last_connect: str,
                 ):

        self.id = id
        self.chat_id = chat_id
        self.streak = streak
        self.streak_date = streak_date
        self.last_connect = last_connect
