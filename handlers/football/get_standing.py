"""
This module provides functionality to get the Premier League Standing Table
from the Football-Data API and send it to a Telegram chat.
"""
from telegram import Update
from telegram.ext import ContextTypes

from client_session import create_client_session


async def get_standing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Gets the current Premier League standing table from the Football-Data API
    and sends it to a Telegram chat.

    Args:
        update (telegram.Update): The `Update` object representing the incoming message.
        context (telegram.ext.Context): The `Context` object representing the current
        state of the bot.

    Returns:
        None
    """
    if not update.effective_chat:
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""Getting the Premier League Standing Table""",
    )
    # Send a sticker using the sticker id
    # How to get a sticker id:
    # https://stackoverflow.com/questions/34355648/telegram-getting-file-id-for-existing-sticker
    await context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        disable_notification=True,
        sticker="CAACAgIAAxkBAAPhZFFwJxT92fned0LYptYIXtuCcBUAAgIBAAJWnb0KTuJsgctA5P8vBA",
    )
    # Get the session object, should only use the same session object in all requests
    # Read more: https://docs.aiohttp.org/en/stable/client_quickstart.html#make-a-request
    session = await create_client_session()
    # TODO: Not hard code League

    # Make the request
    # Get the standing
    async with session.get(url="/v4/competitions/PL/standings") as res:
        if res.status == 200:
            data = await res.json()
            current_standings = data["standings"][0]["table"]
            standing_descriptions = list(
                f"{standing['position']} - {standing['team']['shortName']}"
                for standing in current_standings
            )

            standing_list_message = "\n".join(standing_descriptions)

            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Here are the current Premier League standing:\n{standing_list_message}",
            )

    # Close session
    await session.close()
