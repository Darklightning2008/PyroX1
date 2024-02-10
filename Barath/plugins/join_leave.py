from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant, FloodWait

from Barath import bot, barath
from config import OWNER_ID,HANDLER

ASS_USERNAME="LelouchTheZeroo"

@barath.on_message(filters.command("join", prefixes=HANDLER) & filters.user(OWNER_ID))
async def joinchat(client, message):
    if "@" in message.text:
        Test = message.text.split(" ")
        username = Test[1].replace("@", "")
    else:
        msg =  await message.reply_text("Format: /join @username")
        return

    try:
        user = await client.get_me()
    except:
        user.first_name = f"{ASS_USERNAME}"
    await msg.delete()

    try: 
        await barath.join_chat(f"@{username}")
        msg = await message.reply_text(f"✅ Successfully joined @{username} group!")
    except UserAlreadyParticipant:
        await message.reply_text(f"🔴 {user.first_name} is already in this group!")
    except Exception as e:
        print(f"Error joining group: {e}")
        await message.reply_text(f"❌ An error occurred while trying to join the group. Please try again later.")



@barath.on_message(filters.command("leave", prefixes=HANDLER) & filters.user(OWNER_ID))
async def rem(client, message):
    try:
        await barath.send_message(
            message.chat.id,
            "✅ ᴜsᴇʀʙᴏᴛ ʟᴇғᴛ ᴛʜᴇ ᴄʜᴀᴛ....",
        )
        await barath.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            "❌ **Assistant can't leave your group! probably waiting for floodwaits**\n\n» Manually remove me from your group</b>"
        )
        return


# @bot.on_message(command(["userbotleaveall", "leaveall"]))
# async def bye(client, message):
#     if message.from_user.id not in SUDO_USERS:
#         await message.reply_text(
#             "You need to be part of the Association to scan a user.",
#         )
#         return
#     left = 0
#     sleep_time = 0.1
#     lol = await message.reply("**Assistant leaving all groups**\n\n`Processing...`")
#     async for userObject in USER.get_dialogs():
#         dialog = json.loads(f"{userObject}")
#         try:
#             if dialog['chat']['id'] == GBAN_CHATS or dialog['chat']['id'] == LOG_CHANNEL_ID:
#                 continue
#             await USER.leave_chat(dialog['chat']['id'])
#             await asyncio.sleep(sleep_time)
#             left += 1
#         except FloodWait as e:
#             await asyncio.sleep(int(e.x))
#         except Exception:
#             pass
#     await lol.edit(f"🏃‍♂️ `Assistant leaving...`\n\n» **Left:** {left} chats.")