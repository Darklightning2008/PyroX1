from pyrogram import filters 
from Barath import barath
from requests import get

import os
import config

from barath_db.auto_catch_db import waifu_db,waifu_grabber_bot_db,Hunt_Your_Waifu_Bot_db,catch_your_waifu_db

@barath.on_message(filters.user(config.OWNER_ID) & filters.command("agstats",prefixes=config.HANDLER))
async def agstats(_, message):
    total_waifu_db = waifu_db.count_documents({})
    total_waifu_grabber_bot_db = waifu_grabber_bot_db.count_documents({})
    total_Hunt_Your_Waifu_Bot_db = Hunt_Your_Waifu_Bot_db.count_documents({})
    total_catch_your_waifu_db = catch_your_waifu_db.count_documents({})
    data = f"""
AutoUB Statistics:
▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱

Total Bots Scrapped: 4

@CharacterSecureBot: {total_waifu_db}
@Catch_Your_Waifu_Bot: {total_catch_your_waifu_db}
@Waifu_Grabber_Bot: {total_waifu_grabber_bot_db}
@Hunt_Your_Waifu_Bot: {total_Hunt_Your_Waifu_Bot_db}
"""
    await message.reply_text(data)
    await message.delete()