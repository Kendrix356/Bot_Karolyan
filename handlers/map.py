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

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('map_go'))
async def Поехать_в_область(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    async with state.proxy() as data:
        mes = data['mes']
    await state.finish()
    if code == 1:
        await mes.delete()
        item1 = types.InlineKeyboardButton("7А", callback_data='map_ob_go1')
        item2 = types.InlineKeyboardButton("7Б", callback_data='map_ob_go2')
        item3 = types.InlineKeyboardButton("7В", callback_data='map_ob_go3')
        item4 = types.InlineKeyboardButton("7Г", callback_data='map_ob_go4')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3, item4)
        mes = await dp.send_message(callback_query.from_user.id, 'В какую облать?', reply_markup=markup)
        async with state.proxy() as data:
            data['mes'] = mes

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('map_ob_go'))
async def Ехать_или_нет(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    async with state.proxy() as data:
        mes = data['mes']
    await state.finish()

    await mes.delete()

    item1 = types.InlineKeyboardButton("Поехали", callback_data='map_poexali')
    item2 = types.InlineKeyboardButton("Отмена", callback_data='map_otmena')
    markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
    a = '10'

    if code == 1:
        await dp.send_message(callback_query.from_user.id, 'Стоимость поездки = ' + a + '💎', reply_markup=markup)
    elif code == 2:
        await dp.send_message(callback_query.from_user.id, 'Стоимость поездки = ' + a + '💎', reply_markup=markup)
    elif code == 3:
        await dp.send_message(callback_query.from_user.id, 'Стоимость поездки = ' + a + '💎', reply_markup=markup)
    elif code == 4:
        await dp.send_message(callback_query.from_user.id, 'Стоимость поездки = ' + a + '💎', reply_markup=markup)

def reg_handlers_map(bot: Dispatcher):
    bot.register_callback_query_handler(Поехать_в_область,lambda c: c.data and c.data.startswith('map_go'))
    bot.register_callback_query_handler(Ехать_или_нет,lambda c: c.data and c.data.startswith('map_ob_go'))