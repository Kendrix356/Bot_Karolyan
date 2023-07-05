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

#@bot.message_handler()
async def Главное_меню(message, state: FSMContext):
    #Главное меню
    for i in range(len(ids_users)): 
        if message.from_user.id == ids_users[i] and get_data(message.from_user.id,'status') != 3:
            
            if message.text == "Заработак💰":
                await dp.send_message(message.from_user.id, 'Есть много способов зароботка:)',reply_markup=kb_income)
            
            elif message.text == "Казино🤑":
                await dp.send_message(message.from_user.id, 'Ставь ставку!\nЕсли ты хочешь отменить, просто напиши "отмена"', reply_markup=types.ReplyKeyboardRemove())
                await Form_cas.stavka.set()

            elif message.text == "Карта🃏":
                photo = open('map.png', 'rb')
                await dp.send_photo(message.chat.id, photo=photo, caption="Вот карта)")
                item1 = types.InlineKeyboardButton("Другая облать", callback_data='map_go1')
                item2 = types.InlineKeyboardButton("Столица", callback_data='go_dif4')
                item3 = types.InlineKeyboardButton("Город(жилье)", callback_data='map_go3')
                markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)
                mes = await dp.send_message(message.from_user.id, 'Ты находишься в <i>' + str(get_data(message.from_user.id, 'location')) + '</i>'+ '\nЕсли хочешь переехать нажми кнопку)', reply_markup=markup)

            elif message.text == "Школа🏫":
                item1 = InlineKeyboardButton("Расписание", callback_data='keyboaord_school1')
                item2 = InlineKeyboardButton("Ответы на музыку", callback_data='keyboaord_school2')
                markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
                await dp.send_message(message.from_user.id, 'Выбирай что нужно тебе:', reply_markup=markup)

            elif message.text == "Пожертвование🙏":
                await dp.send_message(message.from_user.id, 'Если ты хочешь пожертвовать немного денег на развитие бота, нажми сюда -> https://clck.ru/32WjF3')    

            elif message.text == "Магазин🏪":
                location = get_data(message.from_user.id, 'location')
                if location == 'Столица':
                    item1 = InlineKeyboardButton("Машины", callback_data='mag_4')
                    item2 = InlineKeyboardButton("Квартиры, дома", callback_data='mag_5')
                    markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
                elif location == 'Верхний город' or location == 'Нижний город': 
                    pass
                else:
                    item1 = InlineKeyboardButton("Бизнес", callback_data='mag_1')
                    item2 = InlineKeyboardButton("Бустеры", callback_data='mag_2')
                    item3 = InlineKeyboardButton("Коллекционные предметы", callback_data='mag_3')
                    markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)
                mes = await dp.send_message(message.from_user.id, 'Выбери категорию:',reply_markup=markup)

            elif message.text == "Моя биография👶":
                item1 = InlineKeyboardButton("Как зовут?🧐", callback_data='keyboaord2_button1')
                item2 = InlineKeyboardButton("Сколкьо денег?💸", callback_data='keyboaord2_button2')
                item3 = InlineKeyboardButton("Сколько использовал(а) промокодов?🎫", callback_data='keyboaord2_button3')
                item4 = KeyboardButton("Мой инвентарь🚗", callback_data='keyboaord2_button4')
                markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3, item4)
                await dp.send_message(message.from_user.id, 'Выбирете что нужно(=', reply_markup=markup)

            elif message.text == "Топ😎":
                user = []
                balance = []
                conn = sqlite3.connect("us.db", check_same_thread=False)
                cursor = conn.cursor()
                cursor.execute("""select balance FROM users""")
                moneys = cursor.fetchall()
                moneys.sort(reverse=True)
                conn.commit()
                cursor.close()

                for i in range(3):
                    conn = sqlite3.connect("us.db", check_same_thread=False)
                    cursor = conn.cursor()
                    try: cursor.execute("""select * FROM users where balance = ?""", moneys[i])
                    except:
                        await dp.send_message(message.from_user.id, 'Что-то пошло не так ¯\_(ツ)_/¯')
                        break
                    data = cursor.fetchall()
                    for row in data:
                        user.append(row[2])
                        balance.append(row[3])
                    conn.commit()
                    cursor.close()

                await dp.send_message(message.from_user.id,
                fmt.text(
                fmt.text("💵Самые самые богатые на планете"),
                fmt.text("1 - ",user[0],"(",balance[0],")"),
                fmt.text("2 - ",user[1],"(",balance[1],")"),
                fmt.text("3 - ",user[2],"(",balance[2],")"),
                sep="\n"
                ), parse_mode="HTML"
                )

            elif message.text == "Заявка модератору🗎":
                await dp.send_message(message.from_user.id, 'Напиши причину того, что тебе не понравилось в поведении админов🤔.',reply_markup=types.ReplyKeyboardRemove())
                await Form_moder.moder.set()
            
            elif message.text == "Работы💼":
                item1 = types.InlineKeyboardButton("Переводчик", callback_data='job_1')
                item2 = types.InlineKeyboardButton("Таксист", callback_data='job_2')
                item3 = types.InlineKeyboardButton("Сетевой Администратор", callback_data='job_3')
                markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)                                                                                                                                                                                                                                                                                                                 
                works_mes = await dp.send_message(message.from_user.id, 'Кем будешь работать?', reply_markup=markup)
                async with state.proxy() as data:
                    data['works_mes'] = works_mes
                    data['working'] = 1
            elif message.text == "Бизнес":
                have_buizness = get_data(message.from_user.id, 'buizness')
                if have_buizness == 0:
                    item1 = types.InlineKeyboardButton("Как работает бизнес?", callback_data='pod_2')
                    markup = InlineKeyboardMarkup(row_width=2).add(item1)
                    await dp.send_message(message.from_user.id, "Ты пока не имешь бизнеса, если ты хочешь купить, тебе в магазин",reply_markup=markup)
                else:
                    if buizness[have_buizness] == 'Автомат с едой': 
                        photo_b = open('buizness1.jpg', 'rb')
                    elif buizness[have_buizness] == 'Кофейня': 
                        photo_b = open('buizness2.jpg', 'rb')
                    item1 = types.InlineKeyboardButton("Подробнее", callback_data='pod_1')
                    item2 = types.InlineKeyboardButton("Как работает бизнес", callback_data='pod_2')
                    markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
                    await dp.send_photo(message.from_user.id, photo=photo_b, caption=f"У тебя есть бизнес <b>{buizness[have_buizness]}</b>", reply_markup=markup)
            elif message.text == "Промокоды🎂":
                await dp.send_message(message.from_user.id,'Напиши промоко_дик')
                await Form_promo.promo.set()

            elif message.text == "Загс":
                await dp.send_message(message.from_user.id, 'Ты еще не дорос!(:')

            elif 'Нах' in message.text or 'нах' in message.text:
                await dp.send_message(message.from_user.id, 'только после тебя')
            elif 'Баранина' in message.text or 'баранина' in message.text:
                await dp.send_message(message.from_user.id, 'сама такая')
            elif 'Шлюх' in message.text or 'шлюх' in message.text:
                await dp.send_message(message.from_user.id, 'чел..')
            elif 'Тупая' in message.text or 'тупая' in message.text:
                await dp.send_message(message.from_user.id, 'жалко тебя')
            elif 'Блядь' in message.text or 'блядь' in message.text:
                await dp.send_message(message.from_user.id, 'ладно.')
            elif 'Ебанутая' in message.text or 'ебанутая' in message.text:
                await dp.send_message(message.from_user.id, 'сама такая')
            elif 'Мудила' in message.text or 'мудила' in message.text:
                await dp.send_message(message.from_user.id, 'кто бы говорил')
            elif 'Пизд' in message.text or 'пизд' in message.text:
                await dp.send_message(message.from_user.id, 'твоя')
            elif 'Сука' in message.text or 'сука' in message.text:
                await dp.send_message(message.from_user.id, 'ты.')

            elif 'Люблю' in message.text or 'люблю' in message.text:
                await dp.send_message(message.from_user.id, 'Я тебя тоже❤')
                if get_data(message.from_user.id, 'love') == 1:
                    await dp.send_message(message.from_user.id, 'Держи денежку')
                    await dp.send_message(message.from_user.id, '(получено 100💎)')
                    send_data(message.from_user.id, 'love', 0)
                    send_data(message.from_user.id, 'balance', get_data(message.from_user.id, 'balance')+100)

            elif message.text == "Назад":
                location = get_data(message.from_user.id, 'location')
                if location == 'Столица': await dp.send_message(message.from_user.id, "Ок", reply_markup=kb_menu_st)
                elif location == 'Верхний город' or location == 'Нижний город': await dp.send_message(message.from_user.id, "Ок", reply_markup=kb_menu_gr)
                else: await dp.send_message(message.from_user.id, "Ок", reply_markup=kb_menu)

            elif message.text == "Завершить":
                async with state.proxy() as data:
                    data['working'] = 0
                location = get_data(message.from_user.id, 'location')
                if location == 'Столица': await dp.send_message(message.from_user.id, "Ок", reply_markup=kb_menu_st)
                elif location == 'Верхний город' or location == 'Нижний город': await dp.send_message(message.from_user.id, "Ок", reply_markup=kb_menu_gr)
                else: await dp.send_message(message.from_user.id, "Ок", reply_markup=kb_menu)    

            else:
                await dp.send_message(message.from_user.id, 'Переведи на ботоводский, я не поняла😢')

def reg_handlers_menu(bot: Dispatcher):
    bot.register_message_handler(Главное_меню)
