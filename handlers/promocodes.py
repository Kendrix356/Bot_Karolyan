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

#Промокоды
#@bot.message_handler(state=Form_promo.promo)
async def Промокоды(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        global bal
        data['promo'] = message.text

        if data['promo'] == 'eRop1n':
            if get_data(message.from_user.id, 'promo1') == 1:
                await dp.send_message(message.chat.id, 'Поздравляю ты выйграл 100💎')
                bal = get_data(message.chat.id, 'balance') + 100
                send_data(message.chat.id, 'balance', bal)
                send_data(message.chat.id, 'promo1', 0)
            else:  
                await dp.send_message(message.chat.id, 'Ты уже использовал такой промокод')  

        elif data['promo'] == 'Suzanne_well_done':
            if get_data(message.from_user.id, 'promo2') == 1 and message.from_user.id != 1143067536:
                await dp.send_message(message.chat.id, 'Поздравляю ты выйграл 150💎.А также ты поддержал Сюзану денежкой, так как это реферальный код))')
                bal = get_data(message.chat.id, 'balance') + 150
                bal_s = get_data(1143067536, 'balance') + 150

                send_data(message.chat.id, 'balance', bal)
                send_data(1143067536, 'balance', bal_s)
                send_data(message.chat.id, 'promo2', 0)
            else:
                if message.from_user.id == 1143067536:
                    await dp.send_message(message.chat.id, 'Это же твоя рефералка, схитрить хотела?') 
                else:
                    await dp.send_message(message.chat.id, 'Ты уже использовал такой промокод')  
        else:
            await dp.send_message(message.chat.id, 'Такого промокода нету😢')
    await state.finish()

def reg_handlers_promocodes(bot: Dispatcher):
    bot.register_message_handler(Промокоды,state=Form_promo.promo)
