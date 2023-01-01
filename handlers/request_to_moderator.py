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

#Заявка модера
#@bot.message_handler(state=Form_moder.moder)
async def Заявка_модеру(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        await dp.send_message(group_id, "@" + message.from_user.username + ": " + data['text'])
        location = get_data(message.from_user.id, 'location')
        if location == 'Столица': await dp.send_message(message.from_user.id, "Все отправила. Жди ответа😁", reply_markup=kb_menu_st)
        elif location == 'Верхний город' or location == 'Нижний город': await dp.send_message(message.from_user.id, "Все отправила. Жди ответа😁)", reply_markup=kb_menu_gr)
        else: await dp.send_message(message.from_user.id, "Все отправила. Жди ответа😁", reply_markup=kb_menu)
    await state.finish()

def reg_handlers_request_to_moderator(bot: Dispatcher):
    bot.register_message_handler(Заявка_модеру,state=Form_moder.moder)