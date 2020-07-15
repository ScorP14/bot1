from aiogram.dispatcher.filters.state import StatesGroup, State


class StateAddExpenses(StatesGroup):
    state_category = State()