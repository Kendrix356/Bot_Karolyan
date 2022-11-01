from constants import *
from objects import *
from Function import *
from fsm import *


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

storage = MemoryStorage()
dp = Bot(token="5095654656:AAGGKQ21-440lk-YNvvtgu2z2wjTAie572Y", parse_mode=types.ParseMode.HTML)
bot = Dispatcher(dp, storage=storage)
thread = Thread(target=run)
thread.start()

@bot.message_handler(commands=['start'])
async def Приветствие(message: types.Message):
    for i in range(len(ids_users)): 
        if message.from_user.id == ids_users[i]:
            try:
                if get_data(message.from_user.id,'register') == 1:
                    await dp.send_message(message.from_user.id, "Привет. Я - бот для группы 7-ого 'Б' класса.Я буду всегда помогать тебе. Но это не правда😁", reply_markup=kb_menu)
                    await Form_name.name.set()
                    await dp.send_message(message.from_user.id,'Напиши пожалалуйста свое реально имя, а то штраф 150(=')
                    register = 0
                    send_data(message.from_user.id, 'register', register)
                else:
                    await dp.send_message(message.from_user.id, "Привет)", reply_markup=kb_menu)
            except:
                reg(message.from_user.id)
                
@bot.message_handler(commands=['admin_panel'])
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
            
