"""
For unknown command handlers

"""


from telegram import Update
from telegram.ext import ContextTypes


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handling unknown command that the bot hasn't been set up for
        Args:
            update (telegram.Update): The update object representing the user's
            message.
            context (telegram.ext.CallbackContext): The context object for
            the current update. Can represent different thing base on different handler

        Returns:
            Send a message to the user indicate that unknown command

    """
    if not update.effective_chat:
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Sorry I don't understand your command"
    )
