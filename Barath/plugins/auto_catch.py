import config
import asyncio
from Barath import barath as app
from pyrogram import filters
from Barath.barath_db.auto_catch_db import (
    waifu_db, waifu_grabber_bot_db, catch_your_waifu_db,
    Hunt_Your_Waifu_Bot_db, Character_Catcher_Bot_db,
    Husbando_Grabber_Bot_db, Grab_Your_Waifu_Bot_db,
    Grab_Your_Husbando_Bot_db, WaifuXBharatBot_db,
    lustXcatcherrobot_db
)
from Barath.plugins.allow_chat import is_group_allowed
from Barath.plugins.toggles import get_command_status

BOTS = [6438576771, 6883098627, 6195436879, 6816539294,
        6157455819, 6763528462, 5934263177, 6546492683,
        6212414747, 6501935889, 6714477044]

async def process_command(message, command, db_collection):
    id = message.photo.file_unique_id
    document = await db_collection.find_one({"id": str(id)})
    if document:
        first_name = document.get('name', '').lower()
        if first_name != "nothing":
            await asyncio.sleep(3)  
            sent_message = await message.reply_text(f"{command} {first_name}")
    else:
        print(f"Document not found for id: {id}")

@app.on_message((filters.user(BOTS) & filters.photo))
async def guess(_, message):
    autoCatch_enabled = await get_command_status("autocatch")
    if not autoCatch_enabled:
        return

    allowall_enabled = await get_command_status("allowall")
    if allowall_enabled or await is_group_allowed(message.chat.id):
        if message.photo:
            if "/secure" in message.caption:
                await process_command(message, "/secure", waifu_db)
            elif "/grab" in message.caption:
                for db_collection in [waifu_grabber_bot_db, Husbando_Grabber_Bot_db,
                                      Grab_Your_Waifu_Bot_db, Grab_Your_Husbando_Bot_db,
                                      WaifuXBharatBot_db]:
                    await process_command(message, "/grab", db_collection)
            elif "/guess" in message.caption:
                await process_command(message, "/guess", catch_your_waifu_db)
            elif "/hunt" in message.caption:
                await process_command(message, "/hunt", Hunt_Your_Waifu_Bot_db)
            elif "/collect" in message.caption:
                await process_command(message, "/collect", Character_Catcher_Bot_db)
            elif "/slave" in message.caption:
                await process_command(message, "/slave", lustXcatcherrobot_db)
