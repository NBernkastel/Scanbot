from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, WebAppData, Contact

from src.config.bot_config import bot
from src.config.texts import GREAT_USER_TEXT, OPEN_QR_TEXT
from src.database.db_config import supabase
from src.keyboards.keyboards import phone_keyboard, open_qr_keyboard
from src.states.states import User

qr_router = Router()


@qr_router.message(CommandStart(), StateFilter(None))
async def start_command(message: Message, state: FSMContext):
    if not supabase.table("users").select("chat_id").eq("chat_id", message.chat.id).execute().data:
        await bot.send_message(message.chat.id, GREAT_USER_TEXT, reply_markup=phone_keyboard())
        await state.set_state(User.user_phone)
    else:
        await state.set_state(User.qr_code)
        await bot.send_message(message.chat.id, OPEN_QR_TEXT, reply_markup=open_qr_keyboard())


@qr_router.message(F.content_type == 'contact', User.user_phone)
async def contact_handler(message: Message, state: FSMContext):
    contact = message.contact
    phone_number = contact.phone_number
    supabase.table("users").insert({'chat_id': message.chat.id, 'phone_number': phone_number}).execute()
    await state.set_state(User.qr_code)
    await bot.send_message(message.chat.id, OPEN_QR_TEXT, reply_markup=open_qr_keyboard())


@qr_router.message(F.content_type == 'web_app_data')
async def qr_data_handler(data: WebAppData):
    web_app_data = data.web_app_data.data
    data: list = supabase.table("users").select("phone_number").eq("chat_id", data.chat.id).execute().data
    print(web_app_data, data[0]['phone_number'])
