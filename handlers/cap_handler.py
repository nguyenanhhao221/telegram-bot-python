"""Handler for the /caps command.
Reply user with their text in ALL CAPS.
"""

from telegram import Update
from telegram.ext import ContextTypes


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /caps command. Reply user with their text in ALL CAPS.
    Hello

        Args:
            update (telegram.Update): The update object representing the user's
            message.
            context (telegram.ext.CallbackContext): The context object for
            the current update. Can represent different thing base on different handler

        Returns:
            None: The function is asynchronous and does not return anything.
            The message is sent using `context.bot.send_message`.
    """

    if not update.effective_chat or context.args is None:
        return

    text_caps = " ".join(context.args).upper()
    # Handle case if message is empty
    if not context.args:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Pleas follow a string after /caps"
        )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
