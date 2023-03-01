import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

storage = MemoryStorage()

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
db = Dispatcher(bot )
ADMIN = [5416111170, 5416111170]

dp = Dispatcher(bot=bot, storage=storage)


