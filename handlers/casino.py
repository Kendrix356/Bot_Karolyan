from constants import *
from objects import *
from Function import *
from fsm import *

from create_bot import dp,bot

import asyncio
import random
from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext, Dispatcher

game_data = {}

async def Ставка(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    async with state.proxy() as data:
        data['stavka'] = message.text
        if data['stavka'].isdigit():
            if get_data(chat_id, 'balance') >= int(data['stavka']):
                cansel = types.InlineKeyboardButton("Отмена", callback_data='cas_4')
                if get_data(chat_id, 'location') != 'Столица':
                    item1 = types.InlineKeyboardButton("Автомат777", callback_data='cas_1')
                    item2 = types.InlineKeyboardButton("Монетка", callback_data='cas_2')
                    markup = InlineKeyboardMarkup(row_width=1).add(item1, item2, cansel)
                else:
                    item1 = types.InlineKeyboardButton("Башня", callback_data='cas_3')
                    markup = InlineKeyboardMarkup(row_width=1).add(item1, cansel)
                await dp.send_message(chat_id, 'Ставка: '+ data['stavka'] + '\nВо что играть будем?',reply_markup=markup)
                game_data[chat_id] = {
                    'stavka': int(data['stavka']),
                    'game_board': 0,
                    'current_level': 0
                    }
                await state.finish()
            else:
                await backmarkup(chat_id, "нету деняг)=")
                await state.finish()
        elif data['stavka'] == "отмена" or data['stavka'] == "Отмена":
            await backmarkup(chat_id, "окей")
            await state.finish()
        else:
            await dp.send_message(chat_id, "Это должна быть цифра")
            await Form_cas.stavka.set()

async def Игра_казино(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    await callback_query.message.delete()
    bal = get_data(chat_id,'balance')
    stavka = int(game_data[chat_id]['stavka'])
    send_data(chat_id, "status",3)

    if code == 1:
        await dp.send_message(chat_id, 'Поехали🍀')
        choice = random.choices(nums, k=3)
        if choice == ['1', '1', '1'] or \
           choice == ['2', '2', '2'] or \
           choice == ['3', '3', '3']: bal += stavka * 5
        mes = await dp.send_message(chat_id, 'Барабан:')
        choiceF = custom_sort(choice)
        await asyncio.sleep(1)
        await mes.edit_text('Барабан: ' + choiceF[0])
        await asyncio.sleep(1)
        await mes.edit_text('Барабан: ' + choiceF[0] + ' '+ choiceF[1])
        await asyncio.sleep(1)
        await mes.edit_text('Барабан: ' + choiceF[0] + ' ' + choiceF[1] + ' ' + choiceF[2])
    elif code == 2:
        await dp.send_message(chat_id, 'Поехали🍀\nВаша сторона - решка')
        await asyncio.sleep(1)
        random_value = random.randrange(1,100)
        if random_value <= 45: 
            await dp.send_message(chat_id, 'Выпала решка\nПобеда')
            bal += 2*stavka
            await asyncio.sleep(1)
        else:
            await dp.send_message(chat_id, 'Выпал орел\nПроигрыш')
            await asyncio.sleep(1)
    elif code == 3:
        await dp.send_message(chat_id, 'Поехали🍀')
        game_data[chat_id]['game_board'] = create_game_board()
        game_data[chat_id]['current_level'] = 0
        send_data(chat_id, "balance",bal-stavka)
        await show_game_board(chat_id)
    if code == 4: 
        await backmarkup(chat_id, "окей") 
        send_data(chat_id, "status",1)
    elif code != 3:
        await backmarkup(chat_id, f"Ваш баланс {str(bal-stavka)}💎")
        send_data(chat_id, "balance",bal-stavka)
        send_data(chat_id, "status",1)
        del game_data[chat_id]

async def Башня(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    game_board = game_data[chat_id]['game_board']
    current_level = game_data[chat_id]['current_level']
    bal = get_data(callback_query.from_user.id,'balance')

    if code != 4:
        game_data[chat_id]['current_level'] += 1
        if game_board[current_level][code-1] == "💣":
            await show_game_board(chat_id,1)
            await dp.send_message(chat_id, f'Вы проиграли.')
            await asyncio.sleep(2)
            await callback_query.message.delete()
            await backmarkup(chat_id, f"Ваш баланс {str(bal)}💎")
            send_data(chat_id, "status",1)
            del game_data[chat_id]
        else:
            if current_level == 4:
                await show_game_board(chat_id,1)
                plus = game_data[chat_id]['stavka']*(current_level+1)
                await dp.send_message(chat_id, f'Поздравляю! Вы прошли все слои. Вы победили.(+{plus})')
                send_data(chat_id,"balance",bal+plus)
                await asyncio.sleep(2)
                await callback_query.message.delete()
                await backmarkup(chat_id, f"Ваш баланс {str(bal+plus)}💎")
                send_data(chat_id, "status",1)
                del game_data[chat_id]
            else:
                await show_game_board(chat_id)
    elif game_data[chat_id]['current_level'] != 0:
        plus = game_data[chat_id]['stavka']*current_level
        await dp.send_message(chat_id, f'Поздравляю! Вы победили.(+{plus})')
        send_data(chat_id,"balance",bal+plus)
        await asyncio.sleep(2)
        await callback_query.message.delete()
        await backmarkup(chat_id, f"Ваш баланс {str(bal+plus)}💎")
        send_data(chat_id, "status",1)
        del game_data[chat_id]
    else:
        await dp.send_message(chat_id, 'Нельзя забрать, не прошев ни один уровень!')

# Функция для отображения игрового поля
async def show_game_board(chat_id, last = 0):
    game_board = game_data[chat_id]['game_board']
    current_level = game_data[chat_id]['current_level']
    board_message = display_game_board(game_board, current_level)

    item1 = types.InlineKeyboardButton("1", callback_data='bash_1')
    item2 = types.InlineKeyboardButton("2", callback_data='bash_2')
    item3 = types.InlineKeyboardButton("3", callback_data='bash_3')
    item4 = types.InlineKeyboardButton("Забрать", callback_data='bash_4')
    keyboard = InlineKeyboardMarkup(row_width=3).add(item1, item2, item3, item4)

    if current_level != 0:
            if last == 0:
                await dp.edit_message_text(chat_id=chat_id, message_id=game_data[chat_id]['message_id'],
                                            text=board_message, reply_markup=keyboard)
            else: await dp.edit_message_text(chat_id=chat_id, message_id=game_data[chat_id]['message_id'],
                                            text=board_message, reply_markup=None)
    else:
        ms = await dp.send_message(chat_id=chat_id, text=board_message, reply_markup=keyboard)
        game_data[chat_id]['message_id'] = ms["message_id"]

def reg_handlers_casino(bot: Dispatcher):
    bot.register_message_handler(Ставка,state=Form_cas.stavka)
    bot.register_callback_query_handler(Игра_казино,lambda c: c.data and c.data.startswith('cas_'))
    bot.register_callback_query_handler(Башня,lambda c: c.data and c.data.startswith('bash_'))