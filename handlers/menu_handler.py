from telegram import Update
from telegram.ext import ContextTypes


async def get_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Retrieve the list of available commands for the bot and send it to the user.

    Args:
        update (telegram.Update): The update object representing the user's message.
        context (telegram.ext.CallbackContext): The context object for the current update.

    Returns:
        None
    """

    current_commands = await context.bot.get_my_commands()
    if update.effective_chat is None:
        return
    command_descriptions = [
        f"/{command.command} - {command.description}" for command in current_commands
    ]
    command_list_message = "\n".join(command_descriptions)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Here are the available commands you can try: \n{command_list_message}",
    )
