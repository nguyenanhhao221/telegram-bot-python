from datetime import datetime
import os

import requests
import pytz
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

IST = pytz.timezone("Asia/Saigon")
raw_TS = datetime.now(IST)
current_date = raw_TS.strftime("%d-%m-%Y")
current_time = raw_TS.strftime("%H:%M:%S")

# Telegram related
BOT_TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_GROUP_CHAT_ID = os.getenv("TELEGRAM_GROUP_ID")
BOT_USERNAME = "@python_vaccine_bot"
msg = f"Message received on {current_date} at {current_time}"
print(msg)


def send_message_telegram(message: str):
    """

    Args:
        message:
    """
    telegram_api_url = f"https://api.telegram.org/bot{BOT_TELEGRAM_TOKEN}/sendMessage"
    params = {
        "chat_id": TELEGRAM_GROUP_CHAT_ID,
        "text": f"{message}",
        "parse_mode": "HTML",
    }
    telegram_response = requests.get(telegram_api_url, params=params)
    if telegram_response.status_code == 200:
        print("INFO: Notification has been sent to Telegram")
    else:
        print("ERROR: Count not send message")


send_message_telegram(msg)
