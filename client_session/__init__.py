"""
This module provides a function for creating an `aiohttp.ClientSession` 
object with the API key for football-data.org set as a header.

The `create_client_session()` function can be used to create a new `aiohttp.ClientSession` object
that includes the API key for football-data.org in the headers.
This function should be used to ensure that the API key is included
in all requests made to the football-data.org API.

Usage:
    To use this module, import the `create_client_session()` function and 
    call it to create a new `aiohttp.ClientSession` object.

Example:
    import aiohttp
    from client_session import create_client_session

    async with create_client_session() as session:
        async with session.get("https://api.football-data.org/v4/competitions") as response:
            response_data = await response.json()

See https://www.football-data.org/documentation/quickstart 
for more information about the football-data.org API.
"""
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
    """
    Create a new `aiohttp.ClientSession` object with the API key for football-data.org
    set as a header.

    Returns:
        An `aiohttp.ClientSession` object.
    """
    return aiohttp.ClientSession(
        base_url="https://api.football-data.org", headers={"X-Auth-Token": FOOTBALL_ORG_API_KEY}
    )
