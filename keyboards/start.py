"""Клавиатура с работай с коммандой start"""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
kb_start = InlineKeyboardMarkup(inline_keyboard=[
        [   InlineKeyboardButton(text='История', callback_data='history'),
            InlineKeyboardButton(text='Понравившиеся аниме',callback_data='anime')]])
kb_start_next_history = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Отсортировать по дате', callback_data='sort')],
        [InlineKeyboardButton(text='Назад', callback_data='back')]])
kb_start_error = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Хоз работы', callback_data='work')],
        [InlineKeyboardButton(text='Уйти', callback_data='back1')]])
kb_start_end = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Не нажимай больше сюда',callback_data='work')],
        [InlineKeyboardButton(text='А всё!', callback_data='stop')]])
kb_start_anime = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text='Этот замечательный мир! 3',
    url='https://animego.org/anime/etot-zamechatelnyy-mir-3-2538',
    callback_data='Animego')],
        [InlineKeyboardButton(text='Назад', callback_data='back')]])
kb_start_back_1 = InlineKeyboardMarkup(inline_keyboard=[
        [   InlineKeyboardButton(text='История', callback_data='history'),
            InlineKeyboardButton(text='Понравившиеся аниме',callback_data='anime')]])
kb_start_back_2 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Отсортировать по дате', callback_data='sort')],
        [InlineKeyboardButton(text='Назад', callback_data='back')]])
