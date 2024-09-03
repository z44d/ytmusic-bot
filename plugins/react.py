from tgram import TgBot, filters
from tgram.types import Message, ReactionTypeEmoji


@TgBot.on_message(filters.text & filters.private, group=-1)
async def react_all_msgs(b: TgBot, m: Message) -> bool:
    return await b.set_message_reaction(
        m.chat.id, m.id, [ReactionTypeEmoji("❤️")], is_big=True
    )
