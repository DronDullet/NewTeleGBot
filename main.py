from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio

token = "6545635337:AAGOOLuN2I5mTqk9YOPw8R10tQfdG2ZXlLM"


async def start_bot(bot: Bot):
    await bot.send_message(1285679933, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(1285679933, text="Бот остановлен!")


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}. Рад тебя видеть!")
    await message.answer(f"Привет {message.from_user.first_name}. Рад тебя видеть!")
    await message.reply(f"Привет {message.from_user.first_name}. Рад тебя видеть!")


async def start():
    bot = Bot(token=token)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.sessioin.close()

if __name__ == '__main__':
    asyncio.run(start())
