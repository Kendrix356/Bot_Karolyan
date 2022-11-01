import random
import time
from threading import Thread
import sqlite3
import schedule, time
import aiogram.utils.markdown as fmt
import aiogram.utils.markdown as md
from aiogram import Bot, types
from aiogram.types import ParseMode
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import init
storage = MemoryStorage()
dp = Bot(token="5095654656:AAGGKQ21-440lk-YNvvtgu2z2wjTAie572Y", parse_mode=types.ParseMode.HTML)
bot = Dispatcher(dp, storage=storage)

item1 = KeyboardButton("Казик🤑")
item2 = KeyboardButton("Смешняфка🙃")
item3 = KeyboardButton("Рандом🎲")
item4 = KeyboardButton("Заявка модератору🗎")
item5 = KeyboardButton("Промокоды🎂")
item6 = KeyboardButton("КриптоБиржа💹")
item7 = KeyboardButton("Моя биография🤓")
item8 = KeyboardButton("Легенды")

item1_1 = KeyboardButton("Купить валюту")
item2_1 = KeyboardButton("Продать валюту")
item3_1 = KeyboardButton("Майнинг")
item4_1 = KeyboardButton("Назад")

item1_2 = KeyboardButton("Автомат_777")
item2_2 = KeyboardButton("Краш")
item1 = InlineKeyboardButton("Забрать!", callback_data='keyboaordcas_button1')
markup3 = InlineKeyboardMarkup(row_width=2).add(item1)

group_id = -1001708790022
nums = ['0', '0', '0', '0', '1', '1', '1', '2','2', '3']

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(item1, item2, item3, item4, item5, item6, item7, item8)
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb1.add(item1_1, item2_1, item3_1, item4_1)
greet_kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb2.add(item1_2, item2_2)

promo1 = 0
promo2 = 0

LeshaKoin = 400
SmeshiKoin = 400
GrafiCoin = 400
Blin_ya_ftoroy_coin = 400

LeshaKoin_im = 0
SmeshiKoin_im = 0
GrafiCoin_im = 0
Blin_ya_ftoroy_coin_im = 0

class Form(StatesGroup):
    name = State() 
class Form1(StatesGroup):
    promo = State()  
class Form2(StatesGroup):
    other = State()  
class Form3(StatesGroup):
    text = State()
class Form4(StatesGroup):
    other = State()

def is_even(number):
    return number % 0.1 == 0
    
def geeks():
    global LeshaKoin
    global SmeshiKoin
    global GrafiCoin
    global Blin_ya_ftoroy_coin
    print("ЛешаКоин ")
    if random.choice(['+','-']) == '+':
        LeshaKoin = LeshaKoin + random.uniform(0, 10)
        print(LeshaKoin)
    else:
        LeshaKoin = LeshaKoin - random.uniform(0, 10)
        print(LeshaKoin)
    print("СмешиКоин ")
    if random.choice(['+','-']) == '+':
        SmeshiKoin = SmeshiKoin + random.uniform(0, 10)
        print(SmeshiKoin)
    else:
        SmeshiKoin = SmeshiKoin - random.uniform(0, 10)
        print(SmeshiKoin)
    print("ГрафиКоин ")
    if random.choice(['+','-']) == '+':
        GrafiCoin = GrafiCoin + random.uniform(0, 10)
        print(GrafiCoin)
    else:
        GrafiCoin = GrafiCoin - random.uniform(0, 10)
        print(GrafiCoin)
    print("Блин я второй Коин ")
    if random.choice(['+','-']) == '+':
        Blin_ya_ftoroy_coin = Blin_ya_ftoroy_coin + random.uniform(0, 10)
        print(Blin_ya_ftoroy_coin)
    else:
        Blin_ya_ftoroy_coin = Blin_ya_ftoroy_coin - random.uniform(0, 10)
        print(Blin_ya_ftoroy_coin)
    print(" ")

def run():
    schedule.every(5).seconds.do(geeks) 
    while True: 
        schedule.run_pending() 
        time.sleep(1)

def remove_char(s):
    result = s[1 : -1]
    return result

thread = Thread(target=run)
thread.start()

