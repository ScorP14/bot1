from utils.db_api.models.models import Categories


def get_list_categories() -> list:
    cat = Categories.select()
    list_categories = [i.category for i in cat]
    return list_categories


def select_all_category():
    sel = Categories.select()
    for i in sel:
        if i:
            print(i)