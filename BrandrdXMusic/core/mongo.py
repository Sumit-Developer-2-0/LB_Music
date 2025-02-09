from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

import config

from ..logging import LOGGER

TEMP_MONGODB = ""


# Check if a MongoDB URI is provided in the configuration
if config.MONGO_DB_URI is None:
    # If no URI is provided, fall back to a temporary in-memory MongoDB

    LOGGER(__name__).warning("No MONGO DB URL found. Using a temporary in-memory MongoDB. Data will NOT be persistent.")

    # Create a Pyrogram client to retrieve the bot's username for creating a unique database name
    temp_client = Client(
        "BrandrdXMusic",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()

    # Initialize MongoDB clients using the temporary URI
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)

    # Create database instances using the bot's username
    mongodb = _mongo_async_[username]  # Asynchronous MongoDB client
    pymongodb = _mongo_sync_[username]  # Synchronous MongoDB client

else:
    # If a MongoDB URI is provided, connect to the specified MongoDB instance

    # Initialize MongoDB clients using the provided URI
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)

    # Create database instances
    mongodb = _mongo_async_.BrandrdXMusic  # Asynchronous MongoDB client
    pymongodb = _mongo_sync_.BrandrdXMusic  # Synchronous MongoDB client