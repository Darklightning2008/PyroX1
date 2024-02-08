from pyrogram import filters 
from Barath import barath
from Barath.barath_db.auto_catch_db import toggle_db
from config import OWNER_ID

@barath.on_message(filters.command("create_toggle") & filters.user(OWNER_ID))
async def create_toggle_command(client, message):
    if len(message.command) != 2:
        await message.reply_text("Usage: /create_toggle [command_name]")
        return

    command_name = message.command[1]
    await toggle_db.insert_one({'command_name': command_name, 'enabled': 'true'})
    await message.reply_text(f"Toggle command '{command_name}' created and enabled.")

async def check_command_status(command_name):
    command = await toggle_db.find_one({'command_name': command_name})
    return command.get('enabled', False) if command else False

@barath.on_message(filters.command("enable") & filters.user(OWNER_ID))
async def toggle_command_enable(client, message):
    user_id = message.from_user.id
    command_name = message.text.split()[1].lower()

    # Get the current state of the command from the database
    command = await toggle_db.find_one({"command_name": command_name})
    if not command:
        return await message.reply_text("Command not found in the database.")

    command_state = command.get('enabled', False)
    if command_state:
        return message.reply_text(f"Command {command_name} is already enabled!")
    else:
        try:
            await toggle_db.update_one({'command_name': command_name}, {'$set': {'enabled': True}})
            message.reply_text(f"The command {command_name} is enabled Successfully!")
        except Exception as err:
            message.reply_text(err)

@barath.on_message(filters.command("disable") & filters.user(OWNER_ID))
async def toggle_command_enable(client, message):
    user_id = message.from_user.id
    command_name = message.text.split()[1].lower()

    # Get the current state of the command from the database
    command = await toggle_db.find_one({"command_name": command_name})
    if not command:
        return await message.reply_text("Command not found in the database.")

    command_state = command.get('enabled', False)
    if command_state:
        return message.reply_text(f"Command {command_name} is already disabled!")
    else:
        try:
            await toggle_db.update_one({'command_name': command_name}, {'$set': {'enabled': False}})
            message.reply_text(f"The command {command_name} is enabled Successfully!")
        except Exception as err:
            message.reply_text(err)
    