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

#Работы
#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('job_'))
async def Работы(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    global situaded
    global answer
    global answers
    global translate_msg
    global right_answer
    global working

    if code == 1:
        working = 1
        answer = 0
        msg1 = await dp.send_message(callback_query.from_user.id, f"Ты выбрал работу - <i>Переводчик</i>")
        time.sleep(1)
        msg2 = await dp.send_message(callback_query.from_user.id, "Ее задача заключается в том, что нужно уметь быcтро переводить текст с английского на русский.")
        time.sleep(3)
        msg3 = await dp.send_message(callback_query.from_user.id, "Через 5 секунд начнется твоя работа, готовься!")
        time.sleep(5)
        await msg1.delete()
        await msg2.delete()
        await msg3.delete()
        await dp.send_message(callback_query.from_user.id, "Начинаем!",reply_markup=kb_stop_work)

        for i in range(10):
            if working == 1:
                answer = 0
                answers+=1
                situaded, correct_word, markup = generate_translate()
                translate_msg = await dp.send_message(callback_query.from_user.id, f"Выбери верный перевод слова '{words_english[correct_word]}' ", reply_markup=markup)
                await asyncio.sleep(5)
                if answer == 0 and working == 1:
                    await translate_msg.delete()
                    time_error = await dp.send_message(callback_query.from_user.id, "Время вышло)=")
                    await asyncio.sleep(1)
                    await time_error.delete()
                    if answers == 10 and working == 1:
                        await dp.send_message(callback_query.from_user.id, f"Вот и поработали) У тебя {right_answer} из 10 правильных. Ты заработал {right_answer*10}💎")
    if code == 2:
        pass
    if code == 3:
        pass

@bot.callback_query_handler(lambda c: c.data and c.data.startswith('translate_'))
async def Переводчик(callback_query: types.CallbackQuery):

    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    global situaded
    global answer
    global answers
    global translate_msg
    global right_answer

    if code == situaded :
        answer = 1
        right_answer+=1
        await translate_msg.delete()
        complete = await dp.send_message(callback_query.from_user.id, 'Правильно(+10💎)')
        await asyncio.sleep(1)
        await complete.delete() 
        if answers == 10:
            await dp.send_message(callback_query.from_user.id, f"Вот и поработали) У тебя {right_answer} из 10 правильных. Ты заработал {right_answer*10}💎")
            send_data(callback_query.from_user.id, 'balance', get_data(callback_query.from_user.id, 'balance') + right_answer*10)
    else:
        answer = 1
        await translate_msg.delete()
        error = await dp.send_message(callback_query.from_user.id, 'Неправильно')
        await asyncio.sleep(1)
        await error.delete() 
        if answers == 10:
            await dp.send_message(callback_query.from_user.id, f"Вот и поработали) У тебя {right_answer} из 10 правильных. Ты заработал {right_answer*10}💎")
            send_data(callback_query.from_user.id, 'balance', get_data(callback_query.from_user.id, 'balance') + right_answer*10)

def reg_handlers_school(bot: Dispatcher):
    bot.register_callback_query_handler(Работы,lambda c: c.data and c.data.startswith('job_'))
    bot.register_callback_query_handler(Переводчик,lambda c: c.data and c.data.startswith('translate_'))