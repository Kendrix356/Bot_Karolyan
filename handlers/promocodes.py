from constants import *
from objects import *
from Function import *
from fsm import *

from create_bot import dp,bot

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import Dispatcher

async def Промокоды(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id
    async with state.proxy() as data:
        data['promo'] = message.text
        if data['promo'] == "eRop1n":
            if get_data(chat_id, 'promo1') == 0:
                await dp.send_message(chat_id, "Поздравляю ты выйграл 100💎")
                send_data(chat_id, 'balance', get_data(chat_id, 'balance') + 100)
                send_data(chat_id, 'promo1', 1)
            else: await dp.send_message(chat_id, "Ты уже использовал такой промокод")  
        elif data['promo'] == 'Suzanne_well_done':
            if get_data(message.from_user.id, 'promo2') == 0 and message.from_user.id != 1143067536:
                await dp.send_message(chat_id, "Поздравляю ты выйграл 150💎.А также ты поддержал Сюзану денежкой, так как это реферальный код))")
                send_data(chat_id, 'balance', get_data(chat_id, 'balance') + 150)
                send_data(1143067536, 'balance', get_data(1143067536, 'balance') + 150)
                send_data(chat_id, 'promo2', 1)
            elif message.from_user.id == 1143067536: await dp.send_message(chat_id, "Это же твоя рефералка, схитрить хотела?") 
            else: await dp.send_message(chat_id, "Ты уже использовал такой промокод")
        elif data['promo'] == 'urarelis':
            if get_data(message.from_user.id, 'promo3') == 0:
                await dp.send_message(chat_id, "Поздравляю ты выйграл 250💎")
                send_data(chat_id, 'balance', get_data(chat_id, 'balance') + 250)
                send_data(chat_id, 'promo3', 1)
            else: await dp.send_message(chat_id, "Ты уже использовал такой промокод")
        else: await dp.send_message(chat_id, "Такого промокода нету😢")
    await state.finish()

def reg_handlers_promocodes(bot: Dispatcher):
    bot.register_message_handler(Промокоды,state=Form_promo.promo)
