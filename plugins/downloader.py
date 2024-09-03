import requests
import os

from config import temp, ytm, ytd, CHANNEL
from database import get_audio, add_audio

from tgram import TgBot
from tgram.types import CallbackQuery, Message

from typing import Union


@TgBot.on_callback_query()
async def on_callback_query(b: TgBot, c: CallbackQuery) -> Union[bool, Message]:
    video_id, album_id = c.data.split(":")

    album_info = ytm.get_album(album_id)
    song_info = temp.get(video_id)

    thumb = album_info["thumbnails"][-1]["url"]

    if aud := await get_audio(song_info["videoId"]):
        return await c.message.reply_audio(aud)

    msg = await c.message.reply_photo(
        thumb,
        caption=(
            "Title: {}\n"
            "Author: **{}**\n"
            "Year: **{}**\n"
            "Is Explict: **{}**\n\n"
            "**Downloading..**"
        ).format(
            song_info["title"],
            " ,".join(i["name"] for i in song_info["artists"]),
            album_info["year"],
            song_info["isExplicit"],
        ),
    )
    vid_info = ytd.extract_info(
        "https://youtube.com/watch?v=" + song_info["videoId"], download=True
    )
    path = ytd.prepare_filename(vid_info)

    audio = await b.send_audio(
        CHANNEL,
        path,
        performer=" ,".join(i["name"] for i in song_info["artists"]),
        caption="```" + song_info["videoId"] + "```",
        title=song_info["title"],
        thumbnail=requests.get(thumb).content,
        duration=song_info["duration_seconds"],
    )

    os.remove(path)

    await add_audio(song_info["videoId"], audio.link)

    return await msg.reply_audio(audio.link)