#Админ панель
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('admin_btn'))
async def Админ_панель(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    if code == 1:
        await Form_name.id.set()
        await dp.send_message(callback_query.from_user.id,'Напишите id пользователя.')
    if code == 2:
        pass
    if code == 3:
        pass
    
@bot.message_handler(state=Form_send_mes.id)
async def Регистрация(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        send_data(message.from_user.id, 'name', remove_char(md.bold(data['name'])))
    await state.finish()
    await dp.send_message(message.from_user.id, "Спасибки)")

@bot.message_handler(state=Form_name.name)
async def Регистрация(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        send_data(message.from_user.id, 'name', remove_char(md.bold(data['name'])))
    await state.finish()
    await dp.send_message(message.from_user.id, "Спасибки)")

@bot.message_handler()
async def Главное_меню(message):
    #Главное меню
    for i in range(len(ids_users)): 
        if message.from_user.id == ids_users[i]:

            if message.text == "Заработак💰":
                await dp.send_message(message.from_user.id, 'Есть много способов зароботка:)',reply_markup=kb_income)
            
            elif message.text == "Казино🤑":
                await dp.send_message(message.from_user.id, 'Во что играть будем?',reply_markup=kb_casino)
            
            elif message.text == "Карта🃏":
                await dp.send_message(message.from_user.id, 'Бетка')

            elif message.text == "Школа🏫":
                item1 = InlineKeyboardButton("Расписание", callback_data='keyboaord_school1')
                item2 = InlineKeyboardButton("Ответы на музыку", callback_data='keyboaord_school2')
                markup = InlineKeyboardMarkup(row_width=2).add(item1, item2)
                await dp.send_message(message.from_user.id, 'Выбирай что нужно тебе:', reply_markup=markup)

            elif message.text == "Пожертвование🙏":
                await dp.send_message(message.from_user.id, 'Если ты хочешь пожертвовать немного денег на развитие бота, нажми сюда -> https://clck.ru/32WjF3')    

            elif message.text == "Мое Магазин🏪":
                await dp.send_message(message.from_user.id, 'Прайс лист:')

            elif message.text == "Моя биография👶":
                item1 = InlineKeyboardButton("Как зовут?🧐", callback_data='keyboaord2_button1')
                item2 = InlineKeyboardButton("Сколкьо денег?💸", callback_data='keyboaord2_button2')
                item3 = InlineKeyboardButton("Сколько использовал(а) промокодов?🎫", callback_data='keyboaord2_button3')
                item4 = InlineKeyboardButton("Склько крипты?💹", callback_data='keyboaord2_button4')
                item5 = KeyboardButton("Мое имущество🚗", callback_data='keyboaord2_button5')
                markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3, item4, item5)
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
                    cursor.execute("""select * FROM users where balance = ?""", moneys[i])
                    data = cursor.fetchall()
                    print(data)
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
                await dp.send_message(message.from_user.id, 'Напиши причину того, что тебе не понравилось в поведении админов🤔.')
                await Form_moder.moder.set()
            
            elif message.text == "Работы💼":
                item1 = types.InlineKeyboardButton("Переводчик", callback_data='job_1')
                item2 = types.InlineKeyboardButton("Таксист", callback_data='job_2')
                item3 = types.InlineKeyboardButton("Сетевой Администратор", callback_data='job_3')
                markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)
                await dp.send_message(message.from_user.id, 'Кем будешь работать?', reply_markup=markup)

            elif message.text == "Промокоды🎂":
                await dp.send_message(message.from_user.id,'Напиши промоко_дик')
                await Form_promo.promo.set()

            elif message.text == "КриптоБиржа💹":
                await dp.send_message(message.from_user.id, "Курс:", reply_markup=kb_cripto)
                global LeshaCoin
                global SmeshiСoin
                global GrafiCoin
                global Blin_ya_ftoroy_coin
                await message.answer(
                fmt.text(
                fmt.text("ЛешаКоин: ",LeshaCoin),
                fmt.text("СмешиКоин: ",SmeshiСoin),
                fmt.text("ГрафиКоин: ",GrafiCoin),
                fmt.text("Блин я второй коин: ",Blin_ya_ftoroy_coin),
                sep="\n"
                ), parse_mode="HTML"
                )

            elif message.text == "Автомат🎰":
                await dp.send_message(message.from_user.id, 'Ставь ставку!')
                await Form_cas777.stavka.set()

            elif message.text == "Краш📈":
                await dp.send_message(message.from_user.id, 'Ставь ставку!')
                #await Form_crash.other.set()
                
            elif message.text == "Купить валюту":
                item1 = types.InlineKeyboardButton("ЛешаКоин", callback_data='min1')
                item2 = types.InlineKeyboardButton("СмешиКоин", callback_data='min2')
                item3 = types.InlineKeyboardButton("ГрафиКоин", callback_data='min3')
                item4 = types.InlineKeyboardButton("Блин я второй Коин", callback_data='min4')
                markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3, item4)
                await dp.send_message(message.from_user.id, 'Выбирай:', reply_markup=markup)

            elif message.text == "Продать валюту":
                item1 = types.InlineKeyboardButton("ЛешаКоин", callback_data='pls1')
                item2 = types.InlineKeyboardButton("СмешиКоин", callback_data='pls2')
                item3 = types.InlineKeyboardButton("ГрафиКоин", callback_data='pls3')
                item4 = types.InlineKeyboardButton("Блин я второй Коин", callback_data='pls4')
                markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3, item4)
                await dp.send_message(message.from_user.id, 'Выбирай:', reply_markup=markup)

            elif message.text == "Майнинг":
                pass

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
                await dp.send_message(message.from_user.id, 'Ок', reply_markup=kb_menu)

            elif message.text == "Завершить":
                global working
                working = 0
                await dp.send_message(message.from_user.id, 'Ок', reply_markup=kb_menu)    

            else:
                await dp.send_message(message.from_user.id, 'Переведи на ботоводский, я не поняла😢')

