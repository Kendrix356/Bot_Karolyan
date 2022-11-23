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

        for i in range(10):
            print(i)
            if i == 0:
                async with state.proxy() as data:
                    working = data['working']
                answer = 0
            else:
                async with state.proxy() as data:
                    working = data['working']
                    answer = data['answer']
            if working == 1:
                situaded, correct_word, markup = generate_translate()
                translate_msg = await dp.send_message(callback_query.from_user.id, f"Выбери верный перевод слова '{words_english[correct_word]}' ", reply_markup=markup)
                async with state.proxy() as data:
                    data['situaded'] = situaded
                await asyncio.sleep(5)
                if answer != 0 and working == 1:

                    if answer == 'Right':
                        right_answer+=1
                        await translate_msg.delete()
                        right = await dp.send_message(callback_query.from_user.id, "Правильно(+10💎)")
                        await asyncio.sleep(1)
                        await right.delete()

                    elif answer == 'Error':
                        await translate_msg.delete()
                        error = await dp.send_message(callback_query.from_user.id, "Неправильно")
                        await asyncio.sleep(1)
                        await error.delete()

                    else:
                        answer = 'Time_error'
                        async with state.proxy() as data:
                            data['answer'] = answer 
                        await translate_msg.delete()
                        time_error = await dp.send_message(callback_query.from_user.id, "Время вышло)=")
                        await asyncio.sleep(1)
                        await time_error.delete()

                    if i == 9:
                        await dp.send_message(callback_query.from_user.id, f"Вот и поработали) У тебя {right_answer} из 10 правильных. Ты заработал {right_answer*10}💎")
                        send_data(callback_query.from_user.id, 'balance', get_data(callback_query.from_user.id, 'balance') + right_answer*10)
    if code == 2:
        pass
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
        line1_S = '00000000000'
        line2_S = '00000000000'
        line3_S = '00000000000'
        line4_S = '00000000000'
        line5_S = '00000000000'
        item_stop = KeyboardButton("Перезагрузить", callback_data='network_1')
        markup = InlineKeyboardMarkup(row_width=2).add(item_stop)
        flag = 0
        state = 0
        i = 0
        while(True): 
            if state == 0:   
                state = 1
                l = random.randint(1,5)
                if l == 1:
                    line1_L = list('00000000000')
                    n = random.randint(0,10)
                    if line1_L[n] == '0':
                        line1_L[n] = '1'
                    line1_S = " ".join(line1_L)
                    line1_S = line1_S.replace(" ","")
                elif l == 2:
                    line2_L = list('00000000000')
                    n = random.randint(0,10)
                    if line2_L[n] == '0':
                        line2_L[n] = '1'
                    line2_S = " ".join(line2_L)
                    line2_S = line2_S.replace(" ","")
                elif l == 3:
                    line3_L = list('00000000000')
                    n = random.randint(0,10)
                    if line3_L[n] == '0':
                        line3_L[n] = '1'
                    line3_S = " ".join(line3_L)
                    line3_S = line3_S.replace(" ","")
                elif l == 4:
                    line4_L = list('00000000000')
                    n = random.randint(0,10)
                    if line4_L[n] == '0':
                        line4_L[n] = '1'
                    line4_S = " ".join(line4_L)
                    line4_S = line4_S.replace(" ","")
                elif l == 5:
                    line5_L = list('00000000000')
                    n = random.randint(0,10)
                    if line5_L[n] == '0':
                        line5_L[n] = '1'
                    line5_S = " ".join(line5_L)
                    line5_S = line5_S.replace(" ","")
                if i != 0:
                    await serever_msg.edit_text(f"{line1_S}\n{line2_S}\n{line3_S}\n{line4_S}\n{line5_S}\n",reply_markup=markup)
                else:
                    i = 1
                    serever_msg = await dp.send_message(callback_query.from_user.id, f"{line1_S}\n{line2_S}\n{line3_S}\n{line4_S}\n{line5_S}\n",reply_markup=markup)
            if flag == 1:
                print('Press')
                line1_L = list('00000000000')
                line2_L = list('00000000000')
                line3_L = list('00000000000')
                line4_L = list('00000000000')
                line5_L = list('00000000000')
                async with state.proxy() as data:
                    data['flag'] = 0
                state = 0
            time = random.randint(5, 15)
            await asyncio.sleep(time)
            async with state.proxy() as data:
                flag = data['flag']


#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('translate_'))
async def Переводчик(callback_query: types.CallbackQuery, state: FSMContext):

    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    async with state.proxy() as data:
        situaded = data['situaded']
        answer = data['answer']

    if code == situaded :
        answer = 'Right'
        async with state.proxy() as data:
            data['answer'] = answer
    else:
        answer = 'Error'
        async with state.proxy() as data:
            data['answer'] = answer         

#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('network_'))
async def Сетевой_админ(callback_query: types.CallbackQuery, state: FSMContext):

    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['flag'] = 1

def reg_handlers_school(bot: Dispatcher):
    bot.register_callback_query_handler(Работы,lambda c: c.data and c.data.startswith('job_'))
    bot.register_callback_query_handler(Переводчик,lambda c: c.data and c.data.startswith('translate_'))
    bot.register_callback_query_handler(Сетевой_админ,lambda c: c.data and c.data.startswith('network_'))
