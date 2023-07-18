import asyncio
import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "5095654656:AAGGKQ21-440lk-YNvvtgu2z2wjTAie572Y"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Список слов и их переводов
words = {
    'hello': ['привет', 'приветствие', 'здравствуй'],
    'cat': ['кошка', 'кот', 'котик'],
    'dog': ['собака', 'пес', 'собачка'],
    'house': ['дом', 'жилище', 'квартира'],
    'book': ['книга', 'книжка', 'тетрадь'],
    'sun': ['солнце', 'солнышко', 'свет'],
    'car': ['машина', 'автомобиль', 'транспорт'],
    'tree': ['дерево', 'древо', 'растение'],
    'bird': ['птица', 'птичка', 'птичонка'],
    'sky': ['небо', 'воздух', 'атмосфера'],
    # Добавьте свои слова и переводы
}

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет! Давай сыграем в игру. У тебя будет 5 секунд на каждый вопрос. Готов?')
    await asyncio.sleep(2)
    await message.reply('Игра начинается!')

    # Создаем список из всех слов
    word_list = list(words.keys())
    random.shuffle(word_list)

    # Инициализируем счетчики
    correct_count = 0
    wrong_count = 0

    for word in word_list:
        # Выбираем случайные переводы для текущего слова
        translations = words[word]
        random.shuffle(translations)
        correct_translation = translations[0]

        # Создаем InlineKeyboardMarkup с вариантами ответов
        keyboard = types.InlineKeyboardMarkup()
        buttons = [
            types.InlineKeyboardButton(text=translation, callback_data=f'{word}:{translation}') for translation in translations
        ]
        random.shuffle(buttons)
        keyboard.add(*buttons)

        # Отправляем вопрос пользователю
        question_message = await message.reply(f'Как переводится слово "{word}"?', reply_markup=keyboard)

        try:
            # Ждем ответа пользователя
            await asyncio.sleep(5)  # Ожидаем 5 секунд

            # Удаляем сообщение с вопросом
            await bot.delete_message(chat_id=question_message.chat.id, message_id=question_message.message_id)
            wrong_count += 1

        except asyncio.CancelledError:
            # Ответ получен, отменяем таймаут
            pass

        # Ждем некоторое время перед следующим вопросом
        await asyncio.sleep(1)

    # Отправляем результаты игры
    await message.reply(f'Игра окончена!\nПравильные ответы: {correct_count}\nНеправильные ответы: {wrong_count}')


@dp.callback_query_handler(lambda c: True)
async def handle_callback_query(callback_query: types.CallbackQuery):
    # Получаем данные из callback_data
    data = callback_query.data
    word, translation = data.split(':')

    # Проверяем правильность ответа
    if translation == words[word][0]:
        await bot.send_message(chat_id=callback_query.message.chat.id, text='Правильно!')
    else:
        await bot.send_message(chat_id=callback_query.message.chat.id, text='Неправильно!')

    # Отвечаем на callback_query, чтобы убрать всплывающее окно
    await callback_query.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
