from constants import *
from objects import *
from Function import *
from fsm import *

from create_bot import dp,bot

from aiogram import types
from aiogram.dispatcher import Dispatcher

async def Биография(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    if code == 1: await dp.send_message(chat_id, "Тебя зовут - " + str(get_data(chat_id, 'name')))
    elif code == 2: await dp.send_message(chat_id, "У тебя " + str(get_data(chat_id, 'balance')) + "💎")
    elif code == 3:
        val = get_data(chat_id,'promo1') + get_data(chat_id,'promo2') + get_data(chat_id,'promo3')
        await dp.send_message(chat_id, "Ты использовал " + str(val) + " промокод/а/ов")
    else:
        inventory = get_data(chat_id,'inventory').split('.')
        for i in range(8):
            if inventory[i] == '0':
                if i == 0:
                    await dp.send_message(chat_id, 'У тебя пустой инвентарь)')
                break
            else:
                if i == 0: await dp.send_message(chat_id, 'Вот твой инвентарь:')
                await dp.send_message(chat_id, f'Элемент {i}: {things_mag[int(inventory[i])]}')
            
def reg_handlers_biography(bot: Dispatcher):
    bot.register_callback_query_handler(Биография,lambda c: c.data and c.data.startswith('keyboaord2_button'))