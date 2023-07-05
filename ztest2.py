import random
import time
from aiogram.types import InlineKeyboardMarkup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Создание экземпляров бота и диспетчера
dp = Bot(token="5095654656:AAGGKQ21-440lk-YNvvtgu2z2wjTAie572Y")
bot = Dispatcher(dp)

# Словарь для хранения данных игр
game_data = {}


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


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):
    chat_id = message.chat.id
    game_data[chat_id] = {
        'game_board': create_game_board(),
        'current_level': 0
    }
    await show_game_board(chat_id)


# Обработчик инлайн-кнопок
@dp.callback_query_handler(lambda c: c.data in ['1', '2', '3'])
async def choose_cell(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    user_choice = int(callback_query.data)
    game_board = game_data[chat_id]['game_board']
    current_level = game_data[chat_id]['current_level']
    # print(game_board[current_level][user_choice-1],user_choice, current_level, game_board)
    game_data[chat_id]['current_level'] += 1
    if game_board[current_level][user_choice-1] == "💣":
        await bot.send_message(chat_id, 'Вы проиграли. Попробуйте еще раз!')
        await show_game_board(chat_id)
        time.sleep(1)
        await callback_query.message.delete()
        del game_data[chat_id]
    else:
        if current_level == 4:
            await bot.send_message(chat_id, 'Поздравляю! Вы прошли все слои. Вы победили.')
            await show_game_board(chat_id)
            time.sleep(1)
            await callback_query.message.delete()
            del game_data[chat_id]
        else:
            await show_game_board(chat_id)


# Функция для отображения игрового поля
async def show_game_board(chat_id):
    game_board = game_data[chat_id]['game_board']
    current_level = game_data[chat_id]['current_level']
    board_message = display_game_board(game_board, current_level)

    item1 = types.InlineKeyboardButton("1", callback_data='1')
    item2 = types.InlineKeyboardButton("2", callback_data='2')
    item3 = types.InlineKeyboardButton("3", callback_data='3')
    item4 = types.InlineKeyboardButton("Забрать", callback_data='4')
    keyboard = InlineKeyboardMarkup(row_width=3).add(item1, item2, item3, item4)
    if current_level != 0:
            try:
                await bot.edit_message_text(chat_id=chat_id, message_id=game_data[chat_id]['message_id'],
                                            text=board_message, reply_markup=keyboard)
            except: pass
    else:
        ms = await bot.send_message(chat_id=chat_id, text=board_message, reply_markup=keyboard)
        game_data[chat_id]['message_id'] = ms["message_id"]


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
