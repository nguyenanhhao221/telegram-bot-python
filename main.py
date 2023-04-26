import os
import asyncio
import telegram

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Telegram related
BOT_TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_GROUP_CHAT_ID = os.getenv("TELEGRAM_GROUP_ID")
BOT_USERNAME = "python_vaccine_bot"

if not BOT_TELEGRAM_TOKEN:
    raise ValueError("APP_PASSWORD is not set correctly in environment variables")


async def main():
    bot = telegram.Bot(BOT_TELEGRAM_TOKEN)
    async with bot:
        print(await bot.get_me())


if __name__ == "__main__":
    asyncio.run(main())
