from Barath import barath as app
from pyrogram import filters
from Barath.plugins.waifu_caption import waifu_db
from pyrogram.types import Photo
import asyncio

BOTS = [6438576771]

@app.on_message((filters.user(BOTS) & filters.photo))
async def guess(_, message):
    
    if message.photo:
   
        if "/secure" in message.caption:
      
            id = message.photo.file_unique_id

            document = await waifu_db.find_one({"id": str(id)})

            if document:
                first_name = document.get('name', '').lower()
                await asyncio.sleep(3)  
                sent_message = await message.reply_text(f"/secure {first_name}")
            else:
                print(f"Document not found for id: {id}")
