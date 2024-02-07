from Barath import barath as app
from pyrogram import filters
from Barath.barath_db.auto_catch_db import waifu_db,catch_your_waifu_db,waifu_grabber_bot_db
from pyrogram.types import Photo
import asyncio

BOTS = [6438576771,6883098627]

@app.on_message((filters.photo))
async def guess(_, message):
    
    if message.photo:
        if message.from_user.id == 6438576771:
   
      
            id = message.photo.file_unique_id

            document = await waifu_db.find_one({"id": str(id)})

            if document:
                first_name = document.get('name', '').lower()
                await asyncio.sleep(2)  
                sent_message = await message.reply_text(f"/secure {first_name}")
            else:
                print(f"Document not found for id: {id}")

        elif  message.from_user.id == 6883098627:
      
            id = message.photo.file_unique_id

            document = await catch_your_waifu_db.find_one({"id": str(id)})

            if document:
                first_name = document.get('name', '').lower()
                await asyncio.sleep(2)  
                sent_message = await message.reply_text(f"/guess {first_name}")
            else:
                print(f"Document not found for id: {id}")

        else:
            return
