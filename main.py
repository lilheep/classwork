import asyncio

from aiogram import  Bot, Dispatcher
from handlers import include_routers

bot = Bot(token="7151332549:AAHSjVhcer11nEWzBhDkwrjPPr9mRopvsAw")

dp = Dispatcher()



async def main():
    include_routers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())