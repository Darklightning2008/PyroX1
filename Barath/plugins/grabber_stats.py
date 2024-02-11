from pyrogram import filters,enums
from Barath import barath
from requests import get

from Barath.barath_db.auto_catch_db import toggle_db

import os
from config import HANDLER,OWNER_ID
import asyncio


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
        counter_text = "\n".join([f" ➣{counter_name}: {counter_value}" for counter_name, counter_value in counter_data.items()])
        return counter_text
    else:
        return "No Data Found!"



    

# # Command handler to list all counters and their values
# @barath.on_message(filters.command("allbots", prefixes=HANDLER) & filters.user(OWNER_ID))
# async def list_counters_command(client, message):
#     # Get the list of counters and their values
#     counter_data = await list_counters()

#     # Format the counter data for display
#     if counter_data:
#         counter_text = "\n".join([f"/{counter_name}: {counter_value}" for counter_name, counter_value in counter_data.items()])
#         msg = await message.reply_text(counter_text)
#     else:
#         await message.reply_text("No counters found.")


@barath.on_message(filters.command("allbots", prefixes=HANDLER))
async def allbots(_, message):
    user_id=message.from_user.id
    if user_id not in OWNER_ID:
        return
    msg = await message.reply_text("Getting Bots info...")
    await asyncio.sleep(1)

    # msg =  await message.reply_text("Getting all bots...")
    counter_data = await list_counters()

    # Format the counter data for display
    if counter_data:
        counter_text = "\n".join([f"{counter_name}: {counter_value}" for counter_name, counter_value in counter_data.items()])
        await msg.edit(counter_text)
    else:
        await message.edit("No counters found.")
    try:
        await message.delete()
    except:
        return
