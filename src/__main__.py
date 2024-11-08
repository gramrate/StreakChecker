#!/usr/bin/python3
# -*- coding: utf-8 -*-
from telethon import TelegramClient, types
from telethon.types import Message
from telethon.events import NewMessage

import asyncio
import logging

from src.config import config
from src.config.consts import *
from src.db.init.init_db import *
from src.db.init.init_db import conn, cursor
from src.app.app import app

API_ID = config.API_ID
API_HASH = config.API_HASH
PHONE = config.PHONE_NUMBER
PASSWORD = config.CLOUD_PASSWORD

async def main():
    client = TelegramClient(session_path, API_ID, API_HASH, system_version="4.16.30-vxCUSTOM")
    await client.start(phone=PHONE, password=PASSWORD)
    logging.info('connected')
    print('connected')

    @client.on(NewMessage(chats=chat_check))
    async def normal_handler(event: NewMessage):
        message: Message = event.message

        chat_id = message.peer_id.user_id
        user=None
        if message.from_id.user_id == user_id: user = user_id
        else: user = message.peer_id.user_id

        # buisness logic
        streak_text = app(chat_id=chat_id, user=user)
        if streak_text:
            await client.send_message(chat_id, streak_text, reply_to=message.id)

    await client.run_until_disconnected()
    client.disconnect()

if __name__ == '__main__':

    asyncio.run(main())

    cursor.close()
    conn.close()