@bot.message_handler(commands=['start', 'help'])
async def send_welome(message: types.Message):
    if message.from_user.id == 1278533043 or message.from_user.id == 1089443949 or message.from_user.id == 1728744256 or message.from_user.id == 1316809851 or message.from_user.id == 1121484143 or message.from_user.id == 1814437620 or message.from_user.id == 2047177073 or message.from_user.id == 925209982 or message.from_user.id == 627015995 or message.from_user.id == 1427309639 or message.from_user.id == 1116058402 or message.from_user.id == 1457183761 or message.from_user.id == 1158996363 or message.from_user.id == 1452562218 or message.from_user.id == 1130425276 or message.from_user.id == 1782177637 or message.from_user.id == 1770002348 or message.from_user.id == 901433127 or message.from_user.id == 5151456253 or message.from_user.id == 1521177605 or message.from_user.id == 5005528361 or message.from_user.id == 1143067536 or message.from_user.id == 1330356014:
        conn = sqlite3.connect("us.db", check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO `users` (`user_id`) VALUES (?)", (message.from_user.id,))
        users = cursor.execute("SELECT * FROM `users`")
        print(users.fetchall())
        er = """select * FROM users where user_id = ?"""
        cursor.execute(er,(message.from_user.id,))
        money = cursor.fetchall()
        for row in money:
            global bal
            bal = row[3]
        conn.commit()
        cursor.close() 
        await dp.send_message(message.from_user.id, "Привет. Я - бот для группы 7-ого 'Б' класса.Я буду всегда помогать тебе. Но это не правда😁", reply_markup=greet_kb)
        await Form.name.set()
        await dp.send_message(message.from_user.id,'Напиши пожалалуйста свое реально имя, а иначе будешь забанен(=')
 
@bot.message_handler()
async def button(message):
    if message.from_user.id == 1278533043 or message.from_user.id == 1089443949 or message.from_user.id == 1728744256 or message.from_user.id == 1316809851 or message.from_user.id == 1121484143 or message.from_user.id == 1814437620 or message.from_user.id == 2047177073 or message.from_user.id == 925209982 or message.from_user.id == 627015995 or message.from_user.id == 1427309639 or message.from_user.id == 1116058402 or message.from_user.id == 1457183761 or message.from_user.id == 1158996363 or message.from_user.id == 1452562218 or message.from_user.id == 1130425276 or message.from_user.id == 1782177637 or message.from_user.id == 1770002348 or message.from_user.id == 901433127 or message.from_user.id == 5151456253 or message.from_user.id == 1521177605 or message.from_user.id == 5005528361 or message.from_user.id == 1143067536 or message.from_user.id == 1330356014:
        global bal
        global love
        global real_name_1
        global real_name_2
        global real_name_3
        if message.text == "Казик🤑":
            await dp.send_message(message.from_user.id, 'Во что играть будем!',reply_markup=greet_kb2)
        elif message.text == "Автомат_777":
            await dp.send_message(message.from_user.id, 'Ставь ставку!')
            await Form2.other.set()
        elif message.text == "Краш":
            await dp.send_message(message.from_user.id, 'Ставь ставку!')
            await Form4.other.set()
        elif message.text == "Смешняфка🙃": 
            st = random.randint(1,13)
            if st == 1:
                await message.answer_sticker(r'CAACAgIAAxkBAAED9gliDpFkfMb7I_NBPBltWOD3sUashAACqRMAAo42eUrNKFwnTPiK3CME')
            elif st == 2:
                await message.answer_sticker(r'CAACAgIAAxkBAAED9gpiDpFlFfYViahdf65RRUXc5nRZVgACfhUAAu49eEo8CM7yutGMZyME')
            elif st == 3:
                await message.answer_sticker(r'CAACAgIAAxkBAAED9gdiDpFbNPcjx-GNmVigpLJr0sW3GgACURAAAiEwWUpGtiSsxBG_5CME')
            elif st == 4:
                await message.answer_sticker(r'CAACAgIAAxkBAAED9gViDpFYfO-LcFg7n23hXTjFF-gEYwACdRMAAilKWEqSPTKZ_5JTuSME')
            elif st == 5:
                await message.answer_sticker(r'CAACAgIAAxkBAAED9gNiDpFRdY3WSsRuluop1x83qKzHAAOhEwACnXJZSkwrKYXIgtAjIwQ')
            elif st == 6:
                await message.answer_sticker(r'CAACAgIAAxkBAAED9gFiDpFIiilAJu-BT65A_CoRfL20MgAC1hIAAv5bWEpjW-eyoFzlliME')
            elif st == 7:
                await message.answer_sticker(r'CAACAgIAAxkBAAED9f1iDpE6zvlCDA1xxmo7jaJi2c6ybQAC7BQAAvLUUEq3iPJaGRIHIyME')
            elif st == 8:
                await message.answer_sticker(r'CAACAgIAAxkBAAED9ftiDpE1s_r7YnxUjmqaHegNDSHUeQACZxMAAjYzUEqaiY8XOvYZUSME')
            elif st == 9:
                await message.answer_sticker(r'CAACAgIAAxkBAAED9fdiDpEwhpa8vlJ-pfsSS5SC7sEnNgACbxQAAv2zUEpD3fPTiWe-rSME')
            elif st == 10:
                await message.answer_sticker(r'CAACAgIAAxkBAAED9fliDpEzVL9som1Cu3MlVTsQJoOQuAACWBYAAptWUEq4S342u4c8_yME')
            elif st == 11:
                await message.answer_sticker(r'CAACAgIAAxkBAAED9fViDpEuobSPfvIHTfMY3Hs41qVo-gACoBMAAoLtUEoOe30VEyBgDSME')
            elif st == 12:
                await message.answer_sticker(r'CAACAgIAAxkBAAED9fJiDpEnq5qKGbtJQfsn1xg4gcBVyQAC0xUAAuRjUErzDe_SELlzrSME')
            elif st == 13:
                await message.answer_sticker(r'CAACAgIAAxkBAAED9fFiDpEmw2slMszkRoAGB_FHozNOcQAC8RIAAjRQUEqt6w4TTogtZyME')
        elif message.text == "Рандом🎲":
            item1 = InlineKeyboardButton("Число(0-9)", callback_data='keyboaord1_button1')
            item2 = InlineKeyboardButton("Цвет🌈", callback_data='keyboaord1_button2')
            item3 = InlineKeyboardButton("Фраза¯\_(ツ)_/¯", callback_data='keyboaord1_button3')
            markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)
            await dp.send_message(message.from_user.id, 'Выбирете что нужно(=', reply_markup=markup)
        elif message.text == "Заявка модератору🗎":
            await dp.send_message(message.from_user.id, 'Напиши причину того, что тебе не понравилось в поведении админов🤔.')
            await Form3.text.set()
        elif message.text == "Промокоды🎂":
            await dp.send_message(message.from_user.id,'Напиши промоко_дик')
            await Form1.promo.set()
        elif message.text == "Купить валюту":
            item1_1 = types.InlineKeyboardButton("ЛешаКоин", callback_data='min1')
            item2_1 = types.InlineKeyboardButton("СмешиКоин", callback_data='min2')
            item3_1 = types.InlineKeyboardButton("ГрафиКоин", callback_data='min3')
            item4_1 = types.InlineKeyboardButton("Блин я второй Коин", callback_data='min4')
            markup_1 = InlineKeyboardMarkup(row_width=2).add(item1_1, item2_1, item3_1, item4_1)
            await dp.send_message(message.from_user.id, 'Выбирай:', reply_markup=markup_1)
        elif message.text == "Продать валюту":
            item1_2 = types.InlineKeyboardButton("ЛешаКоин", callback_data='pls1')
            item2_2 = types.InlineKeyboardButton("СмешиКоин", callback_data='pls2')
            item3_2 = types.InlineKeyboardButton("ГрафиКоин", callback_data='pls3')
            item4_2 = types.InlineKeyboardButton("Блин я второй Коин", callback_data='pls4')
            markup_2 = InlineKeyboardMarkup(row_width=2).add(item1_2, item2_2, item3_2, item4_2)
            await dp.send_message(message.from_user.id, 'Выбирай:', reply_markup=markup_2)
        elif message.text == "Майнинг":
            pass
        elif message.text == "Назад":
            await dp.send_message(message.from_user.id, 'Ок',reply_markup=greet_kb)
        elif 'Нах' in message.text or 'нах' in message.text:
            await dp.send_message(message.from_user.id, 'только после тебя')
        elif 'Баранина' in message.text or 'баранина' in message.text:
            await dp.send_message(message.from_user.id, 'сама такая')
        elif 'Шлюха' in message.text or 'шлюха' in message.text:
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
            conn = sqlite3.connect("us.db", check_same_thread=False)
            cursor = conn.cursor()
            users = cursor.execute("SELECT * FROM `users`")
            print(users.fetchall())
            er = """select * FROM users where user_id = ?"""
            cursor.execute(er,(message.from_user.id,))
            loves = cursor.fetchall()
            for row in loves:
                love = row[4]
            conn.commit()
            cursor.close()
            if love == 1:
                love = 0
                bal += 100
                await dp.send_message(message.from_user.id, 'Держи денежку')
                conn = sqlite3.connect("us.db", check_same_thread=False)
                cursor = conn.cursor()
                sql_update_query = """Update users set love = ? where user_id = ?"""
                sql_update_query1 = """Update users set money = ? where user_id = ?"""
                data = (love, message.from_user.id,)
                data1 = (bal, message.from_user.id,)
                cursor.execute(sql_update_query, data)
                cursor.execute(sql_update_query1, data1)
                conn.commit()
                cursor.close()
                await dp.send_message(message.from_user.id, '(получено 100💎)')
        elif message.text == "КриптоБиржа💹":
            await dp.send_message(message.from_user.id, "Курс:", reply_markup=greet_kb1)
            global LeshaKoin
            global SmeshiKoin
            global GrafiCoin
            global Blin_ya_ftoroy_coin
            await message.answer(
            fmt.text(
            fmt.text("ЛешаКоин: ",LeshaKoin),
            fmt.text("СмешиКоин: ",SmeshiKoin),
            fmt.text("ГрафиКоин: ",GrafiCoin),
            fmt.text("Блин я второй коин: ",Blin_ya_ftoroy_coin),
            sep="\n"
            ), parse_mode="HTML"
            )
        elif message.text == "Моя биография🤓":
            item1 = InlineKeyboardButton("Как зовут?🧐", callback_data='keyboaord2_button1')
            item2 = InlineKeyboardButton("Сколкьо денег?💸", callback_data='keyboaord2_button2')
            item3 = InlineKeyboardButton("Сколько использовал(а) промокодов?🎫", callback_data='keyboaord2_button3')
            item4 = InlineKeyboardButton("Склько крипты?💹", callback_data='keyboaord2_button4')
            markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3, item4)
            await dp.send_message(message.from_user.id, 'Выбирете что нужно(=', reply_markup=markup)
        elif message.text == "Легенды":
            money = 0
            num = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            for i in range(1, 35):
                conn = sqlite3.connect("us.db", check_same_thread=False)
                cursor = conn.cursor()
                er = """select * FROM users where id = ?"""
                cursor.execute(er,(i,))
                data = cursor.fetchall()
                for row in data:
                    num[i] = row[3]
                conn.commit()
                cursor.close()
            num.sort(reverse=True)
            print(num)
            conn = sqlite3.connect("us.db", check_same_thread=False)
            cursor = conn.cursor()
            er = """select * FROM users where money = ?"""
            cursor.execute(er,(num[0],))
            data = cursor.fetchall()
            for row in data:
                real_name_1 = row[2]
            cursor.execute(er,(num[1],))
            data = cursor.fetchall()
            for row in data:
                real_name_2 = row[2]
            cursor.execute(er,(num[2],))
            data = cursor.fetchall()
            for row in data:
                real_name_3 = row[2]
            conn.commit()
            cursor.close()
            await dp.send_message(message.from_user.id,
            fmt.text(
            fmt.text("💵Самые самые богатые на планете"),
            fmt.text("1 - ",real_name_1,"(",num[0],")"),
            fmt.text("2 - ",real_name_2,"(",num[1],")"),
            fmt.text("3 - ",real_name_3,"(",num[2],")"),
            sep="\n"
            ), parse_mode="HTML"
            )
        else:
            await dp.send_message(message.from_user.id, 'Переведи на ботоводский, я не поняла😢')

