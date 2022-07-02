## Ft. Monk ##
## ----------- @Monk_xD ----------- ##
## Music Bot Project : https://github.com/Monk-xD/MonkMusicBot -------- ##
## News Channel : @FT_Monk -------- ##

import time
import uvloop
import asyncio
import importlib

from pytgcalls import idle
from pyrogram import Client

from .service.calls import run as runs
from MonkMusic import BOT_NAME, ASSNAME, bot, assistant, aiohttpsession
from MonkMusic.service.database.functions import clean_restart_stage
from MonkMusic.service.database.queue import (get_active_chats, remove_active_chat)
from .config import API_ID, API_HASH, BOT_TOKEN, MONGO_DB_URI, SUDO_USERS, LOG_GROUP_ID


Client(
    ':monk:',
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={'root': 'MonkMusic.core'},
).start()

print(f"Bot starting....")
print(f"Assistant Activating....")

async def main():
    restart_data = await clean_restart_stage()
    if restart_data:
        print("[ SERVER ] <--- RESTARTING BOT --->")
        try:
            await bot.edit_message_text(
                restart_data["chat_id"],
                restart_data["message_id"],
                "Bot restarted successfully!",
            )
        except Exception:
            pass
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception:
        print("error came while clearing db")
        pass
    for served_chat in served_chats:
        try:
            await remove_active_chat(served_chat)                                         
        except Exception:
            print("error came while clearing db")
            pass     
    await bot.send_message(LOG_GROUP_ID, "Bot started!")
    await assistant.send_message(LOG_GROUP_ID, "Assistant Activated!")
    print("[ SERVER ] <--- CLIENT RESTARTED! --->")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

runs()
idle()

loop.close()
print("BOT & USERBOT CLIENT STOPPED!")
