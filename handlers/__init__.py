"""Обработка всех router"""
from aiogram import Dispatcher
from handlers import anketa, start

def include_routers(dp: Dispatcher):
    """Запуск всех router"""
    dp.include_routers(start.router,anketa.router)
