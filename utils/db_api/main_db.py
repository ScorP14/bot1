from utils.db_api.models.models import Expenses
from utils.db_api.utility_for_db import get_one_day_data_for_db


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