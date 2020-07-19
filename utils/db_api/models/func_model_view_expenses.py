from utils.db_api.models.func_model_categories import get_category_from_str
from utils.db_api.models.models import ViewExpenses, Categories, Expenses, DoesNotExist


def get_name_expenses_from_category_generator(category: Categories):
    """Генератор видов расходов"""
    sel = ViewExpenses.select(ViewExpenses.name_expense).\
        where(ViewExpenses.category == category).\
        order_by(ViewExpenses.name_expense)
    for i in sel:
        yield i.name_expense


def get_name_expenses_from_category(category):
    sel = ViewExpenses.select(ViewExpenses.name_expense).\
        where(ViewExpenses.category == category).\
        order_by(ViewExpenses.name_expense)
    return sel


def get_count_expenses_for_paginator(category: Categories) -> int:
    count = ViewExpenses.select(ViewExpenses.name_expense).where(ViewExpenses.category == category).count()
    return count


def get_name_expenses_from_category_paginator(category: Categories, page: int, count_page: int = 8):
    """Пагинатор видов расходов"""
    count = ViewExpenses.select(ViewExpenses.name_expense).where(ViewExpenses.category == category).count()
    sel = ViewExpenses.select(ViewExpenses.name_expense)\
        .where(ViewExpenses.category == category)\
        .paginate(page, count_page)\
        .order_by(ViewExpenses.name_expense)
    for i in sel:
        yield i.name_expense


def search_name_expenses_in_db(text: str) -> ViewExpenses or False:
    try:
        sel = ViewExpenses.get(ViewExpenses.name_expense == text)
    except DoesNotExist:
        return False
    return sel


def get_name_expense_from_category(category: Categories, text: str) -> str or False:
    try:
        select = ViewExpenses.select(ViewExpenses.name_expense).where(
            (ViewExpenses.category == category) & (ViewExpenses.name_expense == text.title())).get()
        return select.name_expense
    except DoesNotExist:
        return False


def add_the_categories_expenses(category: str, name_expense: str):
    categ = get_category_from_str(category)
    name = get_name_expense_from_category(categ, name_expense)
    print(name)

    # for i in asd:
    #     ViewExpenses.create(category=categ, name_expense=i.title())



