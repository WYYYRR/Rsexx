from YukkiMusic.utils.database import is_music_playing, music_off
from strings import get_command
import asyncio
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import set_loop
from YukkiMusic.utils.decorators import AdminRightsCheck
from YukkiMusic.utils.database import is_muted, mute_on
from YukkiMusic.utils.database import is_muted, mute_off
from YukkiMusic.utils.database import is_music_playing, music_on
from datetime import datetime
from config import (BANNED_USERS, MUSIC_BOT_NAME, YAFA_NAME, YAFA_CHANNEL,
                    SUDR_USER, SUDO_NAMElyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID)
from YukkiMusic.utils import bot_sys_stats
from YukkiMusic.utils.decorators.language import language
import random
import config
import re
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from pyrogram import Client, filters
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
from os import getenv

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
                InlineKeyboardButton(f"• أضفني الى مجموعتك •", 
                                     url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),  
                ]
            ]
        ),
    )
