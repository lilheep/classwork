import asyncio

from aiogram import F, Bot, Dispatcher, Router
from aiogram.types import Message, BotCommand, KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardMarkup,\
    InlineKeyboardButton, CallbackQuery, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

#photo_start = 'Photo/AniVaultBotFinal.png'
bot = Bot(token="7151332549:AAHSjVhcer11nEWzBhDkwrjPPr9mRopvsAw")

dp = Dispatcher()
router = Router()

class Anketa(StatesGroup):
    name = State()
    age = State()
    anime_love = State()



@router.message(Command('info'))
async def  info_handler(msg: Message, state:FSMContext):
    await state.set_state(Anketa.name)
    markup = InlineKeyboardMarkup(inline_keyboard=[
       [ InlineKeyboardButton(text='Отмена', callback_data='cancel')]])
    await msg.answer('Введите ваше имя', reply_markup=markup)







@router.message(Command("start"))
async def start_handler(msg: Message):
    await bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='help', description='Справка'),
        BotCommand(command='delete', description='Отчислиться'),
    ])
    await msg.answer(text='Привет')

    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='История', callback_data='history'),
            InlineKeyboardButton(text='Понравившиеся аниме',callback_data='anime')
        ],
    ])
    await msg.answer(text='Добро пожаловать в мир аниме!', reply_markup=inline_markup)

@router.message(Command("help"))
async def help_handler(msg: Message):
    await msg.answer(text='тебе не поможет')


@router.callback_query(F.data == 'anime')
async def callback_query_handler(callback_query:CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Отсортировать по дате', callback_data='sort')],
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    await callback_query.message.edit_text(text='Страница 2', reply_markup=inline_markup)

@router.callback_query(F.data == 'back1')
async def callback_query_handler(callback_query:CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Отсортировать по дате', callback_data='sort')],
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    await callback_query.message.edit_text(text='Страница 2', reply_markup=inline_markup)
    
@router.callback_query(F.data == 'sort')
async def callback_query_handler(callback_query:CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Хоз работы', callback_data='work')],
        [InlineKeyboardButton(text='Уйти', callback_data='back1')]
    ])
    await callback_query.message.edit_text(text='Такого еще не завезли', reply_markup=inline_markup)

@router.callback_query(F.data == 'work')
async def callback_query_handler(callback_query:CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Не нажимай больше сюда',callback_data='work')],
        [InlineKeyboardButton(text='А всё!', callback_data='stop')]
    ])
    
    await callback_query.message.edit_text(text='Я же сказал, нету тут ничего ', reply_markup=inline_markup)


@router.callback_query(F.data == 'history')
async def callback_query_handler(callback_query:CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Этот замечательный мир! 3', callback_data='Animego')],
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])

    

    await callback_query.message.edit_text(text='Твои любимые аниме!', reply_markup=inline_markup)
    
@router.callback_query(F.data == 'back')
async def callback_query_handler(callback_query:CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
         [  InlineKeyboardButton(text='История', callback_data='history'),
            InlineKeyboardButton(text='Понравившиеся аниме',callback_data='anime')
         ]

    ])
    await callback_query.message.edit_text(text='Добро пожаловать в мир аниме', reply_markup=inline_markup)


@router.callback_query(F.data == '3')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.answer(text='Пока')

async def main():
    await dp.start_polling(bot)

dp.include_routers(router)

if __name__ == '__main__':
    asyncio.run(main())