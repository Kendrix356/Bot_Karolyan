from aiogram.dispatcher.filters.state import State, StatesGroup

class Form_name(StatesGroup):
    name = State() 
class Form_promo(StatesGroup):
    promo = State()  
class Form_cas(StatesGroup):
    stavka = State()
class Form_moder(StatesGroup):
    moder = State()
class Form_send_mes(StatesGroup):
    id = State()
    mes = State()
class Form_id_add(StatesGroup):
    id = State()
class Form_id_delete(StatesGroup):
    id = State()
