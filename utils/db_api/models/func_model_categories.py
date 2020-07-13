from utils.db_api.models.models import Categories


def get_list_categories() -> list:
    all_category = Categories.select()
    list_categories = [i.category for i in all_category]
    return list_categories


def select_all_category():
    sel = Categories.select()
    for i in sel:
        if i:
            print(i)
