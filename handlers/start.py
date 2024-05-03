"""Обработка команды start"""
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import BotCommand, Message, CallbackQuery
from keyboards.start import kb_start, kb_start_anime, kb_start_back_1, kb_start_back_2,\
      kb_start_end, kb_start_error, kb_start_next_history
from tokens import bot


router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    """Ипморт бота"""
    
    await bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='help', description='Справка'),
        BotCommand(command='delete', description='Отчислиться'),
    ])
    await msg.answer(text='Привет')
    await msg.answer(text='Добро пожаловать в мир аниме!',
                     reply_markup=kb_start)

@router.callback_query(F.data == 'anime')
async def callback_query_handler(callback_query:CallbackQuery):
    """ОБработка кнопки anime """
    await callback_query.message.edit_text(text='Страница 2',
                                           reply_markup=kb_start_next_history)

@router.callback_query(F.data == 'back1')
async def callback_query_handler1(callback_query:CallbackQuery):
    """Обработка кнопки back1"""
    await callback_query.message.edit_text(text='Страница 2',
                                           reply_markup=kb_start_back_2)
@router.callback_query(F.data == 'sort')
async def callback_query_handler2(callback_query:CallbackQuery):
    """Обработка кнопки sort"""
    await callback_query.message.edit_text(text='Такого еще не завезли',
                                           reply_markup=kb_start_error)
@router.callback_query(F.data == 'work')
async def callback_query_handler3(callback_query:CallbackQuery):
    """Обработка кнопки work"""
    await callback_query.message.edit_text(text='Я же сказал, нету тут ничего ',
                                           reply_markup=kb_start_end)
@router.callback_query(F.data == 'history')
async def callback_query_handler4(callback_query:CallbackQuery):
    """Обработка кнопки history"""
    await callback_query.message.edit_text(text='Твои любимые аниме!',
                                           reply_markup=kb_start_anime)
@router.callback_query(F.data == 'back')
async def callback_query_handler5(callback_query:CallbackQuery):
    """Обработка кнопки back"""
    await callback_query.message.edit_text(text='Добро пожаловать в мир аниме',
                                            reply_markup=kb_start_back_1)
