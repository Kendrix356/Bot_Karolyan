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

async def Ставка(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['stavka'] = message.text
        if data['stavka'].isdigit():
            if get_data(message.chat.id, 'balance') >= int(data['stavka']):
                item1 = types.InlineKeyboardButton("Автомат777", callback_data='cas_1')
                item2 = types.InlineKeyboardButton("Коинфлип", callback_data='cas_2')
                item3 = types.InlineKeyboardButton("Башня", callback_data='cas_3')
                markup = InlineKeyboardMarkup(row_width=1).add(item1, item2, item3)
                await dp.send_message(message.chat.id, 'Ставка: '+ data['stavka'] + '\nВо что играть будем?',reply_markup=markup)
            else:
                await dp.send_message(message.chat.id, 'Нету деняг)=')
        else:
            await dp.send_message(message.chat.id, "Это должна быть цифра")
        await state.finish()

async def Игра_казино(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    bal = get_data(callback_query.from_user.id,'balance')

    async with state.proxy() as data:
        if code == 1:
            await dp.send_message(callback_query.from_user.id, 'Поехали🍀')
            choice = random.choices(nums, k=3)
            bal = bal - int(data['stavka'])
            if choice == ['1', '1', '1']:
                await dp.send_message(callback_query.from_user.id, 'Барабан:')
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[0])
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[1])
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[2])
                time.sleep(1)
                bal = bal + int(data['stavka']) * 1.5
                print('+',bal,'💎')
            elif choice == ['2', '2', '2']:
                await dp.send_message(callback_query.from_user.id, 'Барабан:')
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[0])
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[1])
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[2])
                time.sleep(1)
                bal = bal + int(data['stavka']) * 2
                print('+',bal,'💎')
            elif choice == ['3', '3', '3']:
                await dp.send_message(callback_query.from_user.id, 'Барабан:')
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[0])
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[1])
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[2])
                time.sleep(1)
                bal = bal + int(data['stavka']) * 3
                print('+',bal,'💎')
            elif choice == ['0', '0', '0']:
                await dp.send_message(callback_query.from_user.id, 'Барабан:')
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[0])
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[1])
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[2])
                time.sleep(1)
                bal = bal + int(data['stavka']) * 1
                print('+',bal,'💎')
            else:
                await dp.send_message(callback_query.from_user.id, 'Барабан:')
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[0])
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[1])
                time.sleep(1)
                await dp.send_message(callback_query.from_user.id, choice[2])
                time.sleep(1)
            await dp.send_message(callback_query.from_user.id, 'Ваш баланс ' + str(bal) + '💎')
            send_data(callback_query.from_user.id, 'balance', bal)
        elif code == 2:
            pass
        elif code == 3:
            pass
    await state.finish()

def reg_handlers_casino(bot: Dispatcher):
    bot.register_message_handler(Ставка,state=Form_cas.stavka)
    bot.register_callback_query_handler(Игра_казино,lambda c: c.data and c.data.startswith('cas_'))