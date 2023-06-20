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
                item4 = types.InlineKeyboardButton("Отмена", callback_data='cas_4')
                markup = InlineKeyboardMarkup(row_width=1).add(item1, item2, item3, item4)
                casino_mes = await dp.send_message(message.chat.id, 'Ставка: '+ data['stavka'] + '\nВо что играть будем?',reply_markup=markup)
                async with state.proxy() as data:
                    data['casino_mes'] = casino_mes
            else:
                await dp.send_message(message.chat.id, 'Нету деняг)=')
                await state.finish()
        elif data['stavka'] == "отмена" or data['stavka'] == "Отмена":
            location = get_data(message.from_user.id, 'location')
            if location == 'Столица': await dp.send_message(message.from_user.id, "Окей", reply_markup=kb_menu_st)
            elif location == 'Верхний город' or location == 'Нижний город': await dp.send_message(message.from_user.id, "Окей", reply_markup=kb_menu_gr)
            else: await dp.send_message(message.from_user.id, "Окей", reply_markup=kb_menu)
            await state.finish()
        else:
            await dp.send_message(message.chat.id, "Это должна быть цифра")
            await Form_cas.stavka.set()

async def Игра_казино(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    bal = get_data(callback_query.from_user.id,'balance')

    async with state.proxy() as data:
        casino_mes = data['casino_mes']

    await casino_mes.delete()
    
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
        elif code == 4:
            location = get_data(callback_query.from_user.id, 'location')
            if location == 'Столица': await dp.send_message(callback_query.from_user.id, "Окей", reply_markup=kb_menu_st)
            elif location == 'Верхний город' or location == 'Нижний город': await dp.send_message(callback_query.from_user.id, "Окей", reply_markup=kb_menu_gr)
            else: await dp.send_message(callback_query.from_user.id, "Окей", reply_markup=kb_menu)
    await state.finish()

def reg_handlers_casino(bot: Dispatcher):
    bot.register_message_handler(Ставка,state=Form_cas.stavka)
    bot.register_callback_query_handler(Игра_казино,lambda c: c.data and c.data.startswith('cas_'))