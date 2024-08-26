from aiogram.types import InlineKeyboardButton, KeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiohttp import request


def open_qr_keyboard():
    guest_keyboard = ReplyKeyboardBuilder()
    qr_button = KeyboardButton(text="Open qr",
                               web_app=WebAppInfo(url="https://vue-qr-tg-scanner.vercel.app"))
    guest_keyboard.row(qr_button)

    return guest_keyboard.as_markup(resize_keyboard=True)


def phone_keyboard():
    phone_keyboard = ReplyKeyboardBuilder()
    button = KeyboardButton(text="Отправить номер телефона", request_contact=True)
    phone_keyboard.row(button)

    return phone_keyboard.as_markup(resize_keyboard=True)
