from pyrogram import filters,enums
from pyrogram.types import Message

from Barath import barath
from requests import get

from Barath.barath_db.auto_catch_db import toggle_db

import os
from config import HANDLER,OWNER_ID
import asyncio
import requests
import yt_dlp
from youtube_search import YoutubeSearch

from Barath.barath_db.counter_db  import list_counters
import httpx

timeout = httpx.Timeout(40, pool=None)
http = httpx.AsyncClient(http2=True, timeout=timeout)
weather_apikey = "8de2d8b3a93542c9a2d8b3a935a2c909"
get_coords = "https://api.weather.com/v3/location/search"
url = "https://api.weather.com/v3/aggcommon/v3-wx-observations-current"
headers = {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12; M2012K11AG Build/SQ1D.211205.017)"
}

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

@barath.on_message(filters.command("weather",prefixes=HANDLER) & filters.user(OWNER_ID))
async def weather(_, m: Message):
    if len(m.command) == 1:
        return await m.reply_text(
            "<b>ᴜsᴀɢᴇ:</b> <code>/weather location ᴏʀ city</code> - ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴛʜᴇ ᴡᴇᴀᴛʜᴇʀ ɪɴ <i>ʟᴏᴄᴀᴛɪᴏɴ ᴏʀ ᴄɪᴛʏ</i>"
        )
    msg = await m.reply_text("Getting Weather info...")

    r = await http.get(
        get_coords,
        headers=headers,
        params=dict(
            apiKey=weather_apikey,
            format="json",
            language="en",
            query=m.text.split(maxsplit=1)[1],
        ),
    )
    loc_json = r.json()
    try:
        await m.delete()
    except:
        return

    if not loc_json.get("location"):
        await msg.edit("ʟᴏᴄᴀᴛɪᴏɴ ɴᴏᴛ ғᴏᴜɴᴅ")
    else:
        pos = f"{loc_json['location']['latitude'][0]},{loc_json['location']['longitude'][0]}"
        r = await http.get(
            url,
            headers=headers,
            params=dict(
                apiKey=weather_apikey,
                format="json",
                language="en",
                geocode=pos,
                units="m",
            ),
        )
        res_json = r.json()

        obs_dict = res_json["v3-wx-observations-current"]

        res = "<b>{location}</b>:\n\nᴛᴇᴍᴘᴇʀᴀᴛᴜʀᴇ: <code>{temperature} °C</code>\nᴛᴇᴍᴘᴇʀᴀᴛᴜʀᴇ ғᴇᴇʟs ʟɪᴋᴇ: <code>{feels_like} °C</code>\nᴀɪʀ ʜᴜᴍɪᴅɪᴛʏ: <code>{air_humidity}%</code>\nᴡɪɴᴅ sᴘᴇᴇᴅ: <code>{wind_speed} km/h</code>\n\n- <i>{overview}</i>".format(
            location=loc_json["location"]["address"][0],
            temperature=obs_dict["temperature"],
            feels_like=obs_dict["temperatureFeelsLike"],
            air_humidity=obs_dict["relativeHumidity"],
            wind_speed=obs_dict["windSpeed"],
            overview=obs_dict["wxPhraseLong"],
        )

        await msg.edit(res)