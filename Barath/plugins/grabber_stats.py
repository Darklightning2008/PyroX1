from pyrogram import filters,enums
from Barath import barath
from requests import get


import os
from config import HANDLER,OWNER_ID
import asyncio

from Barath.barath_db.auto_catch_db import waifu_db,waifu_grabber_bot_db,catch_your_waifu_db,Hunt_Your_Waifu_Bot_db,Character_Catcher_Bot_db,Husbando_Grabber_Bot_db,Grab_Your_Waifu_Bot_db,Grab_Your_Husbando_Bot_db,WaifuXBharatBot_db,allow_chats_collection,toggle_db,lustXcatcherrobot_db,Dark_waifu_Bot_db,waifu_prox_bot_db

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
        counter_text = "\n".join([f" ➣/{counter_name}: {counter_value}" for counter_name, counter_value in counter_data.items()])
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
    total_waifu_prox_bot_db = await waifu_prox_bot_db.count_documents({})
    total_allow_chats_collection = await allow_chats_collection.count_documents({})
    toggle_status = await get_all_toggle_status()
    total_caught = await get_counter("total_caught")
    all_counters = await get_counters_data()

# <a href='tg://user?id={user_id}'>{name}</a>


    data = f"""
<b>AutoUB Statistics:</b>
▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱

<b>Total Bots Scrapped:</b> 12
<b>Total allowed chats:</b> {total_allow_chats_collection}

<a href='t.me/CharacterSecureBot'>Character Secure</a>: {total_waifu_db}
<a href='t.me/Catch_Your_Waifu_Bot'>Catch Your Waifu</a>: {total_catch_your_waifu_db}
<a href='t.me/Waifu_Grabber_Bot'>Waifu Grabber</a>: {total_waifu_grabber_bot_db}
<a href='t.me/Hunt_Your_Waifu_Bot'>Hunt Your Waifu</a>: {total_Hunt_Your_Waifu_Bot_db}
<a href='t.me/Character_Catcher_Bot'>Character Catcher</a>: {total_Character_Catcher_Bot_db}
<a href='t.me/Husbando_Grabber_Bot'>Husbando Grabber</a>: {total_Husbando_Grabber_Bot_db}
<a href='t.me/Grab_Your_Waifu_Bot'>Grab Your Waifu</a>: {total_Grab_Your_Waifu_Bot_db}
<a href='t.me/Grab_Your_Husbando_Bot'>Grab Your Husbando</a>: {total_Grab_Your_Husbando_Bot_db}
<a href='t.me/WaifuXBharatBot'>Waifu Bharat</a>: {total_WaifuXBharatBot_db}
<a href='t.me/lustXcatcherrobot'>Lust Catcher</a>: {total_lustXcatcherrobot_db}
<a href='t.me/Dark_waifu_Bot'>Dark Waifu</a>: {total_Dark_waifu_Bot_db}
<a href='t.me/Dark_waifu_Bot'>Loot Waifu</a>: {total_waifu_prox_bot_db}
━━━━━━━━━━━━━━━━━
<b>Commands Status:</b>
{'\n'.join(f"{cmd}: {'Enabled' if toggle_status.get(cmd, False) else 'Disabled'}" for cmd in toggle_status)}

━━━━━━━━━━━━━━━━━
<b>Total AutoCaught:</b>
{all_counters}
━━━━━━━━━━━━━━━━━
<b>Owner: <a href='t.me/LelouchTheZeroo'>Zero</a></b>
"""
    msg = await  message.reply_text("Getting Stats...")
    await asyncio.sleep(1)
    await msg.edit("Please Wait!")
    await asyncio.sleep(1)
    await msg.edit(data,disable_web_page_preview=True)
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
        msg = await message.reply_text(counter_text)
    else:
        await message.reply_text("No counters found.")