from telegram import Update
from telegram.ext import ContextTypes

from client_session import create_client_session


async def get_standing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_chat:
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""Getting the Premier League Standing Table""",
    )
    # Get the session object, should only use the same session object in all requests
    # Read more: https://docs.aiohttp.org/en/stable/client_quickstart.html#make-a-request
    session = await create_client_session()
    # Add params
    params = {"season": 2022}
    # TODO: Not hard code year, not hard code League

    # Make the request
    async with session.get(url="/v4/competitions/PL/standings", params=params) as res:
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