@bot.callback_query_handler(lambda c: c.data and c.data.startswith('keyboaord1_button'))
async def process_callbacks_button(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await dp.answer_callback_query(callback_query.id)
        n = random.randint(0,9)
        await dp.send_message(callback_query.from_user.id, str(n))
    if code == 2:
        await dp.answer_callback_query(callback_query.id)
        n = random.randint(1,6)
        if n == 1:
            await dp.send_message(callback_query.from_user.id, 'Красный❤')
        elif n == 2:
            await dp.send_message(callback_query.from_user.id, 'Оранжевый🧡')
        elif n == 3:
            await dp.send_message(callback_query.from_user.id, 'Желтый💛')
        elif n == 4:
            await dp.send_message(callback_query.from_user.id, 'Зеленый💚')
        elif n == 5:
            await dp.send_message(callback_query.from_user.id, 'Синий💙')
        elif n == 6:
            await dp.send_message(callback_query.from_user.id, 'Фиолетовый💜')
            await dp.send_message(callback_query.from_user.id, str(n))
    if code == 3:
        await dp.answer_callback_query(callback_query.id)
        n = random.randint(1,20)
        if n == 1:
            await dp.send_message(callback_query.from_user.id, 'Я всё отдам, но где мне это взять?')
        elif n == 2:
            await dp.send_message(callback_query.from_user.id, 'Моя киска умеет играть в ссалки.')
        elif n == 3:
            await dp.send_message(callback_query.from_user.id, 'Что тебе мешает понять это? Лишние хромосомы?')
        elif n == 4:
            await dp.send_message(callback_query.from_user.id, 'Да ничего, ничего, я на тебя не обижаюсь. У меня сосед тоже дебил…')
        elif n == 5:
            await dp.send_message(callback_query.from_user.id, 'Девушка, капля никотина убивает и не такую лошадь.')
        elif n == 6:
            await dp.send_message(callback_query.from_user.id, 'По морде получили? Распишитесь.')
        elif n == 7:
            await dp.send_message(callback_query.from_user.id, 'Любишь кататься — катись к чертовой матери')
        elif n == 8:
            await dp.send_message(callback_query.from_user.id, 'Дураки — не мамонты, сами не вымрут')
        elif n == 9:
            await dp.send_message(callback_query.from_user.id, 'Машу пальцем не испортишь')
        elif n == 10:
            await dp.send_message(callback_query.from_user.id, 'Береги родину — отдыхай за границей.')
        elif n == 11:
            await dp.send_message(callback_query.from_user.id, 'Один в поле — а вони…')
        elif n == 12:
            await dp.send_message(callback_query.from_user.id, 'В здоровом теле — здоровый стул')
        elif n == 13:
            await dp.send_message(callback_query.from_user.id, 'Золотое правило девушки: не знаешь, что сказать — улыбнись и поправь лифчик.')
        elif n == 14:
            await dp.send_message(callback_query.from_user.id, 'Лучше переспать, чем недоесть.')
        elif n == 15:
            await dp.send_message(callback_query.from_user.id, 'Лучше один раз потрогать — чем сто раз увидеть.')
        elif n == 16:
            await dp.send_message(callback_query.from_user.id, 'БАР — Библиотека Алкогольного Раритета.')
        elif n == 17:
            await dp.send_message(callback_query.from_user.id, 'В каждую погоду благо дать.')
        elif n == 18:
            await dp.send_message(callback_query.from_user.id, 'Оптимисты изобретают самолеты, а пессимисты – парашюты.')
        elif n == 19:
            await dp.send_message(callback_query.from_user.id, 'Девушка, давайте скрепим нашу дружбу половым актом.')
        else:
            await dp.send_message(callback_query.from_user.id, 'Люблю тебя))')

@bot.callback_query_handler(lambda c: c.data and c.data.startswith('keyboaord2_button'))
async def process_callback_button(callback_query: types.CallbackQuery):
    global promo1
    global promo2
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        conn = sqlite3.connect("us.db", check_same_thread=False)
        cursor = conn.cursor()
        users = cursor.execute("SELECT * FROM `users`")
        print(users.fetchall())
        er = """select * FROM users where user_id = ?"""
        cursor.execute(er,(callback_query.from_user.id,))
        real_name = cursor.fetchall()
        for row in real_name:
            real_name = row[2]
        conn.commit()
        cursor.close()
        await dp.send_message(callback_query.from_user.id, "Тебя зовут - " + str(real_name))
    if code == 2:
        conn = sqlite3.connect("us.db", check_same_thread=False)
        cursor = conn.cursor()
        users = cursor.execute("SELECT * FROM `users`")
        print(users.fetchall())
        er = """select * FROM users where user_id = ?"""
        cursor.execute(er,(callback_query.from_user.id,))
        money = cursor.fetchall()
        for row in money:
            money = row[3]
        conn.commit()
        cursor.close()
        await dp.send_message(callback_query.from_user.id, "У тебя " + str(money) + "💎")
    if code == 3:
        val = 0
        conn = sqlite3.connect("us.db", check_same_thread=False) 
        cursor = conn.cursor()
        er = """select * FROM users where user_id = ?"""
        cursor.execute(er,(callback_query.from_user.id,))
        base = cursor.fetchall()
        for row in base:
            promo1 = row[6]
            promo2 = row[7]
        conn.commit()
        cursor.close()
        if promo1 == 0:
            val=val+1
        if promo2 == 0:
            val=val+1
        await dp.send_message(callback_query.from_user.id, "Ты использовал " + str(val) + " промокод/а/ов")
    if code == 4:
        global bal
        global LeshaKoin_im
        global SmeshiKoin_im
        global GrafiCoin_im
        global Blin_ya_ftoroy_coin_im
        conn = sqlite3.connect("us.db", check_same_thread=False) 
        cursor = conn.cursor()
        er = """select * FROM users where user_id = ?"""
        cursor.execute(er,(callback_query.from_user.id,))
        base = cursor.fetchall()
        for row in base:
            bal = row[3]
            LeshaKoin_im = row[8]
            SmeshiKoin_im = row[9]
            GrafiCoin_im = row[10]
            Blin_ya_ftoroy_coin_im = row[11]
        conn.commit()
        cursor.close()
        await dp.send_message(callback_query.from_user.id, "Вот сколько у тебя крипты:")
        await dp.send_message(callback_query.from_user.id,
            fmt.text(
            fmt.text("ЛешаКоин: ",LeshaKoin_im),
            fmt.text("СмешиКоин: ",SmeshiKoin_im),
            fmt.text("ГрафиКоин: ",GrafiCoin_im),
            fmt.text("Блин я второй коин: ",Blin_ya_ftoroy_coin_im),
            sep="\n"
            ), parse_mode="HTML"
            )
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('keyboaordcas_button'))
async def process_callback_button_3(callback_query: types.CallbackQuery, x_now, bal):
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await dp.send_message(callback_query.from_user.id, f"Поздравляю, ты выйграл{x_now}")
@bot.message_handler(state=Form.name)
async def process_gender1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        conn = sqlite3.connect("us.db", check_same_thread=False)
        cursor = conn.cursor()
        sql_update_query = """Update users set real_name = ? where user_id = ?"""
        data = (remove_char(md.bold(data['name'])), message.from_user.id,)
        cursor.execute(sql_update_query, data)
        conn.commit()
        cursor.close()
    await state.finish()
    await dp.send_message(message.from_user.id, "Спасибки)")

