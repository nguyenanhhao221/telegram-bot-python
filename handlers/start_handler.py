from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /start command. Sends a greeting message to the user.

    Args:
        update (telegram.Update): The update object representing the user's
        message.
        context (telegram.ext.CallbackContext): The context object for
        the current update.

    Returns:
        None: The function is asynchronous and does not return anything.
        The message is sent using `context.bot.send_message`.
    """

    if not update.effective_chat:
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""Hello I'm a bot created by Hao Nguyen""",
    )
