import random
import time
import datetime
import schedule, time
from constants import *
import sqlite3
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def remove_char(s):
    result = s[1 : -1]
    return result

def is_even(number):
    return number % 0.1 == 0
    
def geeks():
    global LeshaCoin
    global SmeshiСoin
    global GrafiCoin
    global Blin_ya_ftoroy_coin
    print("ЛешаКоин ")
    if random.choice(['+','-']) == '+':
        LeshaCoin = LeshaCoin + random.uniform(0, 10)
        print(LeshaCoin)
    else:
        LeshaCoin = LeshaCoin - random.uniform(0, 10)
        print(LeshaCoin)
    print("СмешиКоин ")
    if random.choice(['+','-']) == '+':
        SmeshiСoin = SmeshiСoin + random.uniform(0, 10)
        print(SmeshiСoin)
    else:
        SmeshiСoin = SmeshiСoin - random.uniform(0, 10)
        print(SmeshiСoin)
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

def get_data(id, column):
    conn = sqlite3.connect("us.db", check_same_thread=False)
    cursor = conn.cursor()
    select_wh_user_id = """select * FROM users where user_id = ?"""
    cursor.execute(select_wh_user_id, (id,))
    send_data = cursor.fetchall()
    for i in range(len(Table)):
        if (column == Table[i]):
            print(Table[i])
            for row in send_data:
                data = row[i]
            print(data)
    conn.commit()
    cursor.close()
    return data

def send_data(id, column, data_edit):
    conn = sqlite3.connect("us.db", check_same_thread=False)
    cursor = conn.cursor()
    select_wh_user_id = f"""Update users set {column} = ? where user_id = ?"""
    data = (data_edit, id)
    print(select_wh_user_id)
    print(data)
    cursor.execute(select_wh_user_id, (data),)
    conn.commit()
    cursor.close()

def reg(user_id):
    conn = sqlite3.connect('us.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO `users` (`user_id`,`name`,`balance`,`love`,`join_data`,`promo1`,`promo2`,`leshaСoin`,`smeshiСoin`,`grafiCoin`,`b_ya_v_Coin`,`register`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (user_id, "None", 500, 1, datetime.datetime.now(), 1, 1, 0, 0, 0, 0, 1))
    conn.commit()

def generate_translate():
    correct_word = random.randint(0,len(words_english)-1)
    while(True):
        error_word1 = random.randint(0,len(words_english)-1)
        error_word2 = random.randint(0,len(words_english)-1)
        if error_word1 != correct_word and error_word2 != correct_word:
            break

    situaded = random.randint(1,3)
    if situaded == 1:
        item1 = InlineKeyboardButton(words_russian[correct_word], callback_data='translate_1')
        item2 = InlineKeyboardButton(words_russian[error_word1], callback_data='translate_2')
        item3 = InlineKeyboardButton(words_russian[error_word2], callback_data='translate_3')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3)

    elif situaded == 2:
        item1 = InlineKeyboardButton(words_russian[error_word1], callback_data='translate_1')
        item2 = InlineKeyboardButton(words_russian[correct_word], callback_data='translate_2')
        item3 = InlineKeyboardButton(words_russian[error_word2], callback_data='translate_3')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3) 

    else:
        item1 = InlineKeyboardButton(words_russian[error_word1], callback_data='translate_1')
        item2 = InlineKeyboardButton(words_russian[error_word2], callback_data='translate_2')
        item3 = InlineKeyboardButton(words_russian[correct_word], callback_data='translate_3')
        markup = InlineKeyboardMarkup(row_width=2).add(item1, item2, item3) 
    
    return situaded, correct_word, markup