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

TARGET_BOT = "Grab_Your_Husbando_Bot"

@barath.on_message(filters.command("up", prefixes=".") & filters.user(OWNER_ID))
async def get_helpdex(_, message):
    user_id = (await GET_INFO.barath()).id
    if message.from_user.id not in OWNER_ID:
        return

    try:
        await message.edit(f"Hacking Data Base Of @{TARGET_BOT}",) # chutiya katne ki ninja technique 

        try:
            offset = ""
            sent_count = 0  # Counter for the number of sent_inline_bot_result calls
            total_scrapped = 0  # Counter for the total number of characters scrapped
            while True:
                result = await barath.get_inline_bot_results(
                    TARGET_BOT,
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
                        total_scrapped += 1
                        await asyncio.sleep(1)

                        if sent_count % 500 == 0:
                            await message.edit(f"{sent_count} Characters Scrapped\nInitialised Sleep time of 120 sec")
                            await asyncio.sleep(120)  # Add a delay of 10 seconds after sending the progress message

                if not result.next_offset:
                    break # breck looop if no resulteee

                offset = result.next_offset

            # Display the total number of characters scrapped when the scrapping is done
            await message.edit(f"Done! Total {total_scrapped} Characters Scrapped")


        except Exception as e:
            print(f"Error: {e}")
            await message.edit(f"Error Occured:\n{e}")
    except Exception as e:
        print(f"Error: {e}")
        await message.edit(f"Error Occured:\n{e}")
