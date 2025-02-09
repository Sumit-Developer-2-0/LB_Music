from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Hotty(Client):
    """
    A Pyrogram client for the music bot.

    This class initializes the Pyrogram client with the bot token, API ID,
    and API hash. It also handles starting and stopping the bot, as well as
    performing initial setup tasks such as logging bot information and
    checking admin privileges in the log group.
    """

    def __init__(self):
        """
        Initializes the Pyrogram client with bot configurations.
        """
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="BrandrdXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        """
        Starts the bot and performs initial setup tasks.

        This method starts the Pyrogram client, retrieves bot information
        (ID, name, username, mention), sends a start message to the log group,
        and checks if the bot is an admin in the log group.
        """
        await super().start()
        self.id = self.me.id  # Get the bot's Telegram ID
        self.name = self.me.first_name + " " + (self.me.last_name or "")  # Get the bot's full name
        self.username = self.me.username  # Get the bot's username
        self.mention = self.me.mention  # Get the bot's mention string

        try:
            # Send a start message to the log group/channel
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            # Handle cases where the log group/channel is invalid
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
            )

        except Exception as ex:
            # Handle other exceptions that may occur
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}."
            )

        # Check if the bot is an admin in the log group/channel
        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote your bot as an admin in your log group/channel."
            )

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        """
        Stops the bot.
        """
        await super().stop()
