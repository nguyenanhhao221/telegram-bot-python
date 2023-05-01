"""Handler for the /caps command.
Reply user with their text in ALL CAPS.
"""


from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
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
            chat_id=update.effective_chat.id, text="Please follow a string after /caps"
        )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handling the inline command for the bot.
    This option need to be activate for our bot with @BotFather `/setinline`

        Args:
            update (telegram.Update): The update object representing the user's
            message.
            context (telegram.ext.CallbackContext): The context object for
            the current update. Can represent different thing base on different handler

        Returns:
            None: The function is asynchronous and does not return anything.
            The message is sent using `context.bot.answer_inline_query`.
    """
    if update.inline_query is None:
        return
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title="Caps",
            input_message_content=InputTextMessageContent(query.upper()),
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)
