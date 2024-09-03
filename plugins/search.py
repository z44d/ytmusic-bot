from config import temp, ytm

from tgram import TgBot, filters
from tgram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


@TgBot.on_message(filters.text & filters.private & ~filters.regex("^/"))
async def ytm_search(_, m: Message) -> Message:
    results = ytm.search(m.text, filter="songs", limit=10)[:10]

    inline_keyboard = [
        [
            InlineKeyboardButton(
                " ,".join(x["name"] for x in i["artists"])
                + " - "
                + i["title"]
                + (" [E]" if i.get("isExplicit") else ""),
                callback_data=f"{i['videoId']}:{i['album']['id']}",
            )
        ]
        for i in results
    ]

    for i in results:
        temp.update({i["videoId"]: i})

    return await m.reply(
        f"Search results for: `{m.text[:50]}...`\n\n```Note [E] in the title mean it's explicited song```",
        reply_markup=InlineKeyboardMarkup(inline_keyboard),
    )
