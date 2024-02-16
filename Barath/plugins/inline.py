import config 
import requests

from Barath import barath 
from Barath import MODULE, bot, INFO as GET_INFO
from Barath.helpers.help_func import spacebin
from pyrogram import filters
from Barath.plugins.alive import alive
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultPhoto,  # Import InlineQueryResultPhoto
)

 

from itertools import zip_longest

async def Bot_inline(_, inline_query):
    data = inline_query.query
    results = []
    
    if len(data.split()) < 2 or data=="help":
        user_id = (await GET_INFO.barath()).id
        if not inline_query.from_user.id == user_id:
            return

        buttons = [
            [InlineKeyboardButton(x['module'], callback_data=f"help:{x['module']}")]
            for x in MODULE
        ]

        # Calculate the number of buttons per column
        num_buttons_per_column = (len(buttons) + 1) // 2  # Add 1 to ensure the first column has more buttons if the total number is odd

        # Split the list of buttons into two columns
        buttons_column1, buttons_column2 = zip_longest(*[iter(buttons)] * num_buttons_per_column, fillvalue=None)

        # Create InlineKeyboardMarkup with the custom layout
        inline_keyboard = InlineKeyboardMarkup(
            [
                *buttons_column1,
                *buttons_column2,
            ]
        )

        await bot.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    "🆘 HELP COMMANDS",
                    InputTextMessageContent(message_text="[`HELP COMMANDS`]"),
                    thumb_url="https://graph.org/file/b136511bda43b1d8db7d2.jpg",
                    reply_markup=inline_keyboard
                )
            ]
        )
    
    elif data=="info":
        user_id = (await GET_INFO.barath()).id
        if not inline_query.from_user.id == user_id:
            return
        
        ALIVE_TEXT, photo_url = await alive()

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("💫 𝗝𝗢𝗜𝗡 ✨", url="https://t.me/botupdatex"),
                ],
                [
                    InlineKeyboardButton("🌝 𝗗𝗘𝗩'𝗦", url="https://t.me/Sexy_Dark"),
                    InlineKeyboardButton("🌝 𝗗𝗘𝗩'𝗦", url="https://t.me/Siamkira"),
                ],
                [
                    InlineKeyboardButton("❄️ 𝗢𝗪𝗡𝗘𝗥", url="https://t.me/tobiix"),
                ],
            ]
        )





 
