from Barath import bot as app
from Barath import barath
from config import OWNER_ID, HANDLER
from Barath.barath_db.auto_catch_db import allow_chats_collection
from pyrogram import filters

async def get_group_name(group_id):
    group_details = await app.get_chat(group_id)
    return group_details.title

async def add_to_allowed_groups(group_id, group_name):
    await allow_chats_collection.insert_one({"group_id": group_id, "group_name": group_name})

async def remove_from_allowed(group_id):
    await allow_chats_collection.delete_one({"group_id": group_id})

async def is_group_allowed(group_id):
    group = await allow_chats_collection.find_one({"group_id": group_id})
    return bool(group)

async def fetch_allowed_groups():
    allowed_groups = []
    async for group in allow_chats_collection.find():
        allowed_groups.append(f"Group ID: {group['group_id']}, Group Name: {group['group_name']}")
    return allowed_groups

@barath.on_message(filters.command(["include"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def ban_group(_, message):
    idd = message.from_user.id
    if idd not in OWNER_ID:
        return

    if len(message.command) > 1:
        group_id = int(message.command[1])
        group_name = await get_group_name(group_id)
        group = await is_group_allowed(group_id)
        if group:
            return await message.reply_text(f"Group is already in the allowed list")
        try:
            await add_to_allowed_groups(group_id, group_name)
            await message.reply_text(f"Group {group_id} ({group_name}) is added to the allowed list for auto catch")
        except Exception as e:
            await message.reply_text(f"Error adding group: {e}")
    else:
        group_id = message.chat.id
        group_name = message.chat.title
        group = await is_group_allowed(group_id)
        if group:
            return await message.reply_text(f"Group is already in the allowed list")
        try:
            await add_to_allowed_groups(group_id, group_name)
            await message.reply_text(f"Group {group_id} ({group_name}) is added to the allowed list for auto catch")
        except Exception as e:
            await message.reply_text(f"Error adding group: {e}")
    await message.delete()

@barath.on_message(filters.command("exclude", prefixes=HANDLER) & filters.user(OWNER_ID))
async def unban_group(_, message):
    idd = message.from_user.id
    if idd not in OWNER_ID:
        return
    try:
        if len(message.command) > 1:
            group_id = int(message.command[1])
            group = await is_group_allowed(group_id)
            if group:
                await remove_from_allowed(group_id)
                await message.reply(f"Group {group_id} is removed from the allowed list")
            else:
                await message.reply("Group is not in the allowed list")
        else:
            await message.reply("Please provide the group ID.")
    except Exception as e:
        await message.reply_text(f"Error removing group: {e}")
    await message.delete()

@barath.on_message(filters.command("allow_chats", prefixes=HANDLER) & filters.user(OWNER_ID))
async def get_allowed_groups(_, message):
    idd = message.from_user.id
    if idd not in OWNER_ID:
        return
    try:
        allowed_groups = await fetch_allowed_groups()
        if allowed_groups:
            allowed_groups_list = "\n".join(allowed_groups)
            await message.reply_text(allowed_groups_list)
        else:
            await message.reply("No groups are currently allowed.")
    except Exception as e:
        await message.reply_text(f"Error getting allowed groups: {e}")
    await message.delete()
