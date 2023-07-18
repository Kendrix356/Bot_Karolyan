from constants import *
from objects import *
from Function import *
from fsm import *

from create_bot import dp,bot

from aiogram import types
from aiogram.dispatcher import Dispatcher

async def Расписание(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    if code == 1:
        try: await dp.send_message(chat_id, Raspis[datetime.datetime.today().weekday()])
        except: await dp.send_message(chat_id, "Сегодня выходной!")
    if code == 2:
        await dp.send_message(chat_id, "Я пока не знаю ответов на музыку")

def reg_handlers_school(bot: Dispatcher):
    bot.register_callback_query_handler(Расписание,lambda c: c.data and c.data.startswith('keyboaord_school'))