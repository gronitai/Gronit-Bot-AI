import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Loglarni sozlash
logging.basicConfig(level=logging.INFO)

# Botni sozlash
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# --- 🎯 CHIROYLI MENYU (TUGMALAR) ---
glavniy_menu = ReplyKeyboardMarkup(resize_keyboard=True)
btn_ai = KeyboardButton("🧠 Gronit AI bilan suhbat")
btn_help = KeyboardButton("ℹ️ Yordam va Qo'llanma")
btn_settings = KeyboardButton("⚙️ Sozlamalar")
glavniy_menu.add(btn_ai).row(btn_help, btn_settings)

# --- 🚀 BUYRUQLAR (HANDLERS) ---

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    welcome_text = (
        f"👋 <b>Assalomu alaykum, {user_name}!</b>\n\n"
        f"🤖 <b>Gronit AI</b> tizimining rasmiy botiga xush kelibsiz!\n"
        f"Men sizga har qanday savolingizga javob topishda va kod yozishda yordam bera olaman.\n\n"
        f"👇 Boshlash uchun pastdagi menyudan foydalaning:"
    )
    await message.reply(welcome_text, reply_markup=glavniy_menu)

@dp.message_handler(lambda message: message.text == "🧠 Gronit AI bilan suhbat")
async def ai_chat(message: types.Message):
    await message.answer(
        "⚡ <b>Sun'iy intellekt moduli yoqilmoqda...</b>\n\n"
        "Menga ixtiyoriy savol yoki topshiriq yuboring. Keyingi qadamda bu yerga to'liq AI miyasi ulanadi!"
    )

@dp.message_handler(lambda message: message.text == "ℹ️ Yordam va Qo'llanma")
async def help_menu(message: types.Message):
    await message.answer(
        "📘 <b>Botdan foydalanish bo'yicha yordam:</b>\n\n"
        "1. Botga savol yuborish uchun pastdagi AI tugmasini bosing.\n"
        "2. Bot hozircha test rejimida ishlamoqda.\n"
        "3. Muammolar yuzaga kelsa, dasturchiga murojaat qiling."
    )

@dp.message_handler(lambda message: message.text == "⚙️ Sozlamalar")
async def settings_menu(message: types.Message):
    await message.answer("⚙️ <b>Sozlamalar bo'limi:</b>\n\nHozircha standart sozlamalar faol.")

@dp.message_handler()
async def echo_all(message: types.Message):
    await message.answer(
        f"✍️ <i>Siz yozdingiz:</i> {message.text}\n\n"
        f"Tizim muvaffaqiyatli ishlayapti. Tez orada AI integratsiyasini yakunlaymiz!"
    )

if name == 'main':
    executor.start_polling(dp, skip_updates=True)
