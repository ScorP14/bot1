from utils.db_api.models.func_model_categories import get_category_from_str
from utils.db_api.models.func_model_user import get_user
from utils.db_api.models.func_model_view_expenses import get_name_expense_from_category, search_name_expenses_in_db
from utils.db_api.models.models import Expenses, Categories, ViewExpenses
from utils.db_api.utility_for_db import get_one_day_data_for_db


def add_expenses(id_tg: int, name_exp: ViewExpenses, price: float, main: bool = False):
    user = get_user(id_tg)
    view_ex = search_name_expenses_in_db(name_exp)
    if not user:
        return False
    Expenses.create(user=user, view_expense=view_ex.name_expense, price=price, main_expense=main)
    return True


def view_expenses(id_tg: int, main=False):
    user = get_user(id_tg)
    epens = Expenses.select().where(Expenses.user == user)
    if main:
        epens = Expenses.select().where((Expenses.user == user)& (Expenses.main_expense >> main))
    for i in epens:
        yield i



def select_all():
    exp = Expenses.select()
    for i in exp:
        print(i)


def test():
    """Считает среднее за день, неделю, месяц, год"""
    start, end = get_one_day_data_for_db(2020, 8, 10)
    print(start, '-----------', end)
    sel = Expenses\
        .select(Expenses.price, Expenses.date_add)\
        .where(Expenses.date_add.between(start, end))\
        .order_by(Expenses.date_add)
    temp = 0.0
    for i in sel:
        temp += i.price
        print(i.date_add, i.price)
    print('Всреднем... вы пробухали -', temp/len(sel))
    print(temp, '=====', temp/len(sel))
