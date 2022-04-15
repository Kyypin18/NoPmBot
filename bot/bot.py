""" Aasf Bot """

from pyrogram import (
    Client,
    __version__
)
from bot import (
    API_HASH,
    APP_ID,
    OWNER_ID,
    PM_IMG,
    LOGGER,
    START_COMMAND,
    START_OTHER_USERS_TEXT,
    TOKEN,
    TG_BOT_WORKERS
)


START_TEXT = f"""
<b>Whassup Buddy !
"""

class Bot(Client):
    """ modded client for NoPMsBot """
    commandi = {}

    def __init__(self):
        super().__init__(
            "NoPMsBot",
            api_hash=API_HASH,
            api_id=APP_ID,
            bot_token=TOKEN,
            plugins={
                "root": "bot/plugins"
            },
            workers=TG_BOT_WORKERS
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        try:
            check_m = await self.get_messages(
                chat_id=OWNER_ID,
                message_ids=START_OTHER_USERS_TEXT,
                replies=0
            )
        except ValueError:
            self.commandi[START_COMMAND] = START_TEXT
        else:
            if check_m:
                self.commandi[START_COMMAND] = check_m.text.html
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
            "© 2022 - 2023 @skytrixsz."
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("BOT STOPPED.")
