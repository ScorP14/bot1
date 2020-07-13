import datetime
from math import ceil

from peewee import DoesNotExist

from setup import logger
from utils.db_api.models.models import Users


def get_user(id_tg: int) -> Users or None:
    return Users.get_or_none(id_tg)



def swap_sub(id_tg):
    user = Users.get_or_none(id_tg)
    if user.sub:
        user.sub = False
        user.save(only=[Users.sub])
        return user.sub
    user.sub = True
    user.save(only=[Users.sub])
    return user.sub


def check_for_user_sub(id_tg):
    try:
        Users.select().where(Users.telegram_id == id_tg, Users.sub >> True).get()
        return True
    except DoesNotExist:
        return False


def add_user(id_tg, name, sub=False):
    user = Users.get_or_none(id_tg)
    if user:
        return user
    user = Users.create(telegram_id=id_tg, name=name, sub=sub)
    logger.info(f'Пользователь создан: {id_tg}-{name}, {user}')
    return user


def del_user(id_tg):
    user = Users.get_or_none(id_tg)
    if user:
        user.delete_by_id(id_tg)
        logger.info(f'Пользователь удален: {user} в {datetime.datetime.now()}')
        return True
    return False


def select_all_user():
    sel = Users.select().order_by(Users.telegram_id)
    print(sel)
    for i in sel:
        print(i)


def paginater(page, per_page):
    total_count = Users.select(Users.telegram_id).order_by(Users.telegram_id).count()
    pagsss = int(ceil(total_count / float(per_page)))
    print(f'Page - {page}, Pages - {pagsss}, Per Page - {per_page}, COUNT - {total_count}')
    if page > pagsss:
        return 'много'
    return [i for i in Users.select().paginate(page, per_page)]