## Ft. Monk ##
## ----------- @Monk_xD ----------- ##
## Music Bot Project : https://github.com/Monk-xD/MonkMusicBot -------- ##
## News Channel : @FT_Monk -------- ##


print("[ INFO ] CONNECTING TO BOT & USERBOT CLIENT --->")

import time
import uvloop
import logging
import aiohttp
import asyncio
import importlib

from MonkMusic import config
from logging import getLogger
from aiohttp import ClientSession
from pyrogram import Client, idle
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from MonkMusic.config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    MONGO_DB_URI,
    SUDO_USERS,
    LOG_GROUP_ID,
    OWNER_ID,
)


def initialize():
    global dbb
    dbb = {}
    
initialize()
print("[ INFO ] CLIENT READY! NOW LOADING DATABASE --->")

__version__ = "1.0"

MONGODB_CLI = MongoClient(MONGO_DB_URI)
db = MONGODB_CLI.wbb
SUDOERS = SUDO_USERS
OWNER = OWNER_ID

async def load_sudoers():
    global SUDOERS
    print("[ INFO ] GETTING SUDO USERS DATA --->")
    sudoersdb = db.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    for user_id in SUDOERS:
        if user_id not in sudoers:
            sudoers.append(user_id)
            await sudoersdb.update_one(
                {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
            )
    SUDOERS = (SUDOERS + sudoers) if sudoers else SUDOERS
    print("[ INFO ] SUDO USERS DATA LOADED! --->")


loop = asyncio.get_event_loop()
loop.run_until_complete(load_sudoers())


START_TIME = time.time()
BOT_ID = 0
BOT_NAME = ""
BOT_USERNAME = ""
ASSID = 0
ASSNAME = ""
ASSUSERNAME = ""
ASSMENTION = ""

print("[ INFO ] <--- PREPARING BOT & USERBOT --->")

bot = Client(
    'monk',
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)
aiohttpsession = ClientSession()

assistant = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)

def all_info(bot, assistant):
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID, ASSNAME, ASSMENTION, ASSUSERNAME
    getme = app.get_me()
    getme1 = chacha.get_me()
    BOT_ID = getme.id
    ASSID = getme1.id
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name
    BOT_USERNAME = getme.username
    ASSNAME = (
        f"{getme1.first_name} {getme1.last_name}"
        if getme1.last_name
        else getme1.first_name
    )
    ASSUSERNAME = getme1.username
    ASSMENTION = getme1.mention

    
print("[ INFO ] <--- CLIENT_1 STARTED --->")
bot.start()
print("[ INFO ] <--- CLIENT_2 STARTED --->")
assistant.start()
print("[ INFO ] <--- CLIENT_1 PROFILE INFO LOADED --->")
all_info(bot, assistant)
print("[ INFO ] <--- CLIENT_2 PROFILE INFO LOADED --->")
