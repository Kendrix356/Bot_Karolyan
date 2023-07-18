from constants import *
from objects import *
from Function import *
from fsm import *

from create_bot import dp,bot

import aiogram.utils.markdown as md
from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher

async def Приветствие(message: types.Message):
    chat_id = message.from_user.id
    for i in range(len(ids_users)): 
        if chat_id == ids_users[i]:
            try:
                if get_data(chat_id,'register') == 0: await backmarkup(chat_id,"Привет!")
            except:
                reg(chat_id)
                await dp.send_message(chat_id, "Привет. Я - бот для группы 8-ого 'Б' класса. Я буду всегда помогать тебе. Но это не правда😁")
                await dp.send_message(chat_id,"Напиши пожалалуйста свое реально имя, а то штраф 150(=")
                send_data(chat_id, 'register', 0)
                await Form_name.name.set()
                
async def Регистрация(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id
    async with state.proxy() as data:
        data['name'] = message.text
        send_data(chat_id, 'name', remove_char(md.bold(data['name'])))
    await state.finish()
    await backmarkup(chat_id,"Спасибки)")

def reg_handlers_start(bot: Dispatcher):
    bot.register_message_handler(Приветствие,commands=['start'])
    bot.register_message_handler(Регистрация,state=Form_name.name)