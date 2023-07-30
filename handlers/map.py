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

async def Поехать_в_область(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    await callback_query.message.delete()

    if code == 1:
        item1 = types.InlineKeyboardButton("7А", callback_data='go_dif0')
        item2 = types.InlineKeyboardButton("7Б", callback_data='go_dif1')
        item3 = types.InlineKeyboardButton("7В", callback_data='go_dif2')
        item4 = types.InlineKeyboardButton("7Г", callback_data='go_dif3')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3, item4)
        await dp.send_message(chat_id, "В какую облать?", reply_markup=markup)
    elif code == 3:
        await dp.send_message(chat_id, "Путь туда завален камнями) Строители уже работают над этим.")


async def Ехать_или_нет(callback_query: types.CallbackQuery, state: FSMContext):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    await callback_query.message.delete()

    item1 = types.InlineKeyboardButton("Поехали", callback_data='poex1')
    item2 = types.InlineKeyboardButton("Отмена", callback_data='poex2')
    markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)

    k = random.uniform(1,1.5)
    pay = round(150 * k)
    kuda = code

    if get_data(chat_id, 'location') != kuda_mes[kuda]:
        if get_data(chat_id,'balance') >= pay:
            if get_data(chat_id, "buster") == 1: 
                text = '\u0336'.join(str(pay))
                pay = round(pay * 0.75)
                await dp.send_message(chat_id, f"Стоимость поездки = {text} {str(pay)}💎", reply_markup=markup)
            else: await dp.send_message(chat_id, f"Стоимость поездки = {str(pay)}💎", reply_markup=markup)
            async with state.proxy() as data:
                data['kuda'] = kuda
                data['pay'] = pay
        else:
            if get_data(chat_id, 'location') == 'Столица': 
                await dp.send_message(chat_id, "Так как у тебя не хватает денег, а ты находишся в столице, где нельзя зарабатывать деньги, поездка для тебе будет бесплатна")
                await dp.send_message(chat_id, "Стоимость поездки = 0💎", reply_markup=markup)
                async with state.proxy() as data:
                    data['kuda'] = kuda
                    data['pay'] = 0
            else: await dp.send_message(chat_id, "У тебя нет денег)=")
    else:
        await dp.send_message(chat_id, "Зачем тебе ехать туда, если ты уже там???")

async def Едим(callback_query: types.CallbackQuery, state: FSMContext):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    async with state.proxy() as data:
        kuda = data['kuda']
        pay = data['pay']
    await state.finish()

    await callback_query.message.delete()

    if code == 1:
        wait_sec = random.randint(10,30)
        wait = await dp.send_message(chat_id, f"Через {wait_sec} секунд ты приедешь(=",reply_markup=types.ReplyKeyboardRemove())
        status_pred = get_data(chat_id, 'status')
        send_data(chat_id, 'status', 3)
        await asyncio.sleep(wait_sec)
        await wait.delete()
        send_data(chat_id, 'balance', get_data(chat_id,'balance')-pay)
        send_data(chat_id, 'location', kuda_mes[kuda])
        send_data(chat_id, 'status', status_pred)
        await backmarkup(chat_id, f"Ты приехал) -{pay}💎")
    elif code == 2:
        await dp.send_message(chat_id, "Ок)")

def reg_handlers_map(bot: Dispatcher):
    bot.register_callback_query_handler(Поехать_в_область,lambda c: c.data and c.data.startswith('map_go'))
    bot.register_callback_query_handler(Ехать_или_нет,lambda c: c.data and c.data.startswith('go_dif'))
    bot.register_callback_query_handler(Едим,lambda c: c.data and c.data.startswith('poex'))