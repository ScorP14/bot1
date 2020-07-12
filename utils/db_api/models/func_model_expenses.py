from utils.db_api.models.models import User, Categories, Expenses
from utils.db_api.utility_for_db import parse_text_for_expenses, get_one_day_data_for_db


def add_expenses(id_tg, mes):
    user = User.get_or_none(id_tg)
    cate = Categories.select()
    if not parse_text_for_expenses(mes):
        return False
    category, price = parse_text_for_expenses(mes)
    for i in cate:
        alias = i.aliases.lower().split()
        if category in alias:
            Expenses.create(user=user, category_id=i, price=price, text_mes=mes)
            break



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
