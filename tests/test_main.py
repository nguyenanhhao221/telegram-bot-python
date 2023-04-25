import unittest
import os
from dotenv import load_dotenv


load_dotenv()


class TestEnv(unittest.TestCase):
    # Class method is a function defined inside a class, it can also be used with other instance that create from this class
    @classmethod
    def setUpClass(cls):
        # Load the environment variables from .env files
        load_dotenv()
        cls.BOT_TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
        cls.TELEGRAM_GROUP_CHAT_ID = os.getenv("TELEGRAM_GROUP_ID")

        if not cls.BOT_TELEGRAM_TOKEN:
            raise ValueError(
                "BOT_TELEGRAM_TOKEN is not set correctly in environment variables"
            )

        if not cls.TELEGRAM_GROUP_CHAT_ID:
            raise ValueError(
                "TELEGRAM_GROUP_CHAT_ID is not set correctly in environment variables"
            )

    def test_env_load_correctly(self):
        self.assertIsNotNone(self.BOT_TELEGRAM_TOKEN)
        self.assertIsNotNone(self.TELEGRAM_GROUP_CHAT_ID)


if __name__ == "__main__":
    unittest.main()
