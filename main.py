import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Loglarni sozlash (xatoliklarni kuzatish uchun)
logging.basicConfig(level=logging.INFO)

# Tokenni server muhitidan olamiz
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "👋 Assalomu alaykum! Gronit AI tizimiga xush kelibsiz.\n"
        "Men sizga yordam berishga tayyorman. Menga ixtiyoriy savol yoʻllashingiz mumkin!"
    )

@dp.message_handler()
async def echo_all(message: types.Message):
    # Bu yerga keyinchalik sun'iy intellekt miyasini ulaymiz
    await message.answer(f"Siz yozdingiz: {message.text}\n\nHozircha men test rejimida ishlayapman.")

if name == 'main':
    executor.start_polling(dp, skip_updates=True)
