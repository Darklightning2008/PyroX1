from pyrogram import filters,enums
from Barath import barath
from requests import get

from Barath.barath_db.auto_catch_db import toggle_db

import os
from config import HANDLER,OWNER_ID
import asyncio
import requests
import yt_dlp
from youtube_search import YoutubeSearch

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


@barath.on_message(filters.command("song",prefixes=HANDLER) & filters.user(OWNER_ID))
def download_song(_, message):
    query = " ".join(message.command[1:])  
    print(query)
    m = message.reply_text("**🔍**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("**⚠️ No results were found. Make sure you typed the information correctly**")
        print(str(e))
        return
    m.edit("**Downloading .. Your Request song**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("**💀 Uploading ..**")
        try:
            message.delete()
        except:
            pass

        message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=f"{title}\n**Uploaded by {message.from_user.mention}**",
            duration=dur
        )
        m.delete()
    except Exception as e:
        m.edit(" - An error check logs again sor!!")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
