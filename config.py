import os
from dotenv import load_dotenv

from yt_dlp import YoutubeDL
from ytmusicapi import YTMusic

load_dotenv()

TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL = "@" + os.environ.get("CHANNEL", "")
OWNER_ID = int(os.environ.get("OWNER_ID", 1))

ytm = YTMusic()
ytd = YoutubeDL(
    {
        "username": "oauth2",
        "password": "",
        "format": "bestaudio",
        "outtmpl": "%(id)s.mp3",
    }
)
temp = {}


print(CHANNEL)
