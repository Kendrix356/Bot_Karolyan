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

#Криптобаржа (покупка)
#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('min'))
async def Криптобиржа_продажа(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code2 = callback_query.data[-1]
    if code2.isdigit():
        code2 = int(code2)

    bal = get_data(callback_query.from_user.id, 'balance')

    if code2 == 1:
        if bal >= LeshaCoin:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Потрачено {round(LeshaCoin)}')
            send_data(callback_query.from_user.id, 'balance', round(bal - LeshaCoin))
            send_data(callback_query.from_user.id, 'leshaСoin', (get_data(callback_query.from_user.id, 'leshaСoin')) + 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно средств❌')
    if code2 == 2:
        if bal >= SmeshiСoin:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Потрачено {round(SmeshiСoin)}')
            send_data(callback_query.from_user.id, 'balance', round(bal - SmeshiСoin))
            send_data(callback_query.from_user.id, 'SmeshiСoin', (get_data(callback_query.from_user.id, 'SmeshiСoin')) + 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно средств❌')
    if code2 == 3:
        if bal >= GrafiCoin:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Потрачено {round(GrafiCoin)}')
            send_data(callback_query.from_user.id, 'balance', round(bal - GrafiCoin))
            send_data(callback_query.from_user.id, 'grafiCoin', (get_data(callback_query.from_user.id, 'grafiCoin')) + 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно средств❌')
    if code2 == 4:
        if bal >= Blin_ya_ftoroy_coin:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Потрачено {round(Blin_ya_ftoroy_coin)}')
            send_data(callback_query.from_user.id, 'balance', round(bal - Blin_ya_ftoroy_coin))
            send_data(callback_query.from_user.id, 'b_ya_v_Coin', (get_data(callback_query.from_user.id, 'b_ya_v_Coin')) + 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно средств❌')

#Криптобиржа (продажа)
#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('pls'))
async def Криптобиржа_купить(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code2 = callback_query.data[-1]
    if code2.isdigit():
        code2 = int(code2)

    bal = get_data(callback_query.from_user.id, 'balance')

    if code2 == 1:
        if get_data(callback_query.from_user.id, 'leshaCoin') >= 1:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Получено {round(LeshaCoin - LeshaCoin*0.1)}')
            send_data(callback_query.from_user.id, 'balance', bal+round(LeshaCoin - LeshaCoin*0.1))
            send_data(callback_query.from_user.id, 'leshaCoin', (get_data(callback_query.from_user.id, 'leshaCoin')) - 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно крипты❌')
    if code2 == 2:
        if get_data(callback_query.from_user.id, 'SmeshiСoin') >= 1:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Получено {round(SmeshiСoin - SmeshiСoin*0.1)}')
            send_data(callback_query.from_user.id, 'balance', bal+round(SmeshiСoin - SmeshiСoin*0.1))
            send_data(callback_query.from_user.id, 'SmeshiСoin', (get_data(callback_query.from_user.id, 'SmeshiСoin')) - 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно крипты❌')
    if code2 == 3:
        if get_data(callback_query.from_user.id, 'grafiCoin') >= 1:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Получено {round(GrafiCoin - GrafiCoin*0.1)}')
            send_data(callback_query.from_user.id, 'balance', bal+round(GrafiCoin - GrafiCoin*0.1))
            send_data(callback_query.from_user.id, 'grafiCoin', (get_data(callback_query.from_user.id, 'grafiCoin')) - 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно крипты❌')
    if code2 == 4:
        if get_data(callback_query.from_user.id, 'b_ya_v_Coin') >= 1:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Получено {round(Blin_ya_ftoroy_coin - Blin_ya_ftoroy_coin*0.1)}')
            send_data(callback_query.from_user.id, 'balance', bal+round(Blin_ya_ftoroy_coin - Blin_ya_ftoroy_coin*0.1))
            send_data(callback_query.from_user.id, 'b_ya_v_Coin', (get_data(callback_query.from_user.id, 'b_ya_v_Coin')) - 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно крипты❌')

def reg_handlers_crypto_exchange(bot: Dispatcher):
    bot.register_callback_query_handler(Криптобиржа_продажа,lambda c: c.data and c.data.startswith('min'))
    bot.register_callback_query_handler(Криптобиржа_купить,lambda c: c.data and c.data.startswith('pls'))