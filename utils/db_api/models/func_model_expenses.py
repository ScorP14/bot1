from utils.db_api.models.func_model_categories import get_category_from_str
from utils.db_api.models.func_model_user import get_user
from utils.db_api.models.func_model_view_expenses import get_name_expense_from_category
from utils.db_api.models.models import Users, Categories, Expenses, ViewExpenses
from utils.db_api.utility_for_db import parse_text_for_expenses, get_one_day_data_for_db


def add_expenses(id_tg: int, category: str, message: str, price: float, main: bool = False):
    user = get_user(id_tg)
    categ = get_category_from_str(category)
    view = get_name_expense_from_category(categ, message)
    if not user or not categ or not view:
        return False
    print(user.name, categ.category, view)
    Expenses.create(user=user, view_expense=view, price=price, main_expense=main)


for i in Expenses.select().where(Expenses.user == 468933460):
    print(f'''User:{i.user.name}, 
Расход: {i.view_expense.category}-{i.view_expense.name_expense} 
Main - {i.main_expense}, 
Data - {i.date_add}, 
Price - {i.price}
{i}''')



#add_expenses(468933460, 'ПродуКты', 'сыр', 300.50, True)


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