#Автомат777
@bot.message_handler(state=Form_cas777.stavka)
async def Автомат777(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        bal = get_data(message.chat.id, 'balance')
        data['other'] = message.text
        if bal >= int(data['other']):
            await dp.send_message(message.chat.id, 'Поехали🍀')
            choice = random.choices(nums, k=3)
            bal = bal - int(data['other'])
            if choice == ['1', '1', '1']:
                await dp.send_message(message.chat.id, 'Барабан:')
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[0])
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[1])
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[2])
                time.sleep(1)
                bal = bal + int(data['other']) * 1.5
                print('+',bal,'💎')
            elif choice == ['2', '2', '2']:
                await dp.send_message(message.chat.id, 'Барабан:')
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[0])
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[1])
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[2])
                time.sleep(1)
                bal = bal + int(data['other']) * 2
                print('+',bal,'💎')
            elif choice == ['3', '3', '3']:
                await dp.send_message(message.chat.id, 'Барабан:')
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[0])
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[1])
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[2])
                time.sleep(1)
                bal = bal + int(data['other']) * 3
                print('+',bal,'💎')
            elif choice == ['0', '0', '0']:
                await dp.send_message(message.chat.id, 'Барабан:')
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[0])
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[1])
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[2])
                time.sleep(1)
                bal = bal + int(data['other']) * 1
                print('+',bal,'💎')
            else:
                await dp.send_message(message.chat.id, 'Барабан:')
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[0])
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[1])
                time.sleep(1)
                await dp.send_message(message.chat.id, choice[2])
                time.sleep(1)
            await dp.send_message(message.chat.id, 'Ваш баланс ' + str(bal) + '💎')
            send_data(message.chat.id, 'balance', bal)
        else:
            await dp.send_message(message.chat.id, 'Нету деняг)=')
    await state.finish()

