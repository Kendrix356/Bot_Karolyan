from constants import *
from objects import *
from Function import *
from fsm import *

from create_bot import dp,bot

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import Dispatcher

async def Магазин(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    await callback_query.message.delete()

    if code == 1:
        item1 = InlineKeyboardButton('Автомат с едой', callback_data='vesh_01')
        item2 = InlineKeyboardButton('Кофейня', callback_data='vesh_02')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
    # elif code == 2:
    #     item1 = InlineKeyboardButton('Скидка 20% на такси', callback_data='vesh_03')
    #     item2 = InlineKeyboardButton('Увелечение работы бизнеса на 25%', callback_data='vesh_04')
    #     markup = InlineKeyboardMarkup(row_width=1).add(item1, item2)
    elif code == 3:
        item1 = InlineKeyboardButton('Трофей(1750)', callback_data='vesh_05')
        item2 = InlineKeyboardButton('Трофей(3000)', callback_data='vesh_06')
        item3 = InlineKeyboardButton('Трофей Михаила', callback_data='vesh_07')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)
    elif code == 4:
        item1 = InlineKeyboardButton('Дешевый класс', callback_data='class_m_1')
        item2 = InlineKeyboardButton('Средний класс', callback_data='class_m_2')
        item3 = InlineKeyboardButton('Дорогой класс', callback_data='class_m_3')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)     
    await dp.send_message(chat_id, 'Выбери что нужно:', reply_markup=markup)

async def Распределение_классов(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    await callback_query.message.delete()

    if code == 1:
        item1 = InlineKeyboardButton('Lada Granta', callback_data='vesh_08')
        item2 = InlineKeyboardButton('Lada Vesta', callback_data='vesh_09')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
    elif code == 2:
        item1 = InlineKeyboardButton('BMV 5', callback_data='vesh_10')
        item2 = InlineKeyboardButton('Mercedes W222', callback_data='vesh_11')
        item3 = InlineKeyboardButton('Audi A4', callback_data='vesh_12')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)
    elif code == 3:
        item1 = InlineKeyboardButton('Tesla Model X', callback_data='vesh_13')
        markup = InlineKeyboardMarkup(row_width=2).add(item1)
    await dp.send_message(chat_id, 'Выбери что нужно:', reply_markup=markup)

