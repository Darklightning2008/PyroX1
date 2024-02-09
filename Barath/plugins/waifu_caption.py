from Barath import bot
from pyrogram import filters
from pyrogram.types import Photo
import re
from Barath.barath_db.auto_catch_db import Grab_Your_Husbando_Bot_db as waifu_db

def kela_mela(caption: str):
    if "🌸" in caption:
        next_word = re.search(r':\s*([^\d\s]+)', caption)
        next_word = next_word.group(1).split()[0] if next_word else "nothing"
    elif "💠|" in caption:
        next_word = re.search(r':\s*([^\d\s]+)', caption)
        next_word = next_word.group(1).split()[0] if next_word else "nothing"
    elif re.search(r'\n\d+:', caption):  # Check if the caption contains a line starting with a number followed by a colon
        next_word = re.search(r'\n\d+:\s*([^\n]+)', caption)
        next_word = next_word.group(1).split()[0] if next_word else "nothing"
    else:
        next_word = "nothing"

    return next_word.strip()



def process_and_insert(photo_id, message_id, caption: str):
    next_word = kela_mela(caption)
    
    waifu_db.insert_one({"id": photo_id, "name": next_word})

    modified_info = f"Modified Info: Photo ID - {photo_id}, Message ID - {message_id}, Next Word - {next_word}"
    return modified_info

@bot.on_message(filters.incoming & filters.photo)
async def modify_and_send(_, message):
    photo_id = message.photo.file_unique_id
    photoid = message.photo.file_id
    message_id = message.id
    caption = message.caption or None
    
    modified_info = process_and_insert(photo_id, message_id, caption)

    await bot.send_photo(
        chat_id=1238234357,
        photo=photoid,
        caption=modified_info,
    )
