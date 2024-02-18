from pyrogram import filters
from Barath import barath as app
GROUP_ID = -1001764251348
TEXT = "ᴄʜᴀʀᴀᴄᴛᴇʀ ʜᴀꜱ ᴊᴜsᴛ ᴀᴘᴘᴇᴀʀᴇᴅ"

@app.on_message(filters.group & filters.text)
async def secure_character(client, message):
    if TEXT in message.text:
        await message.forward(chat_id="@collect_waifu_cheats_bot")

@app.on_message(filters.private)
async def forward_reply(client, message):
    if message.chat.id == GROUP_ID:
        async for msg in app.iter_history("@collect_waifu_cheats_bot", limit=10):
            if msg.text and msg.text.startswith("Character name:"):
                character = msg.text.split(":")[1].strip()
                await app.send_message(GROUP_ID, f"/secure {character}")
                break