#Биография
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('keyboaord2_button'))
async def Биография(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    if code == 1:
        await dp.send_message(callback_query.from_user.id, "Тебя зовут - " + str(get_data(callback_query.from_user.id, 'name')))
    if code == 2:
        await dp.send_message(callback_query.from_user.id, "У тебя " + str(get_data(callback_query.from_user.id, 'balance')) + "💎")
    if code == 3:
        val = get_data(callback_query.from_user.id,'promo1') + get_data(callback_query.from_user.id,'promo2')
        await dp.send_message(callback_query.from_user.id, "Ты использовал " + str(val) + " промокод/а/ов")
    if code == 4:
        await dp.send_message(callback_query.from_user.id, "Вот сколько у тебя крипты:")
        await dp.send_message(callback_query.from_user.id,
            fmt.text(
            fmt.text("ЛешаКоин: ", get_data(callback_query.from_user.id,'leshaСoin')),
            fmt.text("СмешиКоин: ", get_data(callback_query.from_user.id,'smeshiСoin')),
            fmt.text("ГрафиКоин: ", get_data(callback_query.from_user.id,'grafiCoin')),
            fmt.text("Блин я второй коин: ", get_data(callback_query.from_user.id,'b_ya_v_Coin')),
            sep="\n"
            ), parse_mode="HTML"
            )
    if code == 5:
        await dp.send_message(callback_query.from_user.id, 'Какое же имущество у тебя есть!',reply_markup=kb_have)

#Школа
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('keyboaord_school'))
async def Биография(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    if code == 1:
        try:
            await dp.send_message(callback_query.from_user.id, Raspis[datetime.datetime.today().weekday()])
        except:
            await dp.send_message(callback_query.from_user.id, 'Сегодня выходной!')
    if code == 2:
        pass

#Заявка модера
@bot.message_handler(state=Form_moder.moder)
async def Заявка_модеру(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        await dp.send_message(group_id, "@" + message.from_user.username + ": " + data['text'])
        await dp.send_message(message.from_user.id, 'Все отправила. Жди ответа😁')
    await state.finish()

#Промокоды
@bot.message_handler(state=Form_promo.promo)
async def Промокоды(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        global bal
        data['promo'] = message.text

        if data['promo'] == 'eRop1n':
            if get_data(message.from_user.id, 'promo1') == 1:
                await dp.send_message(message.chat.id, 'Поздравляю ты выйграл 100💎')
                bal = get_data(message.chat.id, 'balance') + 100
                send_data(message.chat.id, 'balance', bal)
                send_data(message.chat.id, 'promo1', 0)
            else:  
                await dp.send_message(message.chat.id, 'Ты уже использовал такой промокод')  

        elif data['promo'] == 'Suzanne_well_done':
            if get_data(message.from_user.id, 'promo2') == 1 and message.from_user.id != 1143067536:
                await dp.send_message(message.chat.id, 'Поздравляю ты выйграл 150💎.А также ты поддержал Сюзану денежкой, так как это реферальный код))')
                bal = get_data(message.chat.id, 'balance') + 150
                bal_s = get_data(1143067536, 'balance') + 150

                send_data(message.chat.id, 'balance', bal)
                send_data(1143067536, 'balance', bal_s)
                send_data(message.chat.id, 'promo2', 0)
            else:
                if message.from_user.id == 1143067536:
                    await dp.send_message(message.chat.id, 'Это же твоя рефералка, схитрить хотела?') 
                else:
                    await dp.send_message(message.chat.id, 'Ты уже использовал такой промокод')  
        else:
            await dp.send_message(message.chat.id, 'Такого промокода нету😢')
    await state.finish()

#Криптобаржа (покупка)
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('min'))
async def Криптобиржа_продажа(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code2 = callback_query.data[-1]
    if code2.isdigit():
        code2 = int(code2)

    bal = get_data(callback_query.from_user.id, 'balance')

    if code2 == 1:
        if bal >= LeshaCoin:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Потрачено {round(LeshaCoin)}')
            send_data(callback_query.from_user.id, 'balance', round(bal - LeshaCoin))
            send_data(callback_query.from_user.id, 'leshaСoin', (get_data(callback_query.from_user.id, 'leshaСoin')) + 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно средств❌')
    if code2 == 2:
        if bal >= SmeshiСoin:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Потрачено {round(SmeshiСoin)}')
            send_data(callback_query.from_user.id, 'balance', round(bal - SmeshiСoin))
            send_data(callback_query.from_user.id, 'SmeshiСoin', (get_data(callback_query.from_user.id, 'SmeshiСoin')) + 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно средств❌')
    if code2 == 3:
        if bal >= GrafiCoin:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Потрачено {round(GrafiCoin)}')
            send_data(callback_query.from_user.id, 'balance', round(bal - GrafiCoin))
            send_data(callback_query.from_user.id, 'grafiCoin', (get_data(callback_query.from_user.id, 'grafiCoin')) + 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно средств❌')
    if code2 == 4:
        if bal >= Blin_ya_ftoroy_coin:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Потрачено {round(Blin_ya_ftoroy_coin)}')
            send_data(callback_query.from_user.id, 'balance', round(bal - Blin_ya_ftoroy_coin))
            send_data(callback_query.from_user.id, 'b_ya_v_Coin', (get_data(callback_query.from_user.id, 'b_ya_v_Coin')) + 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно средств❌')

#Криптобиржа (продажа)
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('pls'))
async def Криптобиржа_купить(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code2 = callback_query.data[-1]
    if code2.isdigit():
        code2 = int(code2)

    bal = get_data(callback_query.from_user.id, 'balance')

    if code2 == 1:
        if get_data(callback_query.from_user.id, 'leshaCoin') >= 1:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Получено {round(LeshaCoin - LeshaCoin*0.1)}')
            send_data(callback_query.from_user.id, 'balance', bal+round(LeshaCoin - LeshaCoin*0.1))
            send_data(callback_query.from_user.id, 'leshaCoin', (get_data(callback_query.from_user.id, 'leshaCoin')) - 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно крипты❌')
    if code2 == 2:
        if get_data(callback_query.from_user.id, 'SmeshiСoin') >= 1:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Получено {round(SmeshiСoin - SmeshiСoin*0.1)}')
            send_data(callback_query.from_user.id, 'balance', bal+round(SmeshiСoin - SmeshiСoin*0.1))
            send_data(callback_query.from_user.id, 'SmeshiСoin', (get_data(callback_query.from_user.id, 'SmeshiСoin')) - 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно крипты❌')
    if code2 == 3:
        if get_data(callback_query.from_user.id, 'grafiCoin') >= 1:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Получено {round(GrafiCoin - GrafiCoin*0.1)}')
            send_data(callback_query.from_user.id, 'balance', bal+round(GrafiCoin - GrafiCoin*0.1))
            send_data(callback_query.from_user.id, 'grafiCoin', (get_data(callback_query.from_user.id, 'grafiCoin')) - 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно крипты❌')
    if code2 == 4:
        if get_data(callback_query.from_user.id, 'b_ya_v_Coin') >= 1:
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Получено {round(Blin_ya_ftoroy_coin - Blin_ya_ftoroy_coin*0.1)}')
            send_data(callback_query.from_user.id, 'balance', bal+round(Blin_ya_ftoroy_coin - Blin_ya_ftoroy_coin*0.1))
            send_data(callback_query.from_user.id, 'b_ya_v_Coin', (get_data(callback_query.from_user.id, 'b_ya_v_Coin')) - 1)
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно крипты❌')

#Работы
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('job_'))
async def Работы(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    global situaded
    global answer
    global answers
    global translate_msg
    global right_answer
    global working

    if code == 1:
        working = 1
        answer = 0
        msg1 = await dp.send_message(callback_query.from_user.id, f"Ты выбрал работу - <i>Переводчик</i>")
        time.sleep(1)
        msg2 = await dp.send_message(callback_query.from_user.id, "Ее задача заключается в том, что нужно уметь быcтро переводить текст с английского на русский.")
        time.sleep(3)
        msg3 = await dp.send_message(callback_query.from_user.id, "Через 5 секунд начнется твоя работа, готовься!")
        time.sleep(5)
        await msg1.delete()
        await msg2.delete()
        await msg3.delete()
        await dp.send_message(callback_query.from_user.id, "Начинаем!",reply_markup=kb_stop_work)

        for i in range(10):
            if working == 1:
                answer = 0
                answers+=1
                situaded, correct_word, markup = generate_translate()
                translate_msg = await dp.send_message(callback_query.from_user.id, f"Выбери верный перевод слова '{words_english[correct_word]}' ", reply_markup=markup)
                await asyncio.sleep(5)
                if answer == 0 and working == 1:
                    await translate_msg.delete()
                    time_error = await dp.send_message(callback_query.from_user.id, "Время вышло)=")
                    await asyncio.sleep(1)
                    await time_error.delete()
                    if answers == 10 and working == 1:
                        await dp.send_message(callback_query.from_user.id, f"Вот и поработали) У тебя {right_answer} из 10 правильных. Ты заработал {right_answer*10}💎")
    if code == 2:
        pass
    if code == 3:
        pass

@bot.callback_query_handler(lambda c: c.data and c.data.startswith('translate_'))
async def Переводчик(callback_query: types.CallbackQuery):

    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    global situaded
    global answer
    global answers
    global translate_msg
    global right_answer

    if code == situaded :
        answer = 1
        right_answer+=1
        await translate_msg.delete()
        complete = await dp.send_message(callback_query.from_user.id, 'Правильно(+10💎)')
        await asyncio.sleep(1)
        await complete.delete() 
        if answers == 10:
            await dp.send_message(callback_query.from_user.id, f"Вот и поработали) У тебя {right_answer} из 10 правильных. Ты заработал {right_answer*10}💎")
            send_data(callback_query.from_user.id, 'balance', get_data(callback_query.from_user.id, 'balance') + right_answer*10)
    else:
        answer = 1
        await translate_msg.delete()
        error = await dp.send_message(callback_query.from_user.id, 'Неправильно')
        await asyncio.sleep(1)
        await error.delete() 
        if answers == 10:
            await dp.send_message(callback_query.from_user.id, f"Вот и поработали) У тебя {right_answer} из 10 правильных. Ты заработал {right_answer*10}💎")
            send_data(callback_query.from_user.id, 'balance', get_data(callback_query.from_user.id, 'balance') + right_answer*10)

if __name__ == '__main__':
    executor.start_polling(bot,skip_updates=True)