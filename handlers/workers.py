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
import tracemalloc

tracemalloc.start()

#Работы
#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('job_'))
async def Работы(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    global situaded
    global answer
    global answers
    global translate_msg
    global right_answer

    async with state.proxy() as data:
        works_mes = data['works_mes']

    await works_mes.delete()
    
    if code == 1:
        right_answer = 0
        msg1 = await dp.send_message(callback_query.from_user.id, f"Ты выбрал работу - <i>Переводчик</i>")
        await asyncio.sleep(1)
        msg2 = await dp.send_message(callback_query.from_user.id, "Ее задача заключается в том, что нужно уметь быcтро переводить текст с английского на русский.")
        await asyncio.sleep(3)
        msg3 = await dp.send_message(callback_query.from_user.id, "Через 5 секунд начнется твоя работа, готовься!")
        await asyncio.sleep(5)
        await msg1.delete()
        await msg2.delete()
        await msg3.delete()
        await dp.send_message(callback_query.from_user.id, "Начинаем!",reply_markup=kb_stop_work)
        for i  in range(10):
            async with state.proxy() as data:
                working = data['working']
                data['answer'] = 0
                if i == 0: data['right_answer'] = 0
            if working == 1:
                situaded, correct_word, markup = generate_translate()
                translate_msg = await dp.send_message(callback_query.from_user.id, f"Выбери верный перевод слова '{words_english[correct_word]}' ", reply_markup=markup)
                async with state.proxy() as data:
                    data['situaded'] = situaded
                await asyncio.sleep(5)
                async with state.proxy() as data:
                    answer = data['answer']
                if answer == 0:
                    print('Time_error')
                    answer = 'Time_error'
                    await translate_msg.delete()
                    time_error = await dp.send_message(callback_query.from_user.id, "Время вышло)=")
                    await asyncio.sleep(1)
                    await time_error.delete()

            if i == 9:
                async with state.proxy() as data:
                    right_answer = data['right_answer']
                await dp.send_message(callback_query.from_user.id, f"Вот и поработали) У тебя {right_answer} из 10 правильных. Ты заработал {right_answer*10}💎",reply_markup=kb_income)
                send_data(callback_query.from_user.id, 'balance', get_data(callback_query.from_user.id, 'balance') + right_answer*10)
    if code == 2:
        await dp.send_message(callback_query.from_user.id, "Пока вакансий таксистом нет)=")
    if code == 3:
        msg1 = await dp.send_message(callback_query.from_user.id, f"Ты выбрал работу - <i>Сетевой Администратор</i>")
        await asyncio.sleep(1)
        msg2 = await dp.send_message(callback_query.from_user.id, "Ее задача заключается в том, что нужно уметь быcтро находить ошибки на сервере. Если на каком то канале сервера появится '1' нажимай кнопку исправить")
        await asyncio.sleep(8)
        msg3 = await dp.send_message(callback_query.from_user.id, "Через 5 секунд начнется твоя работа, готовься!")
        await asyncio.sleep(5)
        await msg1.delete()
        await msg2.delete()
        await msg3.delete()
        await dp.send_message(callback_query.from_user.id, "Начинаем!",reply_markup=kb_stop_work)
        array = [[0] * 5 for _ in range(5)]
        asyncio.run(await print_array(callback_query.from_user.id, array))
        asyncio.run(await update_array(array))

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('translate_'))
async def Переводчик(callback_query: types.CallbackQuery, state: FSMContext):

    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    async with state.proxy() as data:
        situaded = data['situaded']
        data['answer'] = 1

    if code == situaded :
        print('Right')
        await translate_msg.delete()
        right = await dp.send_message(callback_query.from_user.id, "Правильно(+10💎)")
        await asyncio.sleep(1)
        await right.delete()
        async with state.proxy() as data:
            data['right_answer'] += 1
    else:
        print('Error')
        await translate_msg.delete()
        error = await dp.send_message(callback_query.from_user.id, "Неправильно")
        await asyncio.sleep(1)
        await error.delete()    

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('network_'))
async def Сетевой_админ(callback_query: types.CallbackQuery, state: FSMContext):

    await dp.answer_callback_query(callback_query.id)
    print('Press')
    async with state.proxy() as data:
        data['state'] = 0
    time = random.randint(5, 15)
    await asyncio.sleep(time)

async def print_array(chat_id, array):
    message = "Массив:\n"
    for row in array:
        message += " ".join(str(cell) for cell in row) + "\n"
    try:
        await serever_msg.edit_text(message)
    except:
        serever_msg = await dp.send_message(chat_id, message)

async def update_array(array):
    while True:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        array[row][col] = 1
        await print_array(array)
        await asyncio.sleep(random.randint(3, 10))
        array[row][col] = 0
        await print_array(array)

def reg_handlers_school(bot: Dispatcher):
    bot.register_callback_query_handler(Работы,lambda c: c.data and c.data.startswith('job_'))
    bot.register_callback_query_handler(Переводчик,lambda c: c.data and c.data.startswith('translate_'))
    bot.register_callback_query_handler(Сетевой_админ,lambda c: c.data and c.data.startswith('network_'))
