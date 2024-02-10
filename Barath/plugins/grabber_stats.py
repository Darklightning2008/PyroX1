from pyrogram import filters 
from Barath import barath
from requests import get


import os
from config import HANDLER,OWNER_ID
import asyncio

from Barath.barath_db.auto_catch_db import waifu_db,waifu_grabber_bot_db,catch_your_waifu_db,Hunt_Your_Waifu_Bot_db,Character_Catcher_Bot_db,Husbando_Grabber_Bot_db,Grab_Your_Waifu_Bot_db,Grab_Your_Husbando_Bot_db,WaifuXBharatBot_db,allow_chats_collection,toggle_db,lustXcatcherrobot_db,Dark_waifu_Bot_db

from Barath.barath_db.counter_db  import list_counters,get_counter

async def get_all_toggle_status():
    cursor = toggle_db.find({})
    toggle_status = {}
    async for document in cursor:
        command_name = document['command_name']
        enabled = document['enabled']
        toggle_status[command_name] = enabled
    return toggle_status

async def get_counters_data():
    # Get the list of counters and their values
    counter_data = await list_counters()

    # Format the counter data for display
    if counter_data:
        counter_text = "\n".join([f"/{counter_name}: {counter_value}" for counter_name, counter_value in counter_data.items()])
        return counter_text
    else:
        return "No Data Found!"

@barath.on_message(filters.command("agstats", prefixes=HANDLER) & filters.user(OWNER_ID))
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
    total_lustXcatcherrobot_db = await lustXcatcherrobot_db.count_documents({})
    total_Dark_waifu_Bot_db = await Dark_waifu_Bot_db.count_documents({})
    total_allow_chats_collection = await allow_chats_collection.count_documents({})
    toggle_status = await get_all_toggle_status()
    total_caught = await get_counter("total_caught")
    all_counters = await get_counters_data()

    data = f"""
AutoUB Statistics:
▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱

Total Bots Scrapped: 11
Total allowed chats: {total_allow_chats_collection}

@CharacterSecureBot: {total_waifu_db}
@Catch_Your_Waifu_Bot: {total_catch_your_waifu_db}
@Waifu_Grabber_Bot: {total_waifu_grabber_bot_db}
@Hunt_Your_Waifu_Bot: {total_Hunt_Your_Waifu_Bot_db}
@Character_Catcher_Bot: {total_Character_Catcher_Bot_db}
@Husbando_Grabber_Bot: {total_Husbando_Grabber_Bot_db}
@Grab_Your_Waifu_Bot: {total_Grab_Your_Waifu_Bot_db}
@Grab_Your_Husbando_Bot: {total_Grab_Your_Husbando_Bot_db}
@WaifuXBharatBot: {total_WaifuXBharatBot_db}
@lustXcatcherrobot: {total_lustXcatcherrobot_db}
@Dark_waifu_Bot: {total_Dark_waifu_Bot_db}
━━━━━━━━━━━━━━━━━
Commands Status:
{'\n'.join(f"{cmd}: {'Enabled' if toggle_status.get(cmd, False) else 'Disabled'}" for cmd in toggle_status)}

━━━━━━━━━━━━━━━━━
Total AutoCaught:
    ➤ {total_caught}
       ➣{all_counters}
━━━━━━━━━━━━━━━━━
Owner: @LelouchTheZeroo
"""
    msg = await  message.reply_text("Getting Stats...")
    await asyncio.sleep(1)
    await msg.edit("Please Wait!")
    await asyncio.sleep(1)
    await msg.edit(data)
    try:
        await message.delete()
    except:
        return

    

# Command handler to list all counters and their values
@barath.on_message(filters.command("allbots", prefixes=HANDLER) & filters.user(OWNER_ID))
async def list_counters_command(client, message):
    # Get the list of counters and their values
    counter_data = await list_counters()

    # Format the counter data for display
    if counter_data:
        counter_text = "\n".join([f"/{counter_name}: {counter_value}" for counter_name, counter_value in counter_data.items()])
        await message.reply_text(counter_text)
    else:
        await message.reply_text("No counters found.")