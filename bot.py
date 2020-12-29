import os
from pyrogram import Client

if bool(os.environ.get("HEROKU")):
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    GUID = os.environ.get("GUID")
    ACCESS_TOKEN = os.environ.get("BITLY_TOKEN")
else:
    from config import API_ID, API_HASH, BOT_TOKEN, GUID, ACCESS_TOKEN

START_MESSAGE = """ Heya {},
`I am a URL-Shortener bot with multiple features.`
**Use /usage to check what I can do.**

Made with ❤️ by [BlackStone](https://t.me/BlackStone_BSC).
"""

USAGE_MESSAGE = """ Heya {},
`Below is a list of all available Commands.`

__Shorten URLs via...__
**Bitly:** `/bitly <url>`
**t1p:** `/t1p <url>`
**ogy:** `/ogy <url>`
"""

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
