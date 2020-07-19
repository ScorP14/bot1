import math
from math import ceil

from aiogram.dispatcher.filters.state import StatesGroup, State

from utils.db_api.models.func_model_view_expenses import get_name_expenses_from_category
from utils.db_api.models.models import Users, ViewExpenses


class StateAddExpenses(StatesGroup):
    state_category = State()


class StateAddExpensesCheque(StatesGroup):
    state_category = State()
    state_message = State()


class PaginatorForExpenses(StatesGroup):
    paginator = None
    page = None
    St1 = State()
    St2 = State()

