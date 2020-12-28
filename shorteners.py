from url_func import bitly, t1p
from bot import bot, START_MESSAGE

from pyrogram import filters
from pyrogram.types import Message


@bot.on_message(filters.private & filters.command("start"))
async def start_(_, msg: Message):
    await msg.reply(
        START_MESSAGE.format(msg.from_user.mention),
        disable_web_page_preview=True
    )


@bot.on_message(filters.private & filters.text & filters.command("bitly"))
async def reply_bitly_link(_, msg: Message):
    long_url = msg.text
    func = bitly(str(long_url))
    short_url = func.convert_url()
    if func.response is False:
        if func.error:
            await msg.reply(f"`{func.error}`")
        else:
            await msg.reply("**ERROR**")
    else:
        await msg.reply(
            f"**Shortened URL:**\n`{short_url}`",
            disable_web_page_preview=True
        )


@bot.on_message(filters.private & filters.text & filters.command("t1p"))
async def reply_t1p_link(_, msg: Message):
    long_url = msg.text
    func = t1p(str(long_url))
    short_url = func.convert_url()
    if func.response is False:
        if func.error:
            await msg.reply(f"`{func.error}`")
        else:
            await msg.reply("**ERROR**")
    else:
        await msg.reply(
            f"**Shortened URL:**\n`{short_url}`",
            disable_web_page_preview=True
        )


if __name__ == "__main__":
    bot.run()
