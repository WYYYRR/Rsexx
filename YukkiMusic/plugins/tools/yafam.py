from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import filters, Client
from typing import Union
from config import (START_IMG_URL, SUDO_NAME, SUDO_USER,
                    YAFA_NAME, YAFA_CHANNEL)
from YukkiMusic import app

@app.on_message(
     command(["سورس","المطور","السورس","المبرمج"])
    & filters.group
    & ~filters.edited
)
async def Ahmed(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG_URL}",
        caption=f"""**Bot channel and bot updates**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(f"• {SUDO_NAME} •", url=f"{SUDO_USER}"),
                ],[
                InlineKeyboardButton(f"• {YAFA_NAME} •", url=f"{YAFA_CHANNEL}"),
                ],[
                InlineKeyboardButton(f"• أضفني الى مجموعتك •", url=f"https://t.me/{BOT_USERNAME}?startgroup=new"),  
                ]
            ]
        ),
    )
