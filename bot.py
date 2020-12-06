import os

from pyrogram import Client

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
GUID = os.environ.get("GUID")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

START_MESSAGE = """ Hello {},

`I am Bitly Bot to shorten links.
Send a valid link to shorten.`

Made with ❤️ by [Krishna](https://t.me/Krishna_Singhal).
"""

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
