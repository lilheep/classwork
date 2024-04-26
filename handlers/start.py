from aiogram import F, Router
from aiogram.filters import Command 
from aiogram.types import BotCommand, Message, CallbackQuery
from keyboards.start import *


router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    from main import bot
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
    await callback_query.message.edit_text(text='Страница 2',
                                           reply_markup=kb_start_next_history)

@router.callback_query(F.data == 'back1')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.edit_text(text='Страница 2',
                                           reply_markup=kb_start_back_2)
    
@router.callback_query(F.data == 'sort')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.edit_text(text='Такого еще не завезли',
                                           reply_markup=kb_start_error)

@router.callback_query(F.data == 'work')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.edit_text(text='Я же сказал, нету тут ничего ',
                                           reply_markup=kb_start_end)


@router.callback_query(F.data == 'history')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.edit_text(text='Твои любимые аниме!',
                                           reply_markup=kb_start_anime)
    
@router.callback_query(F.data == 'back')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.edit_text(text='Добро пожаловать в мир аниме',
                                            reply_markup=kb_start_back_1)
