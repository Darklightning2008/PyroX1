from pyrogram import filters 
from Barath import bot, barath
from Barath.barath_db.auto_catch_db import toggle_db
from config import OWNER_ID, HANDLER

async def create_toggle_command(command_name):
    await toggle_db.insert_one({'command_name': command_name, 'enabled': True})

async def toggle_command_state(command_name, enabled):
    await toggle_db.update_one({'command_name': command_name}, {'$set': {'enabled': enabled}})

async def get_command_status(command_name):
    command = await toggle_db.find_one({'command_name': command_name})
    return command.get('enabled', False) if command else False

@bot.on_message(filters.command("create_toggle") & filters.user(OWNER_ID))
async def create_toggle(client, message):
    if len(message.command) != 2:
        await message.reply_text("Usage: /create_toggle [command_name]")
        return

    command_name = message.command[1]
    await create_toggle_command(command_name)
    await message.reply_text(f"Toggle command '{command_name}' created and enabled.")

@barath.on_message(filters.command("enable", prefixes=HANDLER) & filters.user(OWNER_ID))
async def enable_command(client, message):
    if len(message.command) != 2:
        await message.reply_text("Usage: /enable [command_name]")
        return

    command_name = message.text.split()[1].lower()
    if await get_command_status(command_name):
        await message.reply_text(f"Command {command_name} is already enabled!")
    else:
        await toggle_command_state(command_name, True)
        await message.reply_text(f"Command {command_name} enabled successfully!")
    await message.delete()

@barath.on_message(filters.command("disable", prefixes=HANDLER) & filters.user(OWNER_ID))
async def disable_command(client, message):
    if len(message.command) != 2:
        await message.reply_text("Usage: /disable [command_name]")
        return

    command_name = message.text.split()[1].lower()
    if not await get_command_status(command_name):
        await message.reply_text(f"Command {command_name} is already disabled!")
    else:
        await toggle_command_state(command_name, False)
        await message.reply_text(f"Command {command_name} disabled successfully!")
    
    await message.delete()
