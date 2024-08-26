from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties

from src.config.instance import secrets

default = DefaultBotProperties(parse_mode='Markdown', protect_content=False)
bot = Bot(token=secrets.TOKEN, default=default)
dp = Dispatcher()