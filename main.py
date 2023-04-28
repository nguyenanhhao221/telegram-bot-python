"""
Main entry handler for Telegram bot
"""
import logging
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

from dotenv import load_dotenv
from handlers.start_handler import start

load_dotenv()  # Load environment variables from .env file

# Telegram related
BOT_TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_GROUP_CHAT_ID = os.getenv("TELEGRAM_GROUP_ID")
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


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echoes the message sent by the user.

    If the message contains no text, or if the chat is not valid,
    no action is taken.

    Args:
        update (telegram.Update): The update object containing information
        about the message.
        context (telegram.ext.CallbackContext): The context object for the bot.

    Returns:
        None
    """

    if (
        not update.effective_chat
        or not update.message
        or not update.message.text
    ):
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text
    )


if __name__ == "__main__":
    # Start the bot
    application = ApplicationBuilder().token(BOT_TELEGRAM_TOKEN).build()

    # Add a handler when the bot receive the command "/start",
    # and a callback function to run after it got /start
    start_handler = CommandHandler("start", start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    # Add these handler into the bot
    application.add_handlers([start_handler, echo_handler])

    # This function will keep running and get update to telegram to fetch
    # the latest update to our bot
    application.run_polling()
