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

#Биография
#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('keyboaord2_button'))
async def Биография(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    if code == 1:
        await dp.send_message(callback_query.from_user.id, "Тебя зовут - " + str(get_data(callback_query.from_user.id, 'name')))
    if code == 2:
        await dp.send_message(callback_query.from_user.id, "У тебя " + str(get_data(callback_query.from_user.id, 'balance')) + "💎")
    if code == 3:
        val = get_data(callback_query.from_user.id,'promo1') + get_data(callback_query.from_user.id,'promo2')
        await dp.send_message(callback_query.from_user.id, "Ты использовал " + str(val) + " промокод/а/ов")
    if code == 4:
        await dp.send_message(callback_query.from_user.id, "Вот сколько у тебя крипты:")
        await dp.send_message(callback_query.from_user.id,
            fmt.text(
            fmt.text("ЛешаКоин: ", get_data(callback_query.from_user.id,'leshaСoin')),
            fmt.text("СмешиКоин: ", get_data(callback_query.from_user.id,'smeshiСoin')),
            fmt.text("ГрафиКоин: ", get_data(callback_query.from_user.id,'grafiCoin')),
            fmt.text("Блин я второй коин: ", get_data(callback_query.from_user.id,'b_ya_v_Coin')),
            sep="\n"
            ), parse_mode="HTML"
            )
    if code == 5:
        await dp.send_message(callback_query.from_user.id, 'Какое же имущество у тебя есть!',reply_markup=kb_have)

def reg_handlers_biography(bot: Dispatcher):
    bot.register_callback_query_handler(Биография,lambda c: c.data and c.data.startswith('keyboaord2_button'))