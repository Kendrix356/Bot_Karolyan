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

async def Ставка(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['stavka'] = message.text
        if data['stavka'].isdigit():
            if get_data(message.chat.id, 'balance') >= int(data['stavka']):
                item3 = types.InlineKeyboardButton("Отмена", callback_data='cas_4')
                if get_data(message.from_user.id, 'location') != 'Столица':
                    item1 = types.InlineKeyboardButton("Автомат777", callback_data='cas_1')
                    item2 = types.InlineKeyboardButton("Монетка", callback_data='cas_2')
                    markup = InlineKeyboardMarkup(row_width=1).add(item1, item2, item3)
                else:
                    item1 = types.InlineKeyboardButton("Башня", callback_data='cas_3')
                    markup = InlineKeyboardMarkup(row_width=1).add(item1, item3)
                await dp.send_message(message.chat.id, 'Ставка: '+ data['stavka'] + '\nВо что играть будем?',reply_markup=markup)
                await state.finish()
            else:
                location = get_data(message.from_user.id, 'location')
                if location == 'Столица': await dp.send_message(message.from_user.id, 'Нету деняг)=', reply_markup=kb_menu_st)
                elif location == 'Верхний город' or location == 'Нижний город': await dp.send_message(message.from_user.id, 'Нету деняг)=', reply_markup=kb_menu_gr)
                else: await dp.send_message(message.from_user.id, 'Нету деняг)=', reply_markup=kb_menu)
                await state.finish()
        elif data['stavka'] == "отмена" or data['stavka'] == "Отмена":
            location = get_data(message.from_user.id, 'location')
            if location == 'Столица': await dp.send_message(message.from_user.id, "Окей", reply_markup=kb_menu_st)
            elif location == 'Верхний город' or location == 'Нижний город': await dp.send_message(message.from_user.id, "Окей", reply_markup=kb_menu_gr)
            else: await dp.send_message(message.from_user.id, "Окей", reply_markup=kb_menu)
            await state.finish()
        else:
            await dp.send_message(message.chat.id, "Это должна быть цифра")
            await Form_cas.stavka.set()

async def Игра_казино(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    await callback_query.message.delete()
    bal = get_data(callback_query.from_user.id,'balance')

    async with state.proxy() as data:
        if code == 1:
            await dp.send_message(callback_query.from_user.id, 'Поехали🍀')
            choice = random.choices(nums, k=3)
            bal = bal - int(data['stavka'])
            if choice == ['1', '1', '1']:
                bal += int(data['stavka']) * 2
            elif choice == ['2', '2', '2']:
                bal += int(data['stavka']) * 3
            elif choice == ['3', '3', '3']:
                bal += int(data['stavka']) * 5
            elif choice == ['0', '0', '0']:
                bal += int(data['stavka']) * 1
            mes = await dp.send_message(callback_query.from_user.id, 'Барабан:')
            time.sleep(1)
            await mes.edit_text('Барабан: ' + choice[0])
            time.sleep(1)
            await mes.edit_text('Барабан: ' + choice[0] + ' '+ choice[1])
            time.sleep(1)
            await mes.edit_text('Барабан: ' + choice[0] + ' ' + choice[1] + ' ' + choice[2])
        elif code == 2:
            await dp.send_message(callback_query.from_user.id, 'Поехали🍀\nВаша сторона - решка')
            time.sleep(1)
            random_value = random.choice([True, False])
            if random_value == True: 
                await dp.send_message(callback_query.from_user.id, 'Выпала решка\nПобеда')
                bal = bal + 2 * int(data['stavka'])
                time.sleep(1)
            else:
                await dp.send_message(callback_query.from_user.id, 'Выпал орел\nПроигрыш')
                bal = bal - int(data['stavka'])
                time.sleep(1)
        elif code == 3:
            array = [['✅'] * 3 for _ in range(5)]
            for row in array: row[random.randint(0, 2)] = '💣'
            await dp.send_message(callback_query.from_user.id, 'Поехали🍀')
            item1 = types.InlineKeyboardButton("1", callback_data='bash_1')
            item2 = types.InlineKeyboardButton("2", callback_data='bash_2')
            item3 = types.InlineKeyboardButton("3", callback_data='bash_3')
            markup = InlineKeyboardMarkup(row_width=3).add(item1, item2, item3)
            mes_bash = await dp.send_message(callback_query.from_user.id,
                fmt.text(
                fmt.text("Башня:"),
                fmt.text("5.0x - ",array[4]),
                fmt.text("4.0x - ",array[3]),
                fmt.text("3.0x - ",array[2]),
                fmt.text("2.0x - ",array[1]),
                fmt.text("1.5x - ",array[0]),
                sep="\n"
                ), parse_mode="HTML", reply_markup=markup
                )
            



        if code == 4:
            location = get_data(callback_query.from_user.id, 'location')
            if location == 'Столица': await dp.send_message(callback_query.from_user.id, "Окей", reply_markup=kb_menu_st)
            elif location == 'Верхний город' or location == 'Нижний город': await dp.send_message(callback_query.from_user.id, "Окей", reply_markup=kb_menu_gr)
            else: await dp.send_message(callback_query.from_user.id, "Окей", reply_markup=kb_menu)
        else:
            location = get_data(callback_query.from_user.id, 'location')
            if location == 'Столица': await dp.send_message(callback_query.from_user.id, 'Ваш баланс ' + str(bal) + '💎', reply_markup=kb_menu_st)
            elif location == 'Верхний город' or location == 'Нижний город': await dp.send_message(callback_query.from_user.id, 'Ваш баланс ' + str(bal) + '💎', reply_markup=kb_menu_gr)
            else: await dp.send_message(callback_query.from_user.id, 'Ваш баланс ' + str(bal) + '💎', reply_markup=kb_menu)
            send_data(callback_query.from_user.id, 'balance', bal)
    await state.finish()

def reg_handlers_casino(bot: Dispatcher):
    bot.register_message_handler(Ставка,state=Form_cas.stavka)
    bot.register_callback_query_handler(Игра_казино,lambda c: c.data and c.data.startswith('cas_'))