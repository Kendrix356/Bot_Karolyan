from aiogram.dispatcher.filters.state import State, StatesGroup

class Form_name(StatesGroup):
    name = State() 
class Form_promo(StatesGroup):
    promo = State()  
class Form_cas777(StatesGroup):
    stavka = State()
class Form_crash(StatesGroup):
    stavka = State()
class Form_moder(StatesGroup):
    moder = State()
class Form_send_mes(StatesGroup):
    id = State()
    mes = State()
