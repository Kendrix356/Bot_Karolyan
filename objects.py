from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

item1 = KeyboardButton("Заработак💰")
item2 = KeyboardButton("Казино🤑")
item3 = KeyboardButton("Карта🃏")
item4 = KeyboardButton("Школа🏫") #инлайн
item5 = KeyboardButton("Пожертвование🙏")
item6 = KeyboardButton("Магазин🏪") #инлайн
item7 = KeyboardButton("Моя биография👶")
item8 = KeyboardButton("Топ😎")
item9 = KeyboardButton("Заявка модератору🗎")

item1_st = KeyboardButton("Казино🤑")
item2_st = KeyboardButton("Загс")
item3_st = KeyboardButton("Квартира(самая дорогая)")
item4_st = KeyboardButton("Магазин🏪")
item5_st = KeyboardButton("Карта🃏")


item1_income = KeyboardButton("Работы💼") #инлайн
item2_income = KeyboardButton("Бизнес")
item3_income = KeyboardButton("Промокоды🎂")
item4_income = KeyboardButton("КриптоБиржа💹")

item1_casino = KeyboardButton("Автомат🎰")
# item2_casino = KeyboardButton("Краш📈")

item1_buiznes = KeyboardButton("Бета")

item1_cripto = KeyboardButton("Купить валюту")
item2_cripto = KeyboardButton("Продать валюту")

item_back = KeyboardButton("Назад")

item_stop = KeyboardButton("Завершить")

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu_st = ReplyKeyboardMarkup(resize_keyboard=True)
kb_income = ReplyKeyboardMarkup(resize_keyboard=True)
kb_casino = ReplyKeyboardMarkup(resize_keyboard=True)
kb_buiznes = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cripto = ReplyKeyboardMarkup(resize_keyboard=True)
kb_stop_work = ReplyKeyboardMarkup(resize_keyboard=True)


kb_menu.add(item1, item2, item3)
kb_menu.row(item4, item5, item6, item7)
kb_menu.row(item8, item9)
kb_menu_st.add(item1_st, item2_st)
kb_menu_st.row(item3_st, item4_st, item5_st)
kb_income.add(item1_income, item2_income, item3_income, item4_income, item_back)
kb_casino.add(item1_casino, item_back)
kb_buiznes.add(item1_buiznes, item_back)
kb_cripto.add(item1_cripto, item2_cripto, item_back)
kb_stop_work.add(item_stop)

if __name__ == "__main__":
    kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_menu_st = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_income = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_casino = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_buiznes = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_cripto = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_stop_work = ReplyKeyboardMarkup(resize_keyboard=True)