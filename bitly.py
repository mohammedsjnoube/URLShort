from bitly_func import bitly
from bot import bot, START_MESSAGE

from pyrogram import filters
from pyrogram.types import Message


@bot.on_message(filters.private & filters.command("start"))
async def start_(_, msg: Message):
    await msg.reply(
        START_MESSAGE.format(msg.from_user.mention),
        disable_web_page_preview=True
    )


@bot.on_message(filters.private & filters.text)
async def reply_bitly_link(_, msg: Message):
    long_url = msg.text
    func = bitly(str(long_url))
    short_url = func.convert_url()
    if func.response is False:
        await msg.reply("`Provide Valid Link.`")
    else:
        await msg.reply(
            f"**Shortened Url:** `{short_url}`",
            disable_web_page_preview=True
        )


if __name__ == "__main__":
    bot.run()
