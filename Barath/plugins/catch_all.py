from pyrogram import Client, filters

# Create your Pyrogram client
barath = Client("my_userbot")

# Define the bot IDs and the target bot to forward messages
source_bot_id = 6438576771
target_bot_id = 6355945378

# Filter to check for messages from a particular bot in all chats
@barath.on_message(filters.user(source_bot_id) & filters.photo & ~filters.forwarded)
async def forward_message(client, message):
    chat_id = message.chat.id
    # Forward the received message from source bot to the target bot
    forwarded_message = await client.forward_messages(chat_id=target_bot_id, from_chat_id=chat_id, message_ids=message.message_id)
    
    # Define a filter to wait for messages from the target bot
    def from_target_bot(_, __, update):
        return update.from_user and update.from_user.id == target_bot_id
    
    # Wait for a response from the target bot
    response = await client.listen(from_target_bot)
    
    # Extract the part of the response after the "/" character including "/"
    response_parts = response.text.split('/', 1)
    response_text = response_parts[-1].strip() if len(response_parts) > 1 else response.text.strip()
    
    # Once the response is received, send the extracted text back to the original chat
    await client.send_message(chat_id=chat_id, text=response_text)

