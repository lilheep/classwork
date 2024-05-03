"""Запуск всего бота"""
import asyncio
from aiogram import Dispatcher
from handlers import include_routers
from tokens import bot

dp = Dispatcher()

async def main():
    """запуск бота"""
    include_routers(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    