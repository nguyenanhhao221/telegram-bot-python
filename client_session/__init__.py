import os
from typing import Final

import aiohttp
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
# https://www.football-data.org/documentation/quickstart API KEy
FOOTBALL_ORG_API_KEY: Final = os.getenv("FOOTBALL_ORG_API_KEY")
if not FOOTBALL_ORG_API_KEY:
    raise ValueError("FOOTBALL_ORG_API_KEY is not set up correctly")


async def create_client_session() -> aiohttp.ClientSession:
    return aiohttp.ClientSession(
        base_url="https://api.football-data.org", headers={"X-Auth-Token": FOOTBALL_ORG_API_KEY}
    )
