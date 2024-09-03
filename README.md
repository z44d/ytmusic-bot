# 🎵 YTMusic Telegram Downloader Bot

![License](https://img.shields.io/github/license/z44d/ytmusic-bot)

A powerful Telegram bot that allows you to search and download music from [YTMusic](https://music.youtube.com).

---

## 📖 Contents
- [About This Project](#about-this-project)
- [Requirements](#requirements)
- [Note](#note)
- [Run](#run)
- [License](#license)

## 📝 About This Project

The YTMusic Telegram Downloader Bot is a handy tool that integrates with the [YTMusic](https://music.youtube.com) service to let you search for and download your favorite tracks directly through Telegram.

## ⚙️ Requirements

To get started, you'll need to install the following dependencies:

- **[tgram](https://github.com/z44d/tgram)**: Framework to build the Telegram bot.
- **[ytmusicapi](https://github.com/sigma67/ytmusicapi)**: Used to search in [YTMusic](https://music.youtube.com) and retrieve search results.
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: Utilized to download the music files.
- **[kvsqlite](https://github.com/AYMENJD/Kvsqlite)**: An easy and simple SQLite key-value library for simple projects.
- **[uvloop](https://github.com/MagicStack/uvloop)**: Ultra-fast asyncio event loop (only for Linux).

## ⚠️ Note

- You may need to use the [youtube-oauth2](https://github.com/coletdjnz/yt-dlp-youtube-oauth2) plugin for yt-dlp to avoid the [anti-bots protector](https://github.com/yt-dlp/yt-dlp/issues/10128).

## 🚀 Run

Follow these steps to set up and run the bot:

1. **Clone the repository:**
```bash
git clone https://github.com/z44d/ytmusic-bot
```
2. **Change to the project directory:**
```bash
cd ytmusic-bot
```
3. **Install the required dependencies:**
```bash
pip install -r requirements.txt
```
4. **Edit the environment variables file (.env) to configure your settings.**
5. **Run the bot:**
```bash
python main.py
```

## 📜 License
- This project is licensed under the MIT License - see the [LICENSE](https://github.com/z44d/ytmusic-bot/blob/main/LICENSE) file for details.