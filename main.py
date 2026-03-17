import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# Твой токен уже здесь
TOKEN = "8711447507:AAFhRRMAyb87dKbVoy79QIhO_8WaEz389co"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Твои сервера
SUB_DATA = """vless://948fac3c-42bf-41a6-a5f9-704d36ff0d8d@103.73.65.187:7000?security=tls&encryption=none&type=ws&host=snippet.fgfw.indevs.in&path=/danfeng&sni=snippet.fgfw.indevs.in&fp=chrome#🇦🇺_Australia
vless://055e3bd2-10f8-4d9c-8f7d-70b9f659e476@172.64.33.117:8443?allowInsecure=1&alpn=h3&encryption=none&host=m1.mwu.de5.net&path=/proxyip=sjc.o00o.ooo&security=tls&sni=m1.mwu.de5.net&type=ws#🇨🇦_Canada
vless://055e3bd2-10f8-4d9c-8f7d-70b9f659e476@104.18.38.250:8443?allowInsecure=1&alpn=h3&encryption=none&host=m1.mwu.de5.net&path=/proxyip=sjc.o00o.ooo&security=tls&sni=m1.mwu.de5.net&type=ws#🇸🇬_Singapore
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmNTRjZGVlMTBmOGIyNWNl@57.129.95.38:11201#🇩🇪_Germany"""

@dp.message(Command("start"))
async def start(message: types.Message):
    text = (
        "<b>BluesPN</b> — конфиденциальность и скорость 🛜\n\n"
        "Ваш пробный период: <b>4 дня</b> ⚡️\n"
        "Нажмите кнопку ниже, чтобы получить настройки."
    )
    kb = [[types.InlineKeyboardButton(text="Получить ключ 🔑", callback_data="get_vpn")]]
    await message.answer(text, reply_markup=types.InlineKeyboardMarkup(inline_keyboard=kb), parse_mode="HTML")

@dp.callback_query(F.data == "get_vpn")
async def send_vpn(callback: types.CallbackQuery):
    await callback.message.answer(f"Скопируйте этот текст и вставьте в приложение:\n\n<code>{SUB_DATA}</code>", parse_mode="HTML")
    await callback.answer()

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
