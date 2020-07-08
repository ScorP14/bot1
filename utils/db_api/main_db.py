from peewee import *
import datetime

from peewee import logger

from data.config import DB_DIR
from utils.db_api.utility_for_db import get_one_day_data_for_db, get_month_data_for_db, parse_text_for_expenses

db = SqliteDatabase(DB_DIR)


class User(Model):
    telegram_id = IntegerField(unique=True, primary_key=True, verbose_name='ID_telegram')
    name = CharField(max_length=100, null=False, verbose_name='Имя')
    date_add = DateTimeField(default=datetime.datetime.now(), verbose_name='Дата создания')
    sub = BooleanField(default=False, verbose_name='Подсписка')

    class Meta:
        database = db
        order_be = ('date_add',)

    def __str__(self):
        return f'{self.telegram_id}: {self.name} {self.sub}, {self.date_add}'


class Categories(Model):
    category = CharField(max_length=255, primary_key=True, unique=True, verbose_name='Категорая')
    main_category = BooleanField(verbose_name='Основной расход?')
    aliases = TextField(verbose_name='Ключи')

    class Meta:
        database = db

    def __str__(self):
        return f'{self.category} - {self.main_category}: {self.aliases}'



class Expenses(Model):
    id = PrimaryKeyField(null=False)
    user = ForeignKeyField(User, related_name='expenses')
    category = ForeignKeyField(Categories, related_name='category')
    text_mes = CharField(max_length=255, verbose_name='Сообщение')
    date_add = DateTimeField(default=datetime.datetime.now(), verbose_name='Дата рассхода')
    price = FloatField(verbose_name='Цена')

    class Meta:
        database = db
        order_be = ('date_add',)

    def __str__(self):
        return f'{self.id}-{self.user.telegram_id}: {self.category}_{self.price}_{self.date_add}_{self.text_mes}'








def select_all_category():
    sel = Categories.select()
    for i in sel:
        if i.main_category:
            print(i)



def select_all_user():
    sel = User.select()
    for i in sel:
        print(i)


def get_user(id_tg):
    return User.get_or_none(id_tg)


def check_for_user(id_tg):
    user = User.get_or_none(id_tg)
    if user:
        return True
    return False


def swap_sub(id_tg):
    user = User.get_or_none(id_tg)
    if user.sub:
        user.sub = False
        user.save(only=[User.sub])
        return user.sub
    user.sub = True
    user.save(only=[User.sub])
    return user.sub


def check_for_user_sub(id_tg):
    try:
        User.select().where(User.telegram_id == id_tg, User.sub is True).get()
        return True
    except DoesNotExist:
        return False


def add_user(id_tg, name, sub=False):
    user = User.get_or_none(id_tg)
    if user:
        return user, False
    user = User.create(telegram_id=id_tg, name=name, sub=sub)
    logger.info(f'Пользователь создан: {id_tg}-{name}, {user}')
    return user, True


def del_user(id_tg):
    user = User.get_or_none(id_tg)
    if user:
        user.delete_by_id(id_tg)
        logger.info(f'Пользователь удален: {user} в {datetime.datetime.now()}')
        return True
    return False


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


def test():
    user = get_user(956608146)
    ex = Expenses.select().where(Expenses.user == user)
    a = []
    for i in ex:
        a.append(f'{i.user.telegram_id}: {i.category.category}(Важные - {i.category.main_category}). Текст сообщения - {i.text_mes}')
    return a

  # id = PrimaryKeyField(null=False)
  #   user = ForeignKeyField(User, related_name='expenses')
  #   category = ForeignKeyField(Categories, related_name='category')
  #   text_mes = CharField(max_length=255, verbose_name='Сообщение')
  #   date_add = DateTimeField(default=datetime.datetime.now(), verbose_name='Дата рассхода')
  #   price = FloatField(verbose_name='Цена')


















def select_one_month_by_date(year, month):
    start, end = get_month_data_for_db(year, month)
    sel = User.select().where(User.date_add.between(start, end)).order_by(User.date_add)
    return sel


def select_one_day_by_date(year, month, day):
    start, end = get_one_day_data_for_db(year, month, day)
    print(start, end)
    sel = User.select().where(User.date_add.between(start, end)).order_by(User.date_add)
    return sel

