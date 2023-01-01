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
        
    await mes.delete()

    if code == 1:
        item1 = types.InlineKeyboardButton("7А", callback_data='go_dif0')
        item2 = types.InlineKeyboardButton("7Б", callback_data='go_dif1')
        item3 = types.InlineKeyboardButton("7В", callback_data='go_dif2')
        item4 = types.InlineKeyboardButton("7Г", callback_data='go_dif3')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3, item4)
        mes = await dp.send_message(callback_query.from_user.id, 'В какую облать?', reply_markup=markup)
    elif code == 3:
        item1 = types.InlineKeyboardButton("Верхний", callback_data='go_dif5')
        item2 = types.InlineKeyboardButton("Нижний", callback_data='go_dif6')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        mes = await dp.send_message(callback_query.from_user.id, 'В какой город?', reply_markup=markup)
        async with state.proxy() as data:
            data['mes'] = mes

    async with state.proxy() as data:
        data['mes'] = mes

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('go_dif'))
async def Ехать_или_нет(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    async with state.proxy() as data:
        mes = data['mes']
        await state.finish()

    await mes.delete()

    item1 = types.InlineKeyboardButton("Поехали", callback_data='poex1')
    item2 = types.InlineKeyboardButton("Отмена", callback_data='poex2')
    markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
    k = random.uniform(1,1.2)
    pay = round(150 * k)
    kuda = code

    if get_data(callback_query.from_user.id,'balance') >= pay:
        if get_data(callback_query.from_user.id, 'location') == kuda_mes[kuda]:
            await dp.send_message(callback_query.from_user.id, 'Зачем тебе ехать туда, если ты уже там???')
        else:
            mes = await dp.send_message(callback_query.from_user.id, f'Стоимость поездки = {str(pay)}💎', reply_markup=markup)
            async with state.proxy() as data:
                data['mes'] = mes
                data['kuda'] = kuda
                data['pay'] = pay
    else:
        await dp.send_message(callback_query.from_user.id, 'У тебя нет денег)=')

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('poex'))
async def Едим(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    async with state.proxy() as data:
        mes = data['mes']
        kuda = data['kuda']
        pay = data['pay']
    await state.finish()

    await mes.delete()

    if code == 1:
        wait_sec = random.randint(10,30)
        wait = await dp.send_message(callback_query.from_user.id, f'Через {wait_sec} секунд ты приедешь(=',reply_markup=types.ReplyKeyboardRemove())
        status_pred = get_data(callback_query.from_user.id, 'status')
        send_data(callback_query.from_user.id, 'status', 3)
        await asyncio.sleep(wait_sec)
        await wait.delete()
        send_data(callback_query.from_user.id, 'balance', get_data(callback_query.from_user.id,'balance')-pay)
        send_data(callback_query.from_user.id, 'location', kuda_mes[kuda])
        if kuda_mes[kuda] == 'Столица': await dp.send_message(callback_query.from_user.id, f'Ты приехал) -{pay}💎',reply_markup=kb_menu_st)
        elif kuda_mes[kuda] == 'Верхний город' or kuda_mes[kuda] == 'Нижний город': await dp.send_message(callback_query.from_user.id, f'Ты приехал) -{pay}💎',reply_markup=kb_menu_gr)
        else: await dp.send_message(callback_query.from_user.id, f'Ты приехал) -{pay}💎',reply_markup=kb_menu)
        send_data(callback_query.from_user.id, 'status', status_pred)
    elif code == 2:
        await dp.send_message(callback_query.from_user.id, 'Ок)')

def reg_handlers_map(bot: Dispatcher):
    bot.register_callback_query_handler(Поехать_в_область,lambda c: c.data and c.data.startswith('map_go'))
    bot.register_callback_query_handler(Ехать_или_нет,lambda c: c.data and c.data.startswith('go_dif'))
    bot.register_callback_query_handler(Едим,lambda c: c.data and c.data.startswith('poex'))