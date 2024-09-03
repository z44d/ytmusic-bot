from config import OWNER_ID
from database import is_user, update_user, get_users

from tgram import TgBot, filters
from tgram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, User
from tgram.errors import APIException

from typing import Optional


@TgBot.on_message(filters.command("start") & filters.private)
async def on_start_msg(bot: TgBot, m: Message) -> Message:
    if not await is_user(m.from_user.id):
        await update_user(m.from_user.id)
        await send_start_notif(bot, m.from_user)

    return await m.reply(
        f"Hi {m.from_user.mention.markdown}, Just send me the song name!",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Owner", url=f"tg://user?id={OWNER_ID}")]]
        ),
    )


async def send_start_notif(bot: TgBot, user: User) -> Optional[Message]:
    try:
        await bot.send_message(
            OWNER_ID,
            ("{mention} just started the bot!\n" "Total users now: {users}").format(
                mention=user.mention.markdown, users=len(await get_users())
            ),
            message_effect_id="5046509860389126442",
        )
    except APIException:
        return
