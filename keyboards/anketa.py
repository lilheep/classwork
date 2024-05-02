"""Клавиатура для команды anketa"""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
apteke = InlineKeyboardMarkup(inline_keyboard=[[ InlineKeyboardButton(text='Отмена',
                                                                      callback_data='cancel')]])
