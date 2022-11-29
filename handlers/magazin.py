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
        item1 = InlineKeyboardButton('Дешевый класс', callback_data='class_m_1')
        item2 = InlineKeyboardButton('Средний класс', callback_data='class_m_2')
        item3 = InlineKeyboardButton('Дорогой класс', callback_data='class_m_3')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)     
    elif code == 5:
        pass
    mes = await dp.send_message(callback_query.from_user.id, 'Выбери что нужно:', reply_markup=markup)
    async with state.proxy() as data:
        data['mes_mag'] = mes

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('class_m_'))
async def Распределение_классов(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    async with state.proxy() as data:
        mes = data['mes_mag']

    await mes.delete()

    if code == 1:
        item1 = InlineKeyboardButton('Lada Granta', callback_data='vesh_8')
        item2 = InlineKeyboardButton('Lada Vesta', callback_data='vesh_9')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Выбери что нужно:', reply_markup=markup)
    elif code == 2:
        item1 = InlineKeyboardButton('BMV 5', callback_data='kup_10')
        item2 = InlineKeyboardButton('Mercedes W222', callback_data='kup_11')
        item3 = InlineKeyboardButton('Audi A4', callback_data='kup_12')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)
        mes = await dp.send_message(callback_query.from_user.id, 'Выбери что нужно:', reply_markup=markup)
    elif code == 3:
        item1 = InlineKeyboardButton('Tesla Model X', callback_data='kup_13')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Выбери что нужно:', reply_markup=markup)
    async with state.proxy() as data:
        data['mes_mag'] = mes

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('vesh_'))
async def Магазин_описание(callback_query: types.CallbackQuery, state: FSMContext):
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
        mes = await dp.send_message(callback_query.from_user.id, 'Трофей: <b>Трофей(1750)</b> \nХарактеристеки:\nУровень: 1750\nЦена: 2.000', reply_markup=markup)
    elif code == 6:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_6')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Трофей: <b>Трофей(3000)</b> \nХарактеристеки:\nУровень: 3000\nЦена: 3.250', reply_markup=markup)
    elif code == 7:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_7')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Трофей: <b>Трофей Михаила</b> \nХарактеристеки:\nПроисходжение: Миша\nЦена: 12.750', reply_markup=markup)
    #Машины
    elif code == 8:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_8')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Машина: <b>Lada Granta</b> \nХарактеристеки:\nМощность: 90 лс.\nРасход: 8л.(100км)\nМакс. Скорость: 175 км/ч\nЦена: 130.000', reply_markup=markup)
    elif code == 9:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_9')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Машина: <b>Lada Vesta</b> \nХарактеристеки:\nМощность: 106 лс.\nРасход: 9л.(100км)\nМакс. Скорость: 190 км/ч\nЦена: 175.000', reply_markup=markup)
    elif code == 10:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_10')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Машина: <b>BMV 5</b> \nХарактеристеки:\nМощность: 450 лс.\nРасход: 10л.(100км)\nМакс. Скорость: 240 км/ч\nЦена: 420.000', reply_markup=markup)
    elif code == 11:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_11')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Машина: <b>Mercedes W222</b> \nХарактеристеки:\nМощность: 450 лс.\nРасход: 12л.(100км)\nМакс. Скорость: 230 км/ч\nЦена: 365.000', reply_markup=markup)
    elif code == 12:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_12')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Машина: <b>Audi A4</b> \nХарактеристеки:\nМощность: 400 лс.\nРасход: 11л.(100км)\nМакс. Скорость: 250 км/ч\nЦена: 400.000', reply_markup=markup)
    elif code == 13:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_13')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Машина: <b>Tesla Model S Plaid</b> \nХарактеристеки:\nМощность: 1 034 лс.\nРасход: 1 разрядка (600км)\nМакс. Скорость: 322 км/ч\nЦена: 850.000', reply_markup=markup)
    async with state.proxy() as data:
        data['mes_mag'] = mes

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('kup_'))
async def Магазин_продажа(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    async with state.proxy() as data:
        mes = data['mes_mag']

    await mes.delete()

    balance = get_data(callback_query.from_user.id, 'balance')
    if code == 1:
        pay = 10000
        if balance >= pay:
            await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
            send_data(callback_query.from_user.id, 'buizness', 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
            pay = 0
    elif code == 2:
        pay = 22000
        if balance >= pay:
            await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
            send_data(callback_query.from_user.id, 'buizness', 2)
        else:
            await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
            pay = 0
    elif code == 3:
        pay = 300
        pass
    elif code == 4:
        pay = 450
        pass
    elif code == 5:
        pay = 2000
        if balance >= pay:
            await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
            inventory_add(callback_query.from_user.id,1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
            pay = 0
    elif code == 6:
        pay = 3250
        if balance >= pay:
            await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
            inventory_add(callback_query.from_user.id,2)
        else:
            await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
            pay = 0
    elif code == 7:
        pay = 12750
        if balance >= pay:
            await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
            inventory_add(callback_query.from_user.id,3)
        else:
            await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
            pay = 0
    elif code == 8:
        pay = 130000
        if balance >= pay:
            await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
            inventory_add(callback_query.from_user.id,4)
        else:
            await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
            pay = 0
    elif code == 9:
        pay = 175000
        if balance >= pay:
            await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
            inventory_add(callback_query.from_user.id,5)
        else:
            await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
            pay = 0
    elif code == 10:
        pay = 420000
        if balance >= pay:
            await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
            inventory_add(callback_query.from_user.id,6)
        else:
            await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
            pay = 0
    elif code == 11:
        pay = 365000
        if balance >= pay:
            await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
            inventory_add(callback_query.from_user.id,7)
        else:
            await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
            pay = 0
    elif code == 12:
        pay = 400000
        if balance >= pay:
            await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
            inventory_add(callback_query.from_user.id,8)
        else:
            await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
            pay = 0
    elif code == 13:
        pay = 850000
        if balance >= pay:
            await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
            inventory_add(callback_query.from_user.id,9)
        else:
            await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
            pay = 0
    elif code == 0:
        await dp.send_message(callback_query.from_user.id, 'Ок')

    if code != 0:
        send_data(callback_query.from_user.id, 'balance', get_data(callback_query.from_user.id, 'balance') - pay)

def reg_handlers_magazin(bot: Dispatcher):
    bot.register_callback_query_handler(Магазин,lambda c: c.data and c.data.startswith('mag_'))
    bot.register_callback_query_handler(Распределение_классов,lambda c: c.data and c.data.startswith('class_m_'))
    bot.register_callback_query_handler(Магазин_описание,lambda c: c.data and c.data.startswith('vesh_'))
    bot.register_callback_query_handler(Магазин_продажа,lambda c: c.data and c.data.startswith('kup_'))