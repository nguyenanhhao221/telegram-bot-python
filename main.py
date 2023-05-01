"""
Main entry handler for Telegram bot
"""
import logging
import os
from typing import Final

from dotenv import load_dotenv
from telegram.ext import (ApplicationBuilder, CommandHandler,
                          InlineQueryHandler, MessageHandler, filters)

from handlers.cap_handler import caps, inline_caps
from handlers.echo_handler import echo
from handlers.start_handler import start

load_dotenv()  # Load environment variables from .env file

# Telegram related
BOT_TELEGRAM_TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_GROUP_CHAT_ID: Final = os.getenv("TELEGRAM_GROUP_ID")
BOT_USERNAME = "python_vaccine_bot"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)


if not BOT_TELEGRAM_TOKEN:
    raise ValueError(
        """ BOT_TELEGRAM_TOKEN is not set correctly in environment variables.
            Read here if you need help to retrieve the Telegram BOT Api Token:
            https://core.telegram.org/bots/features#botfather
            """
    )


if __name__ == "__main__":
    # Start the bot
    application = ApplicationBuilder().token(BOT_TELEGRAM_TOKEN).build()

    # Add a handler when the bot receive the command "/start",
    # and a callback function to run after it got /start
    start_handler = CommandHandler("start", start)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    cap_handler = CommandHandler("caps", caps)

    inline_caps_handler = InlineQueryHandler(inline_caps)
    # Add these handler into the bot
    application.add_handlers([start_handler, echo_handler, cap_handler, inline_caps_handler])

    # This function will keep running and get update to telegram to fetch
    # the latest update to our bot
    application.run_polling()
