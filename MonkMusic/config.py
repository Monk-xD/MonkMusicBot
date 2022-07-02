## Ft. Monk ##
## ----------- @Monk_xD ----------- ##
## Music Bot Project : https://github.com/Monk-xD/MonkMusicBot -------- ##
## News Channel : @FT_Monk -------- ##


import os
from os import getenv
from dotenv import load_dotenv

load_dotenv() # environment

## Client vars
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
SESSION_NAME = getenv("SESSION_NAME", "session")

## Others
ASS_ID = int(getenv("ASS_ID"))
MONGO_DB_URI = getenv("MONGO_DB_URI")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "99999"))
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

## Group & Channel
SUPPORT = getenv("SUPPORT")
UPDATES = getenv("UPDATES")
