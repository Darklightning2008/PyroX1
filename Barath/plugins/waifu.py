import config
import requests
import asyncio
from Barath import barath
from Barath import MODULE, bot, INFO as GET_INFO
from config import OWNER_ID
from pyrogram import filters
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultPhoto,
)

@barath.on_message(filters.command("up", prefixes=".") & filters.user(OWNER_ID))
async def get_helpdex(_, message):
    user_id = (await GET_INFO.barath()).id
    if message.from_user.id not in OWNER_ID:
        return

    try:
        await message.edit("`Hacking Data Base Of @Waifu_Grabber_Bot`",) # chutiya katne ki ninja technique 

        try:
            offset = ""
            sent_count = 0  # Counter for the number of sent_inline_bot_result calls
            while True:
                result = await barath.get_inline_bot_results(
                    "Waifu_Grabber_Bot",
                    "",
                    offset=offset
                )

                if result and result.results:
                    for inline_result in result.results:
                        await barath.send_inline_bot_result(
                            chat_id=-1002119409366,  # chat id to send
                            query_id=result.query_id,
                            result_id=inline_result.id,
                            disable_notification=True,
                        )
                        sent_count += 1
                        
                        # # Add a sleep of 0.5 seconds after each send_inline_bot_result
                        # await asyncio.sleep(0.5)
                        
                        # If 100 sent_inline_bot_result calls have been made, add a delay of 10 seconds
                        if sent_count % 100 == 0:
                            try:
                                await barath.send_message(chat_id=message.from_user.id, text=f"{sent_count} Characters Scrapped")
                                await message.edit(f"{sent_count} Characters Scrapped")
                            except Exception as err:
                                print(err)
                            await asyncio.sleep(10)  # Add a delay of 10 seconds after sending the progress message

                if not result.next_offset:
                    break # breck looop if no resulteee

                offset = result.next_offset

        except Exception as e:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
