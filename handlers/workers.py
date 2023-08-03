from constants import *
from objects import *
from Function import *
from fsm import *

from create_bot import dp,bot

import asyncio
from aiogram import types
from aiogram.dispatcher import Dispatcher

work_data = {}

async def Работы(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    await callback_query.message.delete()
    
    if code == 1:
        right_answer = 0
        msg1 = await dp.send_message(chat_id, f"Ты выбрал работу - <i>Переводчик</i>")
        await asyncio.sleep(1)
        msg2 = await dp.send_message(chat_id, "Ее задача заключается в том, что нужно уметь быcтро переводить текст с английского на русский.")
        await asyncio.sleep(3)
        msg3 = await dp.send_message(chat_id, "Через 5 секунд начнется твоя работа, готовься!")
        await asyncio.sleep(5)
        await msg1.delete()
        await msg2.delete()
        await msg3.delete()
        await dp.send_message(chat_id, "Начинаем!",reply_markup=kb_stop_work)
        work_data[chat_id] = {
                    'working': 1,
                    'answer': 0,
                    'right_answer': 0,
                    'situaded': 0
                    }
        for i  in range(10):
            working = work_data[chat_id]['working']
            work_data[chat_id]['answer'] = 0
            if i == 0: work_data[chat_id]['right_answer'] = 0
            if working == 1:
                situaded, correct_word, markup = generate_translate()
                translate_msg = await dp.send_message(chat_id, f"Выбери верный перевод слова '{words_english[correct_word]}' ", reply_markup=markup)
                work_data[chat_id]['situaded'], work_data[chat_id]['translate_msg'] = situaded, translate_msg
                await asyncio.sleep(5)
                answer = work_data[chat_id]['answer']
                if answer == 0:
                    answer = 'Time_error'
                    await translate_msg.delete()
                    time_error = await dp.send_message(chat_id, "Время вышло)=")
                    await asyncio.sleep(1)
                    await time_error.delete()
            if i == 9:
                right_answer = work_data[chat_id]['right_answer']
                await dp.send_message(chat_id, f"Вот и поработали) У тебя {right_answer} из 10 правильных. Ты заработал {right_answer*10}💎",reply_markup=kb_income)
                send_data(chat_id, 'balance', get_data(chat_id, 'balance') + right_answer*10)
                del work_data[chat_id] 
    if code == 2:
        await dp.send_message(chat_id, "Пока вакансий таксистом нет)=")
    if code == 3:
        await dp.send_message(chat_id, "Пока вакансий сетевым админестратором нет)=")

async def Переводчик(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    situaded = work_data[chat_id]['situaded']
    work_data[chat_id]['answer'] = 1
    await callback_query.message.delete()

    if code == situaded :
        right = await dp.send_message(chat_id, "Правильно(+10💎)")
        await asyncio.sleep(1)
        await right.delete()
        work_data[chat_id]['right_answer'] += 1
    else:
        error = await dp.send_message(chat_id, "Неправильно")
        await asyncio.sleep(1)
        await error.delete()    

def reg_handlers_school(bot: Dispatcher):
    bot.register_callback_query_handler(Работы,lambda c: c.data and c.data.startswith('job_'))
    bot.register_callback_query_handler(Переводчик,lambda c: c.data and c.data.startswith('translate_'))



