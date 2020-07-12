from utils.db_api.models.models import User, Categories, Expenses
from utils.db_api.utility_for_db import parse_text_for_expenses


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