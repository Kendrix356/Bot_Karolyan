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

#@bot.message_handler(state=Form_cas777.stavka)
async def Автомат777(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        bal = get_data(message.chat.id, 'balance')
        data['other'] = message.text
        if data['other'].isdigit():
            if bal >= int(data['other']):
                await dp.send_message(message.chat.id, 'Поехали🍀')
                choice = random.choices(nums, k=3)
                bal = bal - int(data['other'])
                if choice == ['1', '1', '1']:
                    await dp.send_message(message.chat.id, 'Барабан:')
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[0])
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[1])
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[2])
                    time.sleep(1)
                    bal = bal + int(data['other']) * 1.5
                    print('+',bal,'💎')
                elif choice == ['2', '2', '2']:
                    await dp.send_message(message.chat.id, 'Барабан:')
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[0])
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[1])
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[2])
                    time.sleep(1)
                    bal = bal + int(data['other']) * 2
                    print('+',bal,'💎')
                elif choice == ['3', '3', '3']:
                    await dp.send_message(message.chat.id, 'Барабан:')
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[0])
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[1])
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[2])
                    time.sleep(1)
                    bal = bal + int(data['other']) * 3
                    print('+',bal,'💎')
                elif choice == ['0', '0', '0']:
                    await dp.send_message(message.chat.id, 'Барабан:')
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[0])
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[1])
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[2])
                    time.sleep(1)
                    bal = bal + int(data['other']) * 1
                    print('+',bal,'💎')
                else:
                    await dp.send_message(message.chat.id, 'Барабан:')
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[0])
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[1])
                    time.sleep(1)
                    await dp.send_message(message.chat.id, choice[2])
                    time.sleep(1)
                await dp.send_message(message.chat.id, 'Ваш баланс ' + str(bal) + '💎')
                send_data(message.chat.id, 'balance', bal)
            else:
                await dp.send_message(message.chat.id, 'Нету деняг)=')
        else:
            location = get_data(message.from_user.id, 'location')
            if location == 'Столица': await dp.send_message(message.from_user.id, "Ок", reply_markup=kb_menu_st)
            elif location == 'Верхний город' or location == 'Нижний город': await dp.send_message(message.from_user.id, "Ок", reply_markup=kb_menu)
            else: await dp.send_message(message.from_user.id, "Ок", reply_markup=kb_menu)
        await state.finish()

def reg_handlers_casino_777(bot: Dispatcher):
    bot.register_message_handler(Автомат777,state=Form_cas777.stavka)