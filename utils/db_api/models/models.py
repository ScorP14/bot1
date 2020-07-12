import datetime
from math import ceil

from peewee import Model, IntegerField, CharField, DateTimeField, BooleanField, DoesNotExist, PrimaryKeyField, \
    ForeignKeyField, FloatField, TextField

from data.config import db
from setup import logger
from utils.db_api.utility_for_db import get_one_day_data_for_db, parse_text_for_expenses


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
    main_category = BooleanField(verbose_name='Основной расход?', default=False)
    aliases = TextField(verbose_name='Ключи')

    class Meta:
        database = db
        order_be = ('category',)

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
