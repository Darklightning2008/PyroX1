from Barath import barath as app
from pyrogram import filters
from Barath.barath_db.auto_catch_db import waifu_db,waifu_grabber_bot_db,catch_your_waifu_db
from pyrogram.types import Photo
import asyncio

BOTS = [6438576771, 6883098627, 6195436879]
@app.on_message((filters.user(BOTS) & filters.photo))
async def guess(_, message):
    
    if message.photo:
   
        if "/secure" in message.caption:
      
            id = message.photo.file_unique_id

            document = await waifu_db.find_one({"id": str(id)})

            if document:
                first_name = document.get('name', '').lower()
                if first_name == "nothing":
                    return
                else:
                    await asyncio.sleep(3)  
                    sent_message = await message.reply_text(f"/secure {first_name}")
            else:
                print(f"Document not found for id: {id}")

        if "/grab" in message.caption:
      
            id = message.photo.file_unique_id

            document = await waifu_grabber_bot_db.find_one({"id": str(id)})

            if document:
                first_name = document.get('name', '').lower()
                if first_name == "nothing":
                    return
                else:
                    await asyncio.sleep(3)  
                    sent_message = await message.reply_text(f"/grab {first_name}")
            else:
                print(f"Document not found for id: {id}")

        if "/guess" in message.caption:
      
            id = message.photo.file_unique_id

            document = await catch_your_waifu_db.find_one({"id": str(id)})

            if document:
                first_name = document.get('name', '').lower()
                if first_name == "nothing":
                    return
                else:
                    await asyncio.sleep(3)  
                    sent_message = await message.reply_text(f"/guess {first_name}")
            else:
                print(f"Document not found for id: {id}")