@bot.message_handler(state=Form1.promo)
async def get1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        global promo_1
        global promo_2
        global bal_s
        data['promo'] = message.text
        global bal
        conn = sqlite3.connect("us.db", check_same_thread=False)
        cursor = conn.cursor()
        users = cursor.execute("SELECT * FROM `users`")
        print(users.fetchall())
        er = """select * FROM users where user_id = ?"""
        cursor.execute(er,(message.from_user.id,))
        promo1 = cursor.fetchall()
        for row in promo1:
            bal = row[3]
            promo_1 = row[6]
            promo_2 = row[7]
        conn.commit()
        cursor.close()
        if data['promo'] == 'eRop1n':
            if promo_1 == 1:
                await dp.send_message(message.chat.id, 'Поздравляю ты выйграл 100💎')
                bal += 100
                promo_1 = 0
                conn = sqlite3.connect("us.db", check_same_thread=False)
                cursor = conn.cursor()
                sql_update_query = """Update users set promo1 = ? where user_id = ?"""
                sql_update_query1 = """Update users set money = ? where user_id = ?"""
                data1 = (bal, message.from_user.id,)
                data = (promo_1, message.from_user.id,)
                cursor.execute(sql_update_query1, data1)
                cursor.execute(sql_update_query, data)
                conn.commit()
                cursor.close()
            elif promo_1 == 0:  
                await dp.send_message(message.chat.id, 'Ты уже использовал такой промокод')  
        elif data['promo'] == 'Suzanne_well_done':
            if promo_2 == 1:
                conn = sqlite3.connect("us.db", check_same_thread=False)
                cursor = conn.cursor()
                users = cursor.execute("SELECT * FROM `users`")
                print(users.fetchall())
                er = """select * FROM users where user_id = ?"""
                cursor.execute(er,(1427309639,))
                data3 = cursor.fetchall()
                for row in data3:
                    bal_s = row[3]
                conn.commit()
                cursor.close()
                await dp.send_message(message.chat.id, 'Поздравляю ты выйграл 150💎.А также ты поддержал Сюзану денежкой, так как это реферальный код))')
                bal += 150
                promo_2 = 0
                conn = sqlite3.connect("us.db", check_same_thread=False)
                cursor = conn.cursor()
                sql_update_query = """Update users set promo2 = ? where user_id = ?"""
                sql_update_query1 = """Update users set money = ? where user_id = ?"""
                data2 = (bal_s+150, 1427309639,)
                data1 = (bal, message.from_user.id,)
                data = (promo_2, message.from_user.id,)
                cursor.execute(sql_update_query1, data2)
                cursor.execute(sql_update_query1, data1)
                cursor.execute(sql_update_query, data)
                conn.commit()
                cursor.close()
            else:
                await dp.send_message(message.chat.id, 'Ты уже использовал такой промокод')  
        else:
            await dp.send_message(message.chat.id, 'Такого промокода нету😢')
    await state.finish()

