from constants import *
from objects import *
from Function import *
from fsm import *

from create_bot import dp,bot

from handlers import (
    biography, admin_panal, buizness, casino, magazin,
    map, menu, promocodes, request_to_moderator, school, workers, start
)
from threading import Thread
from aiogram.utils import executor

thread_buizness = Thread(target=run_buizness_and_cripts)
thread_buizness.start()

start.reg_handlers_start(bot)
admin_panal.reg_handlers_admin_panel(bot)
biography.reg_handlers_biography(bot)
buizness.reg_handlers_buizness(bot)
casino.reg_handlers_casino(bot)
magazin.reg_handlers_magazin(bot)
map.reg_handlers_map(bot)
promocodes.reg_handlers_promocodes(bot)
request_to_moderator.reg_handlers_request_to_moderator(bot)
school.reg_handlers_school(bot)
workers.reg_handlers_school(bot)
menu.reg_handlers_menu(bot)

executor.start_polling(bot,skip_updates=True)
