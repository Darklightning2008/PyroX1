import time 
import random 
import asyncio
import config
from config import HANDLER, OWNER_ID, BARATH,SOURCE
from pyrogram import filters, __version__ as pyrover, enums
from Barath import barath, get_readable_time, StartTime
from Barath import bot, MODULE

from Barath.barath_db.auto_catch_db import waifu_db,waifu_grabber_bot_db,catch_your_waifu_db,Hunt_Your_Waifu_Bot_db,Character_Catcher_Bot_db,Husbando_Grabber_Bot_db,Grab_Your_Waifu_Bot_db,Grab_Your_Husbando_Bot_db,WaifuXBharatBot_db,allow_chats_collection,toggle_db,lustXcatcherrobot_db,Dark_waifu_Bot_db,waifu_prox_bot_db
from Barath.barath_db.counter_db  import get_counter
from  Barath.plugins.grabber_stats import get_all_toggle_status,get_counters_data

async def alive():
    start_time = time.time()
    katsuki = "3.01"
    user = await barath.get_me()
    name = user.first_name
    username = user.username
    user_profile_link = f"https://t.me/{username}" if username else ""
    user_hyperlink = f"[{name}]({user_profile_link})" if user_profile_link else name
    dbhealth = "ᴡᴏʀᴋɪɴɢ"
    uptime = get_readable_time((time.time() - StartTime))
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    
    ALIVE_TEX = "ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴍᴀꜱᴛᴇʀ"
    EMOTES = ["😍", "💀", "😊", "👋", "🎉", "🔥", "🌟", "💫", "🚀", "🤖", "👻", "👾", "🧡"]

    photo_url = "https://telegra.ph/file/e90d5a6fcca486f10025b.mp4"
    
    ALIVE_TEXT = f"""{ALIVE_TEX}
▰▱▰▱▰▱▰▱▰▱▰▱▰

➤ <b>ꜱᴛᴀᴛᴜꜱ:</b> {dbhealth}
➤ <b>ᴠᴇʀꜱɪᴏɴ:</b> {katsuki}
➤ <b>ᴜᴘᴛɪᴍᴇ:</b> {uptime}
➤ <b>ᴘɪɴɢ:</b> {ping_time} ms
➤ <b>Python:</b> {pyrover}

<b>ᴜꜱᴇʀʙᴏᴛ</b> {user_hyperlink}

<b>ᴍʏ ᴊᴏʙ ɪꜱ ᴛᴏ ꜱᴇʀᴠᴇ ᴍʏ ᴍᴀꜱᴛᴇʀ  <a href='{SOURCE}'>ᴋɪʀᴀ</a></b>"""


    return ALIVE_TEXT, photo_url

@barath.on_message(filters.command("alive", prefixes=HANDLER) & filters.user(OWNER_ID))
async def chk_alive(_, message):
    msg = await message.reply_text("Checking...")
    try:
        alive_text, photo_url = await alive()
        await msg.delete()
        await message.reply_animation(
            photo_url,
            caption=alive_text
        )
    except Exception as e:
        print("Error:", e)
        await msg.edit("An error occurred while checking the status.")

    try:
        await message.delete()
    except:
        pass

@barath.on_message(filters.command("ping", prefixes=HANDLER) & filters.user(OWNER_ID))
async def ping(_, message):
    start_time = time.time()
    msg =  await message.reply_text("Ping...")
    await msg.edit("✮ᑭｴƝGing...✮")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    uptime = get_readable_time((time.time() - StartTime))
    await msg.edit(f"**I Aᴍ Aʟɪᴠᴇ Mᴀꜱᴛᴇʀ**\n⋙ 🔔 **ᑭｴƝG**: {ping_time}\n⋙ ⬆️ **ⴑⲢⲦⲒⲘⲈ**: {uptime}")
    try:
        await message.delete()
    except:
        return
    
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
<b><u>AutoUB Statistics:</u></b>
▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱

━━━━━━━━━━━
<b>Total Bots Scrapped:</b> 12
<b>Total allowed chats:</b> {total_allow_chats_collection}
━━━━━━━━━━━

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
━━━━━━━━━━━
<b>Commands Status:</b>
{'\n'.join(f"{cmd}: {'Enabled' if toggle_status.get(cmd, False) else 'Disabled'}" for cmd in toggle_status)}

━━━━━━━━━━━
<b>Total AutoCaught:</b>
{all_counters}
━━━━━━━━━━━
<b>My Master: <a href='t.me/SIAmKira'>Kira</a></b>
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

__mod_name__ = "STATUS"  
    
__help__ = """  
- alive: to check bot on/off
- ping: check response of server
"""  


string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
