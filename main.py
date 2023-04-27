"""
Main entry handler for Telegram bot
"""
import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Telegram related
BOT_TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_GROUP_CHAT_ID = os.getenv("TELEGRAM_GROUP_ID")
BOT_USERNAME = "python_vaccine_bot"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


if not BOT_TELEGRAM_TOKEN:
    raise ValueError(
        """ BOT_TELEGRAM_TOKEN is not set correctly in environment variables. 
            Read here if you need help to retrieve the Telegram BOT Api Token: 
            https://core.telegram.org/bots/features#botfather"""
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /start command. Sends a greeting message to the user.

    Args:
        update (telegram.Update): The update object representing the user's message.
        context (telegram.ext.CallbackContext): The context object for the current update.

    Returns:
        None: The function is asynchronous and does not return anything. The message is sent using `context.bot.send_message`.
    """

    if not update.effective_chat:
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hello I'm a bot created by Hao Nguyen"
    )


if __name__ == "__main__":
    # Start the bot
    application = ApplicationBuilder().token(BOT_TELEGRAM_TOKEN).build()

    # Add a handler when the bot receive the command "/start", and a callback function to run after it got /start
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    # This function will keep running and get update to telegram to fetch the latest update to our bot
    application.run_polling()
