import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

bughunter0 = Client(
    "botname",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)


@bughunter0.on_message(filters.command(["start"]))
async def start(bot, update):
    await update.reply_text("Start Message Here")


@bughunter0.on_message(filters.forwarded & filters.channel)
async def channeltag(bot, message):
   try:
       chat_id = message.chat.id
       forward_msg = await message.copy(chat_id)
       await message.delete()
   except:
       await message.reply_text("Oops , Recheck My Admin Permissions & Try Again")
    
bughunter0.run()
