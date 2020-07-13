from utils.db_api.models.func_model_categories import get_category_from_str
from utils.db_api.models.models import ViewExpenses, Categories, Expenses, DoesNotExist


def get_name_expenses_from_category_generator(category: Categories):
    """Генератор видов расходов"""
    sel = ViewExpenses.select(ViewExpenses.name_expense).where(ViewExpenses.category == category)
    for i in sel:
        yield i.name_expense


def get_name_expense_from_category(category: Categories, text: str) -> ViewExpenses or False:
    try:
        select = ViewExpenses.select(ViewExpenses.name_expense).where(
            (ViewExpenses.category == category) & (ViewExpenses.name_expense == text.title())).get()
        return select.name_expense
    except DoesNotExist:
        return False