async def Магазин_описание(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[5:7]
    if code.isdigit():
        code = int(code)

    await callback_query.message.delete()

    #Бизнесы
    if code == 1:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_01')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        await dp.send_message(chat_id, 'Бизнес: <b>Автомат с едой</b> \nХарактеристеки:\nЗаработок в час: 20\nЗаработок в день: 480\nЗаработок после окупа в день: 288\nЦена: 10.000', reply_markup=markup)
    elif code == 2:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_02')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        await dp.send_message(chat_id, 'Бизнес: <b>Кофейня</b> \nХарактеристеки:\nЗаработок в час: 35\nЗаработок в день: 840\nЗаработок после окупа в день: 504\nЦена: 22.000', reply_markup=markup)
    
    # #Бустеры
    # elif code == 3:
    #     item1 = InlineKeyboardButton('Купить', callback_data='kup_03')
    #     item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
    #     markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
    #     await dp.send_message(chat_id, 'Бустер: <b>Скидка 20% на такси</b> \nХарактеристеки:\nДействует: 1 час\nЦена: 300\n<b>ВНИМАНИЕ, бустер действует до начала след. часа</b>', reply_markup=markup) 
    # elif code == 4:
    #     item1 = InlineKeyboardButton('Купить', callback_data='kup_04')
    #     item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
    #     markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
    #     await dp.send_message(chat_id, 'Бустер: <b>Увелечение работы бизнеса на 25%</b> \nХарактеристеки:\nДействует: 24 часа\nЦена: 450\n<b>ВНИМАНИЕ, бустер действует до начала след. часа (после 23-ого)</b>', reply_markup=markup) 
    
    #Трофеи
    elif code == 5:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_05')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        await dp.send_message(chat_id, 'Трофей: <b>Трофей(1750)</b> \nХарактеристеки:\nУровень: 1750\nЦена: 2.000', reply_markup=markup)
    elif code == 6:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_06')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        await dp.send_message(chat_id, 'Трофей: <b>Трофей(3000)</b> \nХарактеристеки:\nУровень: 3000\nЦена: 3.250', reply_markup=markup)
    elif code == 7:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_07')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        await dp.send_message(chat_id, 'Трофей: <b>Трофей Михаила</b> \nХарактеристеки:\nПроисходжение: Миша\nЦена: 12.750', reply_markup=markup)
    
    #Машины
    elif code == 8:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_08')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        await dp.send_message(chat_id, 'Машина: <b>Lada Granta</b> \nХарактеристеки:\nМощность: 90 лс.\nРасход: 8л.(100км)\nМакс. Скорость: 175 км/ч\nЦена: 130.000', reply_markup=markup)
    elif code == 9:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_09')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        await dp.send_message(chat_id, 'Машина: <b>Lada Vesta</b> \nХарактеристеки:\nМощность: 106 лс.\nРасход: 9л.(100км)\nМакс. Скорость: 190 км/ч\nЦена: 175.000', reply_markup=markup)
    elif code == 10:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_10')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        await dp.send_message(chat_id, 'Машина: <b>BMV 5</b> \nХарактеристеки:\nМощность: 450 лс.\nРасход: 10л.(100км)\nМакс. Скорость: 240 км/ч\nЦена: 420.000', reply_markup=markup)
    elif code == 11:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_11')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        await dp.send_message(chat_id, 'Машина: <b>Mercedes W222</b> \nХарактеристеки:\nМощность: 450 лс.\nРасход: 12л.(100км)\nМакс. Скорость: 230 км/ч\nЦена: 365.000', reply_markup=markup)
    elif code == 12:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_12')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        await dp.send_message(chat_id, 'Машина: <b>Audi A4</b> \nХарактеристеки:\nМощность: 400 лс.\nРасход: 11л.(100км)\nМакс. Скорость: 250 км/ч\nЦена: 400.000', reply_markup=markup)
    elif code == 13:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_13')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_0')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        await dp.send_message(chat_id, 'Машина: <b>Tesla Model S Plaid</b> \nХарактеристеки:\nМощность: 1 034 лс.\nРасход: 1 разрядка (600км)\nМакс. Скорость: 322 км/ч\nЦена: 850.000', reply_markup=markup)
    
    #Дома и квартиры (Столица)
    elif code == 14:
        item1 = InlineKeyboardButton('Купить', callback_data='kup_14')
        item2 = InlineKeyboardButton('Отмена', callback_data='kup_00')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
        await dp.send_message(chat_id, 'Жилье: <b>Квартира(Столица)</b> \nХарактеристеки:\nКачество: 11/10.\nЦена: 1.800.000', reply_markup=markup)

async def Магазин_продажа(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[4:6]
    if code.isdigit():
        code = int(code)
    
    await callback_query.message.delete()
    
    balance = get_data(chat_id, 'balance')
    element = 0
    error = 0
    pay = 0
    
    if code == 1:
        pay = 10000
        if balance >= pay: send_data(chat_id, 'buizness', 1)
        else: await dp.send_message(chat_id, 'Нету деняг)=')
    elif code == 2:
        pay = 22000
        if balance >= pay: send_data(chat_id, 'buizness', 2)
        else: await dp.send_message(chat_id, 'Нету деняг)=')
    # elif code == 3:
    #     pay = 300
    #     send_data(chat_id, 'buster', 1)
    
    # elif code == 4:
    #     pay = 450
    #     send_data(chat_id, 'buster', 224)
    elif code in range(5, 14):
        prices = [2000, 3250, 12750, 130000, 175000, 420000, 365000, 400000, 850000]
        element = code-4
        pay = prices[element-1]
    elif code == 14:
        pay = 1800000
        element = 10
    else:
        await dp.send_message(chat_id, 'Ок')
    
    if balance >= pay:
        if element != 0:
            try: inventory_add(chat_id, element)
            except:
                error = 1
                await dp.send_message(chat_id, 'У тебя полный инвентарь')
    else:
        pay = 0
        await dp.send_message(chat_id, 'Нету деняг)=')
    
    if code != 0 and error != 1 and pay != 0:
        await dp.send_message(chat_id, f'Куплено (-{pay})')
        send_data(chat_id, 'balance', get_data(chat_id, 'balance') - pay)


def reg_handlers_magazin(bot: Dispatcher):
    bot.register_callback_query_handler(Магазин,lambda c: c.data and c.data.startswith('mag_'))
    bot.register_callback_query_handler(Распределение_классов,lambda c: c.data and c.data.startswith('class_m_'))
    bot.register_callback_query_handler(Магазин_описание,lambda c: c.data and c.data.startswith('vesh_'))
    bot.register_callback_query_handler(Магазин_продажа,lambda c: c.data and c.data.startswith('kup_'))