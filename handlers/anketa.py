"""Обработка команды anketa"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.anketa import Anketa

from keyboards.anketa import apteke

router = Router()

@router.message(Command('info'))
async def  info_handler(msg: Message, state:FSMContext):
    """Запуск по команде """
    await state.set_state(Anketa.name)
    await msg.answer('Введите ваше имя', reply_markup=apteke)
