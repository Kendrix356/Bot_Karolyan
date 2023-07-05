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

    await callback_query.message.delete()

    if code == 1:
        item1 = InlineKeyboardButton('Автомат с едой', callback_data='vesh_01')
        item2 = InlineKeyboardButton('Кофейня', callback_data='vesh_02')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
    elif code == 2:
        item1 = InlineKeyboardButton('Скидка 20% на такси', callback_data='vesh_03')
        item2 = InlineKeyboardButton('Увелечение работы бизнеса на 25%', callback_data='vesh_04')
        markup = InlineKeyboardMarkup(row_width=1).add(item1, item2)
    elif code == 3:
        item1 = InlineKeyboardButton('Трофей(1750)', callback_data='vesh_05')
        item2 = InlineKeyboardButton('Трофей(3000)', callback_data='vesh_06')
        item3 = InlineKeyboardButton('Трофей Михаила', callback_data='vesh_07')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)
    elif code == 4:
        item1 = InlineKeyboardButton('Дешевый класс', callback_data='class_m_1')
        item2 = InlineKeyboardButton('Средний класс', callback_data='class_m_2')
        item3 = InlineKeyboardButton('Дорогой класс', callback_data='class_m_3')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)     
    elif code == 5:
        item1 = InlineKeyboardButton('Дома и квартиры Верхнего города', callback_data='class_m_4')
        item2 = InlineKeyboardButton('Дома и квартиры Нижнего города', callback_data='class_m_5')
        item3 = InlineKeyboardButton('Квартира в столице!', callback_data='vesh_30')
        markup = InlineKeyboardMarkup(row_width=1).add(item1, item2, item3)
    mes = await dp.send_message(callback_query.from_user.id, 'Выбери что нужно:', reply_markup=markup)

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('class_m_'))
async def Распределение_классов(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    await callback_query.message.delete()

    if code == 1:
        item1 = InlineKeyboardButton('Lada Granta', callback_data='vesh_08')
        item2 = InlineKeyboardButton('Lada Vesta', callback_data='vesh_09')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Выбери что нужно:', reply_markup=markup)
    elif code == 2:
        item1 = InlineKeyboardButton('BMV 5', callback_data='vesh_10')
        item2 = InlineKeyboardButton('Mercedes W222', callback_data='vesh_11')
        item3 = InlineKeyboardButton('Audi A4', callback_data='vesh_12')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)
        mes = await dp.send_message(callback_query.from_user.id, 'Выбери что нужно:', reply_markup=markup)
    elif code == 3:
        item1 = InlineKeyboardButton('Tesla Model X', callback_data='vesh_13')
        markup = InlineKeyboardMarkup(row_width=2).add(item1)
        mes = await dp.send_message(callback_query.from_user.id, 'Выбери что нужно:', reply_markup=markup)
    elif code == 4:
        item1 = InlineKeyboardButton('Дом1', callback_data='vesh_14')
        item2 = InlineKeyboardButton('Дом2', callback_data='vesh_15')
        item3 = InlineKeyboardButton('Дом3', callback_data='vesh_16')
        item4 = InlineKeyboardButton('Дом4', callback_data='vesh_17')
        item5 = InlineKeyboardButton('Дом5', callback_data='vesh_18')
        item6 = InlineKeyboardButton('Дом6', callback_data='vesh_19')
        item7 = InlineKeyboardButton('Квартира1', callback_data='vesh_20')
        item8 = InlineKeyboardButton('Квартира2', callback_data='vesh_21')
        markup = InlineKeyboardMarkup(row_width=3).add(item1, item2, item3, item4, item5, item6, item7, item8)
        mes = await dp.send_message(callback_query.from_user.id, 'Выбери что нужно:', reply_markup=markup)
    elif code == 5:
        item1 = InlineKeyboardButton('Дом1', callback_data='vesh_22')
        item2 = InlineKeyboardButton('Дом2', callback_data='vesh_23')
        item3 = InlineKeyboardButton('Дом3', callback_data='vesh_24')
        item4 = InlineKeyboardButton('Дом4', callback_data='vesh_25')
        item5 = InlineKeyboardButton('Дом5', callback_data='vesh_26')
        item6 = InlineKeyboardButton('Дом6', callback_data='vesh_27')
        item7 = InlineKeyboardButton('Квартира1', callback_data='vesh_28')
        item8 = InlineKeyboardButton('Квартира2', callback_data='vesh_29')
        markup = InlineKeyboardMarkup(row_width=3).add(item1, item2, item3, item4, item5, item6, item7, item8)
        mes = await dp.send_message(callback_query.from_user.id, 'Выбери что нужно:', reply_markup=markup)

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('vesh_'))
async def Магазин_описание(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[5:7]
    if code.isdigit():
        code = int(code)

    await callback_query.message.delete()

    #Бизнесы
    if code == 1:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_01')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Бизнес: <b>Автомат с едой</b> \nХарактеристеки:\nЗаработок в час: 20\nЗаработок в день: 480\nЗаработок после окупа в день: 288\nЦена: 10.000', reply_markup=markup)
    elif code == 2:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_02')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Бизнес: <b>Кофейня</b> \nХарактеристеки:\nЗаработок в час: 35\nЗаработок в день: 840\nЗаработок после окупа в день: 504\nЦена: 22.000', reply_markup=markup)
    #Бустеры
    elif code == 3:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_03')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Бустер: <b>Скидка 20% на такси</b> \nХарактеристеки:\nДействует: 1 час\nЦена: 300\n<b>ВНИМАНИЕ, бустер действует до начала след. часа</b>', reply_markup=markup) 
    elif code == 4:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_04')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Бустер: <b>Увелечение работы бизнеса на 25%</b> \nХарактеристеки:\nДействует: 24 часа\nЦена: 450\n<b>ВНИМАНИЕ, бустер действует до начала след. часа (после 23-ого)</b>', reply_markup=markup) 
    #Трофеи
    elif code == 5:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_05')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Трофей: <b>Трофей(1750)</b> \nХарактеристеки:\nУровень: 1750\nЦена: 2.000', reply_markup=markup)
    elif code == 6:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_06')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Трофей: <b>Трофей(3000)</b> \nХарактеристеки:\nУровень: 3000\nЦена: 3.250', reply_markup=markup)
    elif code == 7:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_07')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Трофей: <b>Трофей Михаила</b> \nХарактеристеки:\nПроисходжение: Миша\nЦена: 12.750', reply_markup=markup)
    #Машины
    elif code == 8:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_08')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Машина: <b>Lada Granta</b> \nХарактеристеки:\nМощность: 90 лс.\nРасход: 8л.(100км)\nМакс. Скорость: 175 км/ч\nЦена: 130.000', reply_markup=markup)
    elif code == 9:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_09')
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
    #Дома и квартиры (Верхний)
    elif code == 14:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_14')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Дом1(Верхний город)</b> \nХарактеристеки:\nКачество: 5/10.\nЦена: 230.000', reply_markup=markup)
    elif code == 15:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_15')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Дом2(Верхний город)</b> \nХарактеристеки:\nКачество: 5/10.\nЦена: 230.000', reply_markup=markup)
    elif code == 16:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_16')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Дом3(Верхний город)</b> \nХарактеристеки:\nКачество: 5/10.\nЦена: 230.000', reply_markup=markup)
    elif code == 17:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_17')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Дом4(Верхний город)</b> \nХарактеристеки:\nКачество: 8/10.\nЦена: 580.000', reply_markup=markup)
    elif code == 18:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_18')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Дом5(Верхний город)</b> \nХарактеристеки:\nКачество: 8/10.\nЦена: 580.000', reply_markup=markup)
    elif code == 19:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_19')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Дом6(Верхний город)</b> \nХарактеристеки:\nКачество: 8/10.\nЦена: 580.000', reply_markup=markup)
    elif code == 20:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_20')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Квартира1(Верхний город)</b> \nХарактеристеки:\nКачество: 3/10.\nЦена: 130.000', reply_markup=markup)
    elif code == 21:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_21')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Квартира2(Верхний город)</b> \nХарактеристеки:\nКачество: 7/10.\nЦена: 285.000', reply_markup=markup)
    
    #Дома и квартиры (Нижний)
    elif code == 22:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_22')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Дом1(Нижний город)</b> \nХарактеристеки:\nКачество: 5/10.\nЦена: 230.000', reply_markup=markup)
    elif code == 23:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_23')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Дом2(Нижний город)</b> \nХарактеристеки:\nКачество: 5/10.\nЦена: 230.000', reply_markup=markup)
    elif code == 24:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_24')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Дом3(Нижний город)</b> \nХарактеристеки:\nКачество: 5/10.\nЦена: 230.000', reply_markup=markup)
    elif code == 25:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_25')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Дом4(Нижний город)</b> \nХарактеристеки:\nКачество: 8/10.\nЦена: 580.000', reply_markup=markup)
    elif code == 26:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_26')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Дом5(Нижний город)</b> \nХарактеристеки:\nКачество: 8/10.\nЦена: 580.000', reply_markup=markup)
    elif code == 27:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_27')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Дом6(Нижний город)</b> \nХарактеристеки:\nКачество: 8/10.\nЦена: 580.000', reply_markup=markup)
    elif code == 28:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_28')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Квартира1(Нижний город)</b> \nХарактеристеки:\nКачество: 3/10.\nЦена: 130.000', reply_markup=markup)
    elif code == 29:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_29')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Квартира2(Нижний город)</b> \nХарактеристеки:\nКачество: 7/10.\nЦена: 285.000', reply_markup=markup)
    
    #Дома и квартиры (Столица)
    elif code == 30:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_30')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_00')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'Жилье: <b>Квартира(Столица)</b> \nХарактеристеки:\nКачество: 11/10.\nЦена: 1.800.000', reply_markup=markup)

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('kup_'))
async def Магазин_продажа(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[4:6]
    if code.isdigit():
        code = int(code)

    await callback_query.message.delete()

    balance = get_data(callback_query.from_user.id, 'balance')
    element = 0
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
        send_data(callback_query.from_user.id, 'buster', 1)
    elif code == 4:
        pay = 450
        send_data(callback_query.from_user.id, 'buster', 224)
    elif code == 5:
        pay = 2000
        element = 1
    elif code == 6:
        pay = 3250
        element = 2
    elif code == 7:
        pay = 12750
        element = 3
    elif code == 8:
        pay = 130000
        element = 4
    elif code == 9:
        pay = 175000
        element = 5
    elif code == 10:
        pay = 420000
        element = 6
    elif code == 11:
        pay = 365000
        element = 7
    elif code == 12:
        pay = 400000
        element = 8
    elif code == 13:
        pay = 850000
        element = 9
    elif code == 14:
        pay = 230000
        element = 10
    elif code == 15:
        pay = 230000
        element = 11
    elif code == 16:
        pay = 230000
        element = 12
    elif code == 17:
        pay = 580000
        element = 13
    elif code == 18:
        pay = 580000
        element = 14
    elif code == 19:
        pay = 580000
        element = 15
    elif code == 20:
        pay = 130000
        element = 16
    elif code == 21:
        pay = 285000
        element = 17
    elif code == 22:
        pay = 230000
        element = 18
    elif code == 23:
        pay = 230000
        element = 19
    elif code == 24:
        pay = 230000
        element = 20
    elif code == 25:
        pay = 580000
        element = 21
    elif code == 26:
        pay = 580000
        element = 22
    elif code == 27:
        pay = 580000
        element = 23
    elif code == 28:
        pay = 130000
        element = 24
    elif code == 29:
        pay = 285000
        element = 25
    elif code == 30:
        pay = 1800000
        element = 26

    elif code == 0:
        pay = 0
        await dp.send_message(callback_query.from_user.id, 'Ок')

    if balance >= pay:
        if element != 0:
            try:
                inventory_add(callback_query.from_user.id,element)
                print(element)
                error = 0
            except:
                error = 1
                pay = 0
                await dp.send_message(callback_query.from_user.id, 'У тебя полный инвентарь')
            if error == 0:
                await dp.send_message(callback_query.from_user.id, f'Куплено (-{pay})')
    else:
        await dp.send_message(callback_query.from_user.id, 'Нету деняг)=')
        pay = 0
        
    if code != 0:
        send_data(callback_query.from_user.id, 'balance', get_data(callback_query.from_user.id, 'balance') - pay)

def reg_handlers_magazin(bot: Dispatcher):
    bot.register_callback_query_handler(Магазин,lambda c: c.data and c.data.startswith('mag_'))
    bot.register_callback_query_handler(Распределение_классов,lambda c: c.data and c.data.startswith('class_m_'))
    bot.register_callback_query_handler(Магазин_описание,lambda c: c.data and c.data.startswith('vesh_'))
    bot.register_callback_query_handler(Магазин_продажа,lambda c: c.data and c.data.startswith('kup_'))