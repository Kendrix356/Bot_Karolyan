from constants import *
from objects import *
from Function import *
from fsm import *

from create_bot import dp,bot

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

#Школа
#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('keyboaord_school'))
async def Расписание(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    if code == 1:
        try:
            await dp.send_message(callback_query.from_user.id, Raspis[datetime.datetime.today().weekday()])
        except:
            await dp.send_message(callback_query.from_user.id, 'Сегодня выходной!')
    if code == 2:
        await dp.send_message(callback_query.from_user.id, 'Я пока не знаю ответов на музыку')

def reg_handlers_school(bot: Dispatcher):
    bot.register_callback_query_handler(Расписание,lambda c: c.data and c.data.startswith('keyboaord_school'))