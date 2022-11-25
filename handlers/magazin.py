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

#Магазин
#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('mag_'))
async def Магазин(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    async with state.proxy() as data:
        mes = data['mes_mag']
    
    await mes.delete()

    if code == 1:
        item1 = InlineKeyboardButton('Автомат с едой', callback_data='vesh_1')
        item2 = InlineKeyboardButton('Кофейня', callback_data='vesh_2')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
    elif code == 2:
        item1 = InlineKeyboardButton('Скидка 20% на такси', callback_data='vesh_3')
        item2 = InlineKeyboardButton('Увелечение работы бизнеса на 25%', callback_data='vesh_4')
        markup = InlineKeyboardMarkup(row_width=1).add(item1, item2)
    elif code == 3:
        item1 = InlineKeyboardButton('Трофей(1750)', callback_data='vesh_5')
        item2 = InlineKeyboardButton('Трофей(3000)', callback_data='vesh_6')
        item3 = InlineKeyboardButton('Трофей Михаила', callback_data='vesh_7')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)
    elif code == 4:
        pass     
    elif code == 5:
        pass
    mes = await dp.send_message(callback_query.from_user.id, 'Выбери что нужно:', reply_markup=markup)
    async with state.proxy() as data:
        data['mes_mag'] = mes

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('vesh_'))
async def Магазин_бизнес(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    async with state.proxy() as data:
        mes = data['mes_mag']

    await mes.delete()

    #Бизнесы
    if code == 1:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_1')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Бизнес: <b>Автомат с едой</b> \nХарактеристеки:\nЗаработок в час: 20\nЗаработок в день: 480\nЗаработок после окупа в день: 288\nЦена: 10.000', reply_markup=markup)
    elif code == 2:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_2')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Бизнес: <b>Кофейня</b> \nХарактеристеки:\nЗаработок в час: 35\nЗаработок в день: 840\nЗаработок после окупа в день: 504\nЦена: 22.000', reply_markup=markup)
    #Бустеры
    elif code == 3:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_3')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Бустер: <b>Скидка 20% на такси</b> \nХарактеристеки:\nДействует: 1 час\nЦена: 300', reply_markup=markup) 
    elif code == 4:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_4')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Бустер: <b>Увелечение работы бизнеса на 25%</b> \nХарактеристеки:\nДействует: 1 день\nЦена: 450', reply_markup=markup) 
    #Трофеи
    elif code == 5:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_5')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Трофей: <b>Трофей(1750)</b> \nХарактеристеки:\nУровень: 1750\nЦена: 15.500', reply_markup=markup)
    elif code == 6:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_6')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Трофей: <b>Трофей(3000)</b> \nХарактеристеки:\nУровень: 3000\nЦена: 24.500', reply_markup=markup)
    elif code == 7:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_7')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Трофей: <b>Трофей Михаила</b> \nХарактеристеки:\nПроисходжение: Миша\nЦена: 39.999', reply_markup=markup)
    async with state.proxy() as data:
        data['mes_mag'] = mes

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('kup_'))
async def Продажа(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    async with state.proxy() as data:
        mes = data['mes_mag']

    await mes.delete()

    if code == 1:
        pay = 10000
        if get_data(callback_query.from_user.id, 'balance') >= pay:
            await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
            send_data(callback_query.from_user.id, 'buizness', 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
            pay = 0
    elif code == 2:
        pay = 22000
        if get_data(callback_query.from_user.id, 'balance') >= pay:
            await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
            send_data(callback_query.from_user.id, 'buizness', 2)
        else:
            await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
            pay = 0
    elif code == 0:
        await dp.send_message(callback_query.from_user.id, 'Ок')
    if code != 0:
        send_data(callback_query.from_user.id, 'balance', get_data(callback_query.from_user.id, 'balance') - pay)

def reg_handlers_magazin(bot: Dispatcher):
    bot.register_callback_query_handler(Магазин,lambda c: c.data and c.data.startswith('mag_'))
    bot.register_callback_query_handler(Магазин_бизнес,lambda c: c.data and c.data.startswith('vesh_'))
    bot.register_callback_query_handler(Продажа,lambda c: c.data and c.data.startswith('kup_'))