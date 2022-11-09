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

@bot.message_handler(commands=['start'])
async def Приветствие(message: types.Message):
    for i in range(len(ids_users)): 
        if message.from_user.id == ids_users[i]:
            try:
                if get_data(message.from_user.id,'register') == 1:
                    await dp.send_message(message.from_user.id, "Привет. Я - бот для группы 7-ого 'Б' класса.Я буду всегда помогать тебе. Но это не правда😁", reply_markup=kb_menu)
                    await Form_name.name.set()
                    await dp.send_message(message.from_user.id,'Напиши пожалалуйста свое реально имя, а то штраф 150(=')
                    register = 0
                    send_data(message.from_user.id, 'register', register)
                else:
                    await dp.send_message(message.from_user.id, "Привет)", reply_markup=kb_menu)
            except:
                reg(message.from_user.id)
                
@bot.message_handler(state=Form_name.name)
async def Регистрация(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        send_data(message.from_user.id, 'name', remove_char(md.bold(data['name'])))
    await state.finish()
    await dp.send_message(message.from_user.id, "Спасибки)")

def reg_handlers_start(bot: Dispatcher):
    bot.register_message_handler(Приветствие,commands=['start'])
    bot.register_message_handler(Регистрация,state=Form_name.name)