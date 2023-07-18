from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

storage = MemoryStorage()
dp = Bot(token="5095654656:AAGGKQ21-440lk-YNvvtgu2z2wjTAie572Y", parse_mode=types.ParseMode.HTML)
bot = Dispatcher(dp, storage=storage)