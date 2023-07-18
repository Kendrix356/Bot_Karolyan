from constants import *
from objects import *
from Function import *
from fsm import *

from create_bot import dp,bot

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import Dispatcher, FSMContext

async def Админ_панель(message: types.Message):
    chat_id = message.from_user.id
    for i in range(len(ids_admines)): 
        if chat_id == ids_admines[i]:
            await dp.send_message(chat_id,'Вы вошли в админ панель.\nСообщение о входе отправлено.', reply_markup=types.ReplyKeyboardRemove())
            await dp.send_message(group_id, "@" + message.from_user.username + ": " + "Вошел в админ панель.")
            item1_admin_panel = InlineKeyboardButton("Добавить пользователя в бота", callback_data='admin_btn1')
            item2_admin_panel = InlineKeyboardButton("Удалить пользователя из бота", callback_data='admin_btn2')
            item3_admin_panel = InlineKeyboardButton("Написать от имени бота", callback_data='admin_btn3')
            kb_admin_panel = InlineKeyboardMarkup(row_width=2).add(item1_admin_panel, item2_admin_panel, item3_admin_panel)
            await dp.send_message(chat_id,'Выбирай', reply_markup=kb_admin_panel)
        else: await dp.send_message(chat_id, "Ты не админ😡!")
            
async def Админ_панель_инлайн(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    if code == 1: await Form_id_add.id.set()
    if code == 2: await Form_id_delete.id.set()
    if code == 3: await Form_send_mes.id.set()
    await dp.send_message(chat_id,'Напишите id пользователя.')

async def Добавление_нового_пользователя(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id
    async with state.proxy() as data:
        data['id'] = message.text
        ids_users.append(data['id'])
        await dp.send_message(chat_id, "Ок.")

async def Удаление_пользователя(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id
    async with state.proxy() as data:
        data['id'] = message.text
        try:
            ids_users.remove(data['id'])
            await dp.send_message(chat_id, "Ок.")
        except: await dp.send_message(chat_id, "Что-то пошло не так.")

async def Отправка_сообщения1(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id
    async with state.proxy() as data:
        data['id'] = message.text
        await Form_send_mes.mes.set()
        await dp.send_message(chat_id, "Теперь напиши сообщение.")

async def Отправка_сообщения2(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id
    async with state.proxy() as data:
        data['mes'] = message.text
        try: await dp.send_message(data['id'], 'Новое сообщение\n<i>' + data['mes'] + '</i> - от Админа')
        except: await dp.send_message(chat_id, "Ошибка. Проверьте id и сообщение.")
    await state.finish()

def reg_handlers_admin_panel(bot: Dispatcher):
    bot.register_message_handler(Админ_панель,commands=['admin_panel'])
    bot.register_callback_query_handler(Админ_панель_инлайн,lambda c: c.data and c.data.startswith('admin_btn'))
    bot.register_message_handler(Добавление_нового_пользователя,state=Form_id_add.id)
    bot.register_message_handler(Удаление_пользователя,state=Form_id_delete.id)
    bot.register_message_handler(Отправка_сообщения1,state=Form_send_mes.id)
    bot.register_message_handler(Отправка_сообщения2,state=Form_send_mes.mes)
