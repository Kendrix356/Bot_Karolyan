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


game_data = {}

async def Ставка(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['stavka'] = message.text
        if data['stavka'].isdigit():
            if get_data(message.chat.id, 'balance') >= int(data['stavka']):
                cansel = types.InlineKeyboardButton("Отмена", callback_data='cas_4')
                if get_data(message.chat.id, 'location') != 'Столица':
                    item1 = types.InlineKeyboardButton("Автомат777", callback_data='cas_1')
                    item2 = types.InlineKeyboardButton("Монетка", callback_data='cas_2')
                    markup = InlineKeyboardMarkup(row_width=1).add(item1, item2, cansel)
                else:
                    item1 = types.InlineKeyboardButton("Башня", callback_data='cas_3')
                    markup = InlineKeyboardMarkup(row_width=1).add(item1, cansel)
                await dp.send_message(message.chat.id, 'Ставка: '+ data['stavka'] + '\nВо что играть будем?',reply_markup=markup)
                game_data[message.chat.id] = {
                    'stavka': int(data['stavka']),
                    'game_board': 0,
                    'current_level': 0
                    }
                await state.finish()
            else:
                await backmarkup("нету деняг)=", message.chat.id)
                await state.finish()
        elif data['stavka'] == "отмена" or data['stavka'] == "Отмена":
            await backmarkup("окей", message.chat.id)
            await state.finish()
        else:
            await dp.send_message(message.chat.id, "Это должна быть цифра")
            await Form_cas.stavka.set()

async def Игра_казино(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    await callback_query.message.delete()
    bal = get_data(callback_query.from_user.id,'balance')
    stavka = int(game_data[callback_query.from_user.id]['stavka'])
    send_data(callback_query.from_user.id, "balance",bal-stavka)
    send_data(callback_query.from_user.id, "status",3)

    if code == 1:
        await dp.send_message(callback_query.from_user.id, 'Поехали🍀')
        choice = random.choices(nums, k=3)
        if choice == ['1', '1', '1']:
            bal += stavka * 10
        elif choice == ['2', '2', '2']:
            bal += stavka * 20
        elif choice == ['3', '3', '3']:
            bal += stavka * 30
        elif choice == ['0', '0', '0']:
            bal += stavka * 5
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
        random_value = random.randrange(1,100)
        if random_value <= 40: 
            await dp.send_message(callback_query.from_user.id, 'Выпала решка\nПобеда')
            bal =+ 2*stavka
            time.sleep(1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Выпал орел\nПроигрыш')
            time.sleep(1)
    elif code == 3:
        await dp.send_message(callback_query.from_user.id, 'Поехали🍀')
        game_data[callback_query.from_user.id]['game_board'] = create_game_board()
        game_data[callback_query.from_user.id]['current_level'] = 0
        await show_game_board(callback_query.from_user.id)
    if code == 4: await backmarkup("окей", callback_query.from_user.id) 
    elif code != 3:
        await backmarkup(f"Ваш баланс {str(bal)}💎", callback_query.from_user.id)
        send_data(callback_query.from_user.id, 'balance', bal)
        send_data(callback_query.from_user.id, "status",1)
        del game_data[callback_query.from_user.id]

async def Башня(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    chat_id = callback_query.message.chat.id
    game_board = game_data[chat_id]['game_board']
    current_level = game_data[chat_id]['current_level']
    bal = get_data(callback_query.from_user.id,'balance')

    if code != 4:
        game_data[chat_id]['current_level'] += 1
        if game_board[current_level][code-1] == "💣":
            await dp.send_message(chat_id, f'Вы проиграли.')
            time.sleep(1)
            await callback_query.message.delete()
            await backmarkup(f"Ваш баланс {str(bal)}💎", chat_id)
            send_data(chat_id, "status",1)
            del game_data[chat_id]
        else:
            if current_level == 4:
                plus = game_data[chat_id]['stavka']*current_level
                await dp.send_message(chat_id, f'Поздравляю! Вы прошли все слои. Вы победили.(+{plus})')
                send_data(chat_id,"balance",bal+plus)
                time.sleep(1)
                await callback_query.message.delete()
                await backmarkup(f"Ваш баланс {str(bal+plus)}💎", chat_id)
                send_data(chat_id, "status",1)
                del game_data[chat_id]
            else:
                await show_game_board(chat_id)
    elif game_data[chat_id]['current_level'] != 0:
        plus = game_data[chat_id]['stavka']*current_level
        await dp.send_message(chat_id, f'Поздравляю! Вы победили.(+{plus})')
        send_data(chat_id,"balance",bal+plus)
        time.sleep(1)
        await callback_query.message.delete()
        await backmarkup(f"Ваш баланс {str(bal+plus)}💎", chat_id)
        send_data(chat_id, "status",1)
        del game_data[chat_id]
    else:
        await dp.send_message(chat_id, 'Нельзя забрать, не прошев ни один уровень!')

# Функция для отображения игрового поля
async def show_game_board(chat_id):
    game_board = game_data[chat_id]['game_board']
    current_level = game_data[chat_id]['current_level']
    board_message = display_game_board(game_board, current_level)

    item1 = types.InlineKeyboardButton("1", callback_data='bash_1')
    item2 = types.InlineKeyboardButton("2", callback_data='bash_2')
    item3 = types.InlineKeyboardButton("3", callback_data='bash_3')
    item4 = types.InlineKeyboardButton("Забрать", callback_data='bash_4')
    keyboard = InlineKeyboardMarkup(row_width=3).add(item1, item2, item3, item4)
    if current_level != 0:
            try:
                await dp.edit_message_text(chat_id=chat_id, message_id=game_data[chat_id]['message_id'],
                                            text=board_message, reply_markup=keyboard)
            except: pass
    else:
        ms = await dp.send_message(chat_id=chat_id, text=board_message, reply_markup=keyboard)
        game_data[chat_id]['message_id'] = ms["message_id"]

def reg_handlers_casino(bot: Dispatcher):
    bot.register_message_handler(Ставка,state=Form_cas.stavka)
    bot.register_callback_query_handler(Игра_казино,lambda c: c.data and c.data.startswith('cas_'))
    bot.register_callback_query_handler(Башня,lambda c: c.data and c.data.startswith('bash_'))