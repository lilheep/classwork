"""Машинное сотояние"""
from aiogram.fsm.state import State, StatesGroup
class Anketa(StatesGroup):
    """Класс машинного стояния"""
    name = State()
    age = State()
    anime_love = State()
