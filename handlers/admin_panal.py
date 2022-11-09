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


#@bot.message_handler(commands=['admin_panel'])
async def Админ_панель(message: types.Message):
    for i in range(len(ids_admines)): 
        if message.from_user.id == ids_admines[i]:
            await dp.send_message(message.from_user.id,'Вы вошли в админ панель.\nСообщение о входе отправлено.', reply_markup=types.ReplyKeyboardRemove())
            await dp.send_message(group_id, "@" + message.from_user.username + ": " + "Вошел в админ панель.")
            item1_admin_panel = InlineKeyboardButton("Добавить пользователя в бота", callback_data='admin_btn1')
            item2_admin_panel = InlineKeyboardButton("Удалить пользователя из бота", callback_data='admin_btn2')
            item3_admin_panel = InlineKeyboardButton("Написать от имени бота", callback_data='admin_btn3')
            kb_admin_panel = InlineKeyboardMarkup(row_width=2).add(item1_admin_panel, item2_admin_panel, item3_admin_panel)
            await dp.send_message(message.from_user.id,'Выбирай', reply_markup=kb_admin_panel)
        else: 
            await dp.send_message(message.from_user.id, "Ты не админ😡!")
            
#@bot.callback_query_handler(lambda c: c.data and c.data.startswith('admin_btn'))
async def Админ_панель_инлайн(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    if code == 1:
        await Form_id_add.id.set()
    if code == 2:
        await Form_id_delete.id.set()
    if code == 3:
        await Form_send_mes.id.set()
    await dp.send_message(callback_query.from_user.id,'Напишите id пользователя.')
    
#@bot.message_handler(state=Form_id_add.id)
async def Добавление_нового_пользователя(message: types.Message, state: FSMContext):

    global ids_users

    async with state.proxy() as data:
        data['id'] = message.text
        ids_users.append(data['id'])
        await dp.send_message(message.from_user.id, "Ок.")
    await state.finish()

#@bot.message_handler(state=Form_id_delete.id)
async def Удаление_пользователя(message: types.Message, state: FSMContext):

    global ids_users

    async with state.proxy() as data:
        data['id'] = message.text
        try:
            ids_users.remove(data['id'])
            await dp.send_message(message.from_user.id, "Ок.")
        except:
            await dp.send_message(message.from_user.id, "Что-то пошло не так.")
    await state.finish()

#@bot.message_handler(state=Form_send_mes.id)
async def Отправка_сообщения1(message: types.Message, state: FSMContext):

    global id

    async with state.proxy() as data:
        data['id'] = message.text

        id = data['id']
        await Form_send_mes.mes.set()
        await dp.send_message(message.from_user.id, "Теперь напиши сообщение.")

#@bot.message_handler(state=Form_send_mes.mes)
async def Отправка_сообщения2(message: types.Message, state: FSMContext):

    global id

    async with state.proxy() as data:
        data['mes'] = message.text
        try:
            await dp.send_message(id, 'Новое сообщение\n<i>' + data['mes'] + '</i> - от Админа')
        except:
            await dp.send_message(message.from_user.id, "Ошибка. Проверьте id и сообщение.")
    await state.finish()

def reg_handlers_admin_panel(bot: Dispatcher):
    bot.register_message_handler(Админ_панель,commands=['admin_panel'])
    bot.register_callback_query_handler(Админ_панель_инлайн,lambda c: c.data and c.data.startswith('admin_btn'))
    bot.register_message_handler(Добавление_нового_пользователя,state=Form_id_add.id)
    bot.register_message_handler(Удаление_пользователя,state=Form_id_delete.id)
    bot.register_message_handler(Отправка_сообщения1,state=Form_send_mes.id)
    bot.register_message_handler(Отправка_сообщения2,state=Form_send_mes.mes)
