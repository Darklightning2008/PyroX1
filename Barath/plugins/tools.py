from Barath import barath
import requests
from pyrogram import filters,types

@barath.on_message(filters.command("bard"))
async def bard(client,message):
    msg = await message.reply_text("Getting Response...")
    prompt = None
    if message.text is None:
        prompt = None
    if " " in message.text:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            prompt =  None
    else:
        prompt = None
    if prompt is None:
        return await msg.edit("Where is query my master?")
    resp = requests.post(
        f"https://lexica.qewertyy.me/models?model_id=20&prompt={prompt}"
        )
    if resp.status_code != 200:
        return await msg.edit("An error occured.")
    data = resp.json()
    try:
        text,images = data['content'], data['images']
        if len(images) == 0:
            await msg.edit(text)
        else:
            media = []
            for i in images:
                media.append(types.InputMediaPhoto(i))
            media[0] = types.InputMediaPhoto(images[0],caption=text)
            await barath.send_media_group(
                message.chat.id,
                media,
                reply_to_message_id=message.id
                )
        try:
            await message.delete()
        except:
            return
    except Exception as Ok:
        print(Ok,data)