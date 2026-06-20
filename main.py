# Sozlamalar bo'limi
@dp.message_handler(lambda message: message.text == "⚙️ Sozlamalar")
async def settings_menu(message: types.Message):
    await message.answer(
        "⚙️ <b>Sozlamalar paneli:</b>\n\n"
        "• Bot tili: O'zbekcha 🇺🇿\n"
        "• Tizim holati: Barqaror (Stable) 🚀\n\n"
        "Xizmat ko'rsatish sozlamalari standart holatda o'rnatilgan."
    )


# Yordam bo'limi
@dp.message_handler(lambda message: message.text == "ℹ️ Yordam")
async def help_menu(message: types.Message):
    await message.answer(
        "ℹ️ <b>Yordam va Yo'riqnoma:</b>\n\n"
        "1. Botni qayta yurgizish uchun /start buyrug'ini bosing.\n"
        "2. Sun'iy intellekt bilan gaplashish uchun tegishli tugmadan foydalaning.\n"
        "3. Texnik xatoliklar yuzaga kelsa, dasturchiga murojaat qiling."
    )


# --- 🎛 5. INLINE TUGMALAR UCHUN CALLBACK HANDLER ---
@dp.callback_query_handler(lambda call: call.data.startswith('proj_'))
async def callback_projects(call: types.CallbackQuery):
    if call.data == "proj_web":
        await call.message.answer("🌐 <b>Web Yo'nalishi:</b> Biz HTML, CSS, JavaScript va ilg'or freymvorklar yordamida mukammal interfeyslar tayyorlaymiz.")
    elif call.data == "proj_bots":
        await call.message.answer("🤖 <b>Bot Yo'nalishi:</b> Python (Aiogram) va xavfsiz serverlar yordamida yuqori yuklamalarga chidovchi botlar yaratish.")
    await call.answer()


# 6. Echo xabarlar (Foydalanuvchi ixtiyoriy matn yozganda)
@dp.message_handler()
async def echo_all(message: types.Message):
    await message.answer(
        f"✍️ <i>Siz yozdingiz:</i> {message.text}\n\n"
        f"Tizim 100% barqaror ishlamoqda. Keyingi qadamda aynan shu qismga AI miyasini ulaymiz!"
    )


# --- 🚀 7. BOTNI ISHGA TUSHIRISH (XATOSIZ QISM) ---
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
