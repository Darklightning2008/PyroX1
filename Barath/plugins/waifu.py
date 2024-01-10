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
    if not message.from_user.id == user_id:
        return

    try:
        await message.edit("`Hacking Data Base Of @Catch_Your_Waifu_Bot`",) # chutiya katne ki ninja technique 

        try:
            offset = ""
            while True:
                result = await barath.get_inline_bot_results(
                    "Catch_Your_Waifu_Bot",
                    "",
                    offset=offset
                )

                if result and result.results:
                    for inline_result in result.results:
                        await barath.send_inline_bot_result(
                            chat_id=-1002096164087,  # chat id to send
                            query_id=result.query_id,
                            result_id=inline_result.id,
                            disable_notification=True,
                        )

                if not result.next_offset:
                    break # breck looop if no resulteee

                offset = result.next_offset

        except Exception as e:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