@bot.message_handler(state=Form2.other)
async def get2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        global bal
        conn = sqlite3.connect("us.db", check_same_thread=False) 
        cursor = conn.cursor()
        users = cursor.execute("SELECT * FROM `users`")
        print(users.fetchall())
        er = """select * FROM users where user_id = ?"""
        cursor.execute(er,(message.chat.id,))
        money = cursor.fetchall()
        for row in money:
            global bal
            bal = row[3]
        conn.commit()
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
            conn = sqlite3.connect("us.db", check_same_thread=False)
            cursor = conn.cursor()
            de = """Update users SET money = ? WHERE user_id = ?"""
            w = message.chat.id
            de1 = (bal,w)
            cursor.execute(de, de1)
            conn.commit()
            cursor.close() 
        else:
            await dp.send_message(message.chat.id, 'Нету деняг)=')
    await state.finish()

@bot.message_handler(state=Form4.other)
async def get(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        global bal
        global x
        conn = sqlite3.connect("us.db", check_same_thread=False) 
        cursor = conn.cursor()
        users = cursor.execute("SELECT * FROM `users`")
        print(users.fetchall())

        er = """select * FROM users where user_id = ?"""
        cursor.execute(er,(message.chat.id,))
        money = cursor.fetchall()
        for row in money:
            global bal
            bal = row[3]
        conn.commit()
        data['other'] = message.text
        if bal >= int(data['other']):
            await dp.send_message(message.chat.id, 'Поехали🍀')
            time.sleep(2)
            k = [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,4,4]
            ab = k[random.randint(1, 24)]
            if ab == 0:
                x = round(random.uniform(1.00, 1.20), 1)
            elif ab == 1:
                x = round(random.uniform(1.20, 2.00), 1)
            elif ab == 2:
                x = round(random.uniform(2.00, 5.00), 1)
            elif ab == 3:
                x = round(random.uniform(5.00, 10.00), 1)
            elif ab == 4:
                x = round(random.uniform(10.00, 100.00), 1)
            await dp.send_message(message.chat.id, f"Ты поставил {int(data['other'])}💎",reply_markup=markup3)
            upload_message = await dp.send_message(chat_id=message.chat.id, text="1")
            x_now = 1
            print(x)
            timing = time.time()
            while(True):   
                if time.time() - timing > 0.25:
                    timing = time.time()
                    if x_now == x:
                        break
                    else:
                        x_now += 0.1
                        x_now = round(x_now,1)
                        await upload_message.edit_text(text=f"{x_now}")
            await dp.send_message(message.chat.id, f"Краш!")
    await state.finish()

@bot.message_handler(state=Form3.text)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        await dp.send_message(group_id, "@" + message.from_user.username + ": " + data['text'])
        await dp.send_message(message.from_user.id, 'Все отправила. Жди ответа😁')
    await state.finish()

@bot.callback_query_handler(lambda c: c.data and c.data.startswith('min'))
async def cript_min(callback_query: types.CallbackQuery):
    global bal
    global LeshaKoin_im
    global SmeshiKoin_im
    global GrafiCoin_im
    global Blin_ya_ftoroy_coin_im
    conn = sqlite3.connect("us.db", check_same_thread=False) 
    cursor = conn.cursor()
    er = """select * FROM users where user_id = ?"""
    cursor.execute(er,(callback_query.from_user.id,))
    base = cursor.fetchall()
    for row in base:
        bal = row[3]
        LeshaKoin_im = row[8]
        SmeshiKoin_im = row[9]
        GrafiCoin_im = row[10]
        Blin_ya_ftoroy_coin_im = row[11]
    conn.commit()
    cursor.close()
    await dp.answer_callback_query(callback_query.id)
    code2 = callback_query.data[-1]
    if code2.isdigit():
        code2 = int(code2)
    if code2 == 1:
        if bal >= LeshaKoin:
            LeshaKoin_im = LeshaKoin_im + 1
            bal = round(bal - LeshaKoin)
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Потрачено {round(LeshaKoin)}')
            conn = sqlite3.connect("us.db", check_same_thread=False)
            cursor = conn.cursor()
            sql_update_query = """Update users set LeshaKoin = ? where user_id = ?"""
            de = """Update users SET money = ? WHERE user_id = ?"""
            data = (LeshaKoin_im, callback_query.from_user.id,)
            w = callback_query.from_user.id
            de1 = (bal,w)
            cursor.execute(sql_update_query, data)
            cursor.execute(de, de1)
            conn.commit()
            cursor.close()
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно средств❌')
    if code2 == 2:
        if bal >= SmeshiKoin:
            SmeshiKoin_im = SmeshiKoin_im + 1
            bal = round(bal - SmeshiKoin)
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Потрачено {round(SmeshiKoin)}')
            conn = sqlite3.connect("us.db", check_same_thread=False)
            cursor = conn.cursor()
            sql_update_query = """Update users set SmeshiKoin = ? where user_id = ?"""
            de = """Update users SET money = ? WHERE user_id = ?"""
            data = (SmeshiKoin_im, callback_query.from_user.id,)
            w = callback_query.from_user.id
            de1 = (bal,w)
            cursor.execute(sql_update_query, data)
            cursor.execute(de, de1)
            conn.commit()
            cursor.close()
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно средств❌')
    if code2 == 3:
        if bal >= GrafiCoin:
            GrafiCoin_im = GrafiCoin_im + 1
            bal = round(bal - GrafiCoin)
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Потрачено {round(GrafiCoin)}')
            conn = sqlite3.connect("us.db", check_same_thread=False)
            cursor = conn.cursor()
            sql_update_query = """Update users set GrafiCoin = ? where user_id = ?"""
            de = """Update users SET money = ? WHERE user_id = ?"""
            data = (GrafiCoin_im, callback_query.from_user.id,)
            w = callback_query.from_user.id
            de1 = (bal,w)
            cursor.execute(sql_update_query, data)
            cursor.execute(de, de1)
            conn.commit()
            cursor.close()
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно средств❌')
    if code2 == 4:
        if bal >= Blin_ya_ftoroy_coin:
            Blin_ya_ftoroy_coin_im = Blin_ya_ftoroy_coin_im + 1
            bal = round(bal - Blin_ya_ftoroy_coin)
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Потрачено {round(Blin_ya_ftoroy_coin)}')
            conn = sqlite3.connect("us.db", check_same_thread=False)
            cursor = conn.cursor()
            sql_update_query = """Update users set B_YA_V_Coin = ? where user_id = ?"""
            de = """Update users SET money = ? WHERE user_id = ?"""
            data = (Blin_ya_ftoroy_coin_im, callback_query.from_user.id,)
            w = callback_query.from_user.id
            de1 = (bal,w)
            cursor.execute(sql_update_query, data)
            cursor.execute(de, de1)
            conn.commit()
            cursor.close()
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно средств❌')

@bot.callback_query_handler(lambda c: c.data and c.data.startswith('pls'))
async def cript_pls(callback_query: types.CallbackQuery):
    global bal
    global LeshaKoin_im
    global SmeshiKoin_im
    global GrafiCoin_im
    global Blin_ya_ftoroy_coin_im
    conn = sqlite3.connect("us.db", check_same_thread=False) 
    cursor = conn.cursor()
    er = """select * FROM users where user_id = ?"""
    cursor.execute(er,(callback_query.from_user.id,))
    base = cursor.fetchall()
    for row in base:
        bal = row[3]
        LeshaKoin_im = row[8]
        SmeshiKoin_im = row[9]
        GrafiCoin_im = row[10]
        Blin_ya_ftoroy_coin_im = row[11]
    conn.commit()
    cursor.close()
    await dp.answer_callback_query(callback_query.id)
    code2 = callback_query.data[-1]
    if code2.isdigit():
        code2 = int(code2)
    if code2 == 1:
        if LeshaKoin_im >= 1:
            LeshaKoin_im = LeshaKoin_im - 1
            LeshaKoin_pls = LeshaKoin - LeshaKoin/100*10
            bal = round(bal + LeshaKoin_pls)
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Получено {round(LeshaKoin_pls)}')
            conn = sqlite3.connect("us.db", check_same_thread=False)
            cursor = conn.cursor()
            sql_update_query = """Update users set LeshaKoin = ? where user_id = ?"""
            de = """Update users SET money = ? WHERE user_id = ?"""
            data = (LeshaKoin_im, callback_query.from_user.id,)
            w = callback_query.from_user.id
            de1 = (bal,w)
            cursor.execute(sql_update_query, data)
            cursor.execute(de, de1)
            conn.commit()
            cursor.close()
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно крипты❌')
    if code2 == 3:
        if GrafiCoin_im >= 1:
            GrafiCoin_im = GrafiCoin_im - 1
            GrafiCoin_pls = GrafiCoin - GrafiCoin/100*10
            bal = round(bal + GrafiCoin_pls)
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Получено {round(GrafiCoin_pls)}')
            conn = sqlite3.connect("us.db", check_same_thread=False)
            cursor = conn.cursor()
            sql_update_query = """Update users set GrafiCoin = ? where user_id = ?"""
            de = """Update users SET money = ? WHERE user_id = ?"""
            data = (GrafiCoin_im, callback_query.from_user.id,)
            w = callback_query.from_user.id
            de1 = (bal,w)
            cursor.execute(sql_update_query, data)
            cursor.execute(de, de1)
            conn.commit()
            cursor.close()
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно крипты❌')
    if code2 == 2:
        if SmeshiKoin_im >= 1:
            SmeshiKoin_im = SmeshiKoin_im - 1
            SmeshiKoin_pls = SmeshiKoin - SmeshiKoin/100*10
            bal = round(bal + SmeshiKoin_pls)
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Получено {round(SmeshiKoin_pls)}')
            conn = sqlite3.connect("us.db", check_same_thread=False)
            cursor = conn.cursor()
            sql_update_query = """Update users set SmeshiKoin = ? where user_id = ?"""
            de = """Update users SET money = ? WHERE user_id = ?"""
            data = (SmeshiKoin_im, callback_query.from_user.id,)
            w = callback_query.from_user.id
            de1 = (bal,w)
            cursor.execute(sql_update_query, data)
            cursor.execute(de, de1)
            conn.commit()
            cursor.close()
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно крипты❌')
    if code2 == 4:
        if Blin_ya_ftoroy_coin_im >= 1:
            Blin_ya_ftoroy_coin_im = Blin_ya_ftoroy_coin_im - 1
            Blin_ya_ftoroy_coin_pls = Blin_ya_ftoroy_coin - Blin_ya_ftoroy_coin/100*10
            bal = round(bal + Blin_ya_ftoroy_coin_pls)
            await dp.send_message(callback_query.from_user.id, f'Успешно✅. Получено {round(Blin_ya_ftoroy_coin_pls)}')
            conn = sqlite3.connect("us.db", check_same_thread=False)
            cursor = conn.cursor()
            sql_update_query = """Update users set B_YA_V_Coin = ? where user_id = ?"""
            de = """Update users SET money = ? WHERE user_id = ?"""
            data = (Blin_ya_ftoroy_coin_im, callback_query.from_user.id,)
            w = callback_query.from_user.id
            de1 = (bal,w)
            cursor.execute(sql_update_query, data)
            cursor.execute(de, de1)
            conn.commit()
            cursor.close()
        else:
            await dp.send_message(callback_query.from_user.id, 'Недостаточно крипты❌')

if __name__ == '__main__':
    executor.start_polling(bot,skip_updates=True)
