from constants import *
from objects import *
from Function import *
from fsm import *

from create_bot import dp,bot

from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher

async def Заявка_модеру(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id
    async with state.proxy() as data:
        data['text'] = message.text
        await dp.send_message(group_id, "@" + message.from_user.username + ": " + data['text'])
        await backmarkup(chat_id, "Все отправила. Жди ответа😁")
    await state.finish()

def reg_handlers_request_to_moderator(bot: Dispatcher):
    bot.register_message_handler(Заявка_модеру,state=Form_moder.moder)