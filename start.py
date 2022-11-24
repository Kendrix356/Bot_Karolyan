from constants import *
from objects import *
from Function import *
from fsm import *

from create_bot import dp,bot

from handlers import admin_panal
from handlers import biography
from handlers import buizness
from handlers import casino_777
from handlers import crypto_exchange
from handlers import map
from handlers import menu
from handlers import promocodes
from handlers import request_to_moderator
from handlers import school
from handlers import workers
from handlers import start

import asyncio
import random
import time
from threading import Thread

import sqlite3
import aiogram.utils.markdown as fmt
import aiogram.utils.markdown as md
from aiogram import Bot, types
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup

# thread = Thread(target=run)
# thread.start()
thread_buizness = Thread(target=run_buizness)
thread_buizness.start()

start.reg_handlers_start(bot)
admin_panal.reg_handlers_admin_panel(bot)
biography.reg_handlers_biography(bot)
buizness.reg_handlers_buizness(bot)
casino_777.reg_handlers_casino_777(bot)
crypto_exchange.reg_handlers_crypto_exchange(bot)
map.reg_handlers_map(bot)
promocodes.reg_handlers_promocodes(bot)
request_to_moderator.reg_handlers_request_to_moderator(bot)
school.reg_handlers_school(bot)
workers.reg_handlers_school(bot)
menu.reg_handlers_menu(bot)

executor.start_polling(bot,skip_updates=True)
