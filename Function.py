import random
import time
import datetime
import schedule, time
import sqlite3
from constants import *
from objects import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from create_bot import dp


def remove_char(s):
    result = s[1 : -1]
    return result

def is_even(number):
    return number % 0.1 == 0

def buizness_zarp():
    for i in range(100):
        have_buizness = get_data(i, 'buizness')
        if have_buizness != 0:
            if have_buizness == 1: pay = 20
            elif have_buizness == 2: pay = 35
            try:
                Id = get_data(i, 'user_id', 'id')
                send_data(Id,'balance',get_data(Id,'balance')+pay)
                send_data(Id,'buster', 0)
            except: pass

def run_buizness_and_crpts():
    schedule.every().minute.do(buizness_zarp) 
    while True: 
        schedule.run_pending() 
        time.sleep(1)

def send_data(id, column, data_edit):
    conn = sqlite3.connect("us.db", check_same_thread=False)
    cursor = conn.cursor()
    select_wh_user_id = f"""Update users set {column} = ? where user_id = ?"""
    data = (data_edit, id)
    # print(select_wh_user_id)
    # print(data)
    cursor.execute(select_wh_user_id, (data),)
    conn.commit()
    cursor.close()

def get_data(id, column, getform = "user_id"):
    global data
    conn = sqlite3.connect("us.db", check_same_thread=False)
    cursor = conn.cursor()
    select_wh_user_id = f"""select * FROM users where {getform} = ?"""
    cursor.execute(select_wh_user_id, (id,))
    send_data = cursor.fetchall()
    for i in range(len(Table_users)):
        if (column == Table_users[i]):
            # print(Table[i])
            for row in send_data:
                data = row[i]
            # print(data)
    conn.commit()
    cursor.close()
    return data

def reg(user_id):
    conn = sqlite3.connect('us.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO `users` (`user_id`,`name`,`balance`,`love`,`join_data`,`promo1`,`promo2`,`promo3`,`register`,`location`,`buizness`,`inventory`,`buster`,`status`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (user_id, "None", 500, 1, datetime.datetime.now(), 0, 0, 0, 0, "7Б",0,"0.0.0.0.0.0.0.0",0,1))
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

def inventory_add(id,text):
    l = list(get_data(id,'inventory'))
    count = 0
    for item in l:
        if item == '0':
            count += 1
    elemet = 8 - count
    elemet = elemet * 2
    l[elemet] = str(text)
    data = ''.join(l)
    send_data(id,'inventory',data)

def inventory_delete(id,text):
    l = list(get_data(id,'inventory'))
    elemet = l.index(str(text))
    l.pop(elemet)
    l.insert(elemet,'0')
    data = ''.join(l)
    send_data(id,'inventory',data)

# Функция для создания игрового поля
def create_game_board():
    game_board = []
    for _ in range(5):
        row = ['✅', '✅', '✅']
        row[random.randint(0, 2)] = '💣'
        game_board.append(row)
    return game_board


def display_game_board(game_board, current_level):
    board_str = f'Башня:\n'
    for i, row in reversed(list(enumerate(game_board))):
        # print(i+1,current_level,row)
        if i+1 <= current_level:
            row_str = f'{i+1}.0x - {row}\n'
            board_str += row_str
    return board_str

async def backmarkup(chat_id, mess):
    location = get_data(chat_id, 'location')
    if location == 'Столица': await dp.send_message(chat_id, mess, reply_markup=kb_menu_st)
    elif location == 'Верхний город' or location == 'Нижний город': await dp.send_message(chat_id, mess, reply_markup=kb_menu_gr)
    else: await dp.send_message(chat_id, mess, reply_markup=kb_menu)

def custom_sort(arr):
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1
    has_duplicates = any(count > 1 for count in count_dict.values())
    if not has_duplicates:
        return arr
    def custom_key_func(element):
        return (-count_dict.get(element, 0), element)
    sorted_arr = sorted(arr, key=custom_key_func)
    return sorted_arr