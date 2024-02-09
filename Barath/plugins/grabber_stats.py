from pyrogram import filters 
from Barath import barath
from requests import get

import os
import config

from Barath.barath_db.auto_catch_db import waifu_db,waifu_grabber_bot_db,catch_your_waifu_db,Hunt_Your_Waifu_Bot_db,Character_Catcher_Bot_db,Husbando_Grabber_Bot_db,Grab_Your_Waifu_Bot_db,Grab_Your_Husbando_Bot_db,WaifuXBharatBot_db,allow_chats_collection,toggle_db



async def get_all_toggle_status():
    cursor = toggle_db.find({})
    toggle_status = {}
    async for document in cursor:
        command_name = document['command_name']
        enabled = document['enabled']
        toggle_status[command_name] = enabled
    return toggle_status

@barath.on_message(filters.user(config.OWNER_ID) & filters.command("agstats",prefixes=config.HANDLER))
async def agstats(_, message):
    total_waifu_db = await waifu_db.count_documents({})
    total_waifu_grabber_bot_db = await waifu_grabber_bot_db.count_documents({})
    total_Hunt_Your_Waifu_Bot_db = await Hunt_Your_Waifu_Bot_db.count_documents({})
    total_catch_your_waifu_db = await catch_your_waifu_db.count_documents({})
    total_Character_Catcher_Bot_db = await Character_Catcher_Bot_db.count_documents({})
    total_Husbando_Grabber_Bot_db = await Husbando_Grabber_Bot_db.count_documents({})
    total_Grab_Your_Waifu_Bot_db = await Grab_Your_Waifu_Bot_db.count_documents({})
    total_Grab_Your_Husbando_Bot_db = await Grab_Your_Husbando_Bot_db.count_documents({})
    total_WaifuXBharatBot_db = await WaifuXBharatBot_db.count_documents({})
    total_allow_chats_collection = await allow_chats_collection.count_documents({})
    toggle_status = await get_all_toggle_status()

    data = f"""
AutoUB Statistics:
▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱

Total Bots Scrapped: 9
Total allowed chats: {total_allow_chats_collection}

@CharacterSecureBot: {total_waifu_db}
@Catch_Your_Waifu_Bot: {total_catch_your_waifu_db}
@Waifu_Grabber_Bot: {total_waifu_grabber_bot_db}
@Hunt_Your_Waifu_Bot: {total_Hunt_Your_Waifu_Bot_db}
@Character_Catcher_Bot: {total_Character_Catcher_Bot_db}
@Husbando_Grabber_Bot: {total_Husbando_Grabber_Bot_db}
@Grab_Your_Waifu_Bot: {total_Grab_Your_Waifu_Bot_db}
@Grab_Your_Husbando_Bot: {total_Grab_Your_Husbando_Bot_db}
@_WaifuXBharatBot: {total_WaifuXBharatBot_db}

━━━━━━━━━━━━━━━━━
Toggle Status:
{'\n'.join(f"{cmd}: {'Enabled' if toggle_status.get(cmd, False) else 'Disabled'}" for cmd in toggle_status)}

━━━━━━━━━━━━━━━━━
Owner: @LelouchTheZeroo
"""
    await message.reply_text(data)
    await message.delete()