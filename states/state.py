from aiogram.dispatcher.filters.state import StatesGroup, State


class StateAddExpenses(StatesGroup):
    state_category = State()


class StateAddExpensesCheque(StatesGroup):
    state_category = State()
    state_message = State()
