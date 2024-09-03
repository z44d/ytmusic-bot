from database import get_users
from config import OWNER_ID

from tgram import TgBot, filters
from tgram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@TgBot.on_message(filters.command("stats") & filters.private & filters.user(OWNER_ID))
async def get_stats(_, m: Message) -> Message:
    return await m.reply(
        "Total number of users now is:",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(f"{len(await get_users())}", callback_data="0")]]
        ),
    )
