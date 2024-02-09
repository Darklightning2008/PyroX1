from Barath import bot as app
from Barath import barath
from config import OWNER_ID,HANDLER
from Barath.barath_db.auto_catch_db import allow_chats_collection
from pyrogram import filters

async def get_group_name(group_id):
    group_details = await app.get_chat(group_id)
    return group_details.title

async def add_to_banned_groups(group_id):
    await allow_chats_collection.insert_one({"group_id": group_id})

async def remove_from_banned(group_id):
    await allow_chats_collection.delete_one({"group_id": group_id})

async def is_group_allowed(group_id):
    group = await allow_chats_collection.find_one({"group_id": group_id})
    return bool(group)

async def fetch_banned_groups():
    banned_groups = []
    async for group in allow_chats_collection.find():
        banned_groups.append(f"Group ID: {group['group_id']}")
    return banned_groups


@barath.on_message(filters.command(["include"],prefixes=HANDLER) & filters.user(OWNER_ID))
async def ban_group(_, message):
    idd = message.from_user.id
    if idd not in OWNER_ID:
        return

    if len(message.command) > 1:
        group_id = int(message.command[1])
        group = await is_group_allowed(group_id)
        if  group:
            return await message.reply_text(f"Group is already into include  list")
        try:
            await add_to_banned_groups(group_id)
            await message.reply_text(f"Group {group_id} is set to auto catch")
        except Exception as e:
            await message.reply_text(f"Error banning group: {e}")
    else:
        await message.reply_text("Please provide the group ID. Example: `/include -1001830463327`")
    await message.delete()


@barath.on_message(filters.command("exclude",prefixes=HANDLER)& filters.user(OWNER_ID))
async def unban_group(_, message):
    idd = message.from_user.id
    if idd not in OWNER_ID:
        return
    try:
        if len(message.command) > 1:
            group_id = int(message.command[1])
            group = await is_group_allowed(group_id)
            if group:
                await remove_from_banned(group_id)
                await message.reply(f"Group {group_id} is removed from allow catch.")
            else:
                await message.reply("Group is not into allow list")
        else:
            await message.reply("Please provide the group ID.")
    except Exception as e:
        await message.reply_text(f"Error unbanning group: {e}")
    await message.delete()

@barath.on_message(filters.command("allow_chats",prefixes=HANDLER)& filters.user(OWNER_ID))
async def get_banned_groups(_, message):
    idd = message.from_user.id
    if idd not in OWNER_ID:
        return
    try:
        banned_groups = await fetch_banned_groups()
        if banned_groups:
            banned_groups_list = "\n".join(banned_groups)
            await message.reply_text(banned_groups_list)
        else:
            await message.reply("No groups are currently banned.")
    except Exception as e:
        await message.reply_text(f"Error getting banned groups: {e}")
    await message.delete()
