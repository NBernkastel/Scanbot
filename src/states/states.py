from aiogram.fsm.state import State, StatesGroup


class User(StatesGroup):
    user_phone = State()
    qr_code = State()