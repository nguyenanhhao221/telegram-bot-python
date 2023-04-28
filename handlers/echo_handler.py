from telegram import Update
from telegram.ext import (
    ContextTypes,
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
