from constants import *
from objects import *
from Function import *
from fsm import *

from create_bot import dp,bot

from aiogram import types
from aiogram.dispatcher import Dispatcher

async def Бизнес(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await dp.answer_callback_query(callback_query.id)
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    buizness_have = get_data(chat_id,'buizness')

    if code == 2:
        await dp.send_message(chat_id, 'Бизнес работает так: каждый час ты получаешь \
                                        зарплату с бизнеса который ты купил. Содержать \
                                        бизнес можно только один, если ты купил другой, \
                                        то тот, котороый у тебя был не продается, а деньги \
                                        за него не возварщаются. Когда бизнес окупается, \
                                        прибыль уменьшается на 40 процентов(затраты)')
    if code == 1:
        if buizness[buizness_have] == 'Автомат с едой':
            await dp.send_message(chat_id, 'Характеристеки:\nЗаработок в час: 20\nЗаработок в день: 480\nЗаработок после окупа в день: 288')
        elif buizness[buizness_have] == 'Кофейня':
            await dp.send_message(chat_id, 'Характеристеки:\nЗаработок в час: 35\nЗаработок в день: 840\nЗаработок после окупа в день: 504')

def reg_handlers_buizness(bot: Dispatcher):
    bot.register_callback_query_handler(Бизнес,lambda c: c.data and c.data.startswith('pod_'))