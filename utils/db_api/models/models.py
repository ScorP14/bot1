import datetime
import random
from math import ceil
from peewee import *

from data.config import db


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    telegram_id = IntegerField(primary_key=True, unique=True, verbose_name='ID')
    name = CharField(max_length=255, verbose_name='Имя',null=True)
    date_add = DateTimeField(default=datetime.datetime.now(), verbose_name='Дата')
    sub = BooleanField(default=False, verbose_name='Подсписка')

    class Meta:
        order_be = ('date_add',)


class Categories(BaseModel):
    category = CharField(primary_key=True, unique=True, verbose_name='Категория')


class ViewExpenses(BaseModel):
    category = ForeignKeyField(Categories, related_name='view_expenses')
    name_expense = CharField(max_length=255, verbose_name='Расход', null=False, unique=True)


class Expenses(BaseModel):
    user = ForeignKeyField(Users, related_name='expenses', verbose_name='Пользователь')
    view_expense = ForeignKeyField(ViewExpenses, related_name='expenses', verbose_name='Вид расхода')
    main_expense = BooleanField(default=False, verbose_name='Основной расход?')
    date_add = DateTimeField(default=datetime.datetime.now(), verbose_name='Дата расхода')
    price = FloatField(verbose_name='Цена', null=False)

    class Meta:
        order_be = ('date_add',)



def add_exp():
    user = Users.get_by_id(7594222)
    view = random.choice(ViewExpenses.select())
    main = random.choice([True, False])
    sss = random.randint(10, 2000)
    Expenses.create(user=user, view_expense=view, main_expense=main, price=sss)


# -----------------Шпаргалки --------------------------------------------------------
# for i in Expenses.select():
#     print(f'Main - {i.main_expense}, \n'
#           f'Data - {i.date_add},\n'
#           f'рублей - {i.price}\n'
#           f'{i.view_expense.category}-{i.view_expense.name_expense},\n\n')

# def asd():
#
#     cat = Categories.select().where(Categories.category == 'Продукты')
#     vie = ViewExpenses.select().where(ViewExpenses.category == cat)
#     for i in vie:
#         print(i.name_expense)
#
#
#
#     for i in Expenses.select().where(Expenses.view_expense << vie):
#         print(f'рублей - {i.price}\n'
#               f'{i.view_expense.category}-{i.view_expense.name_expense}\n')
#
# asd()
'''
448236
1269236
2156161
2810235
3819591
4418592
4736411
7594222
7676783
8682489
8710810
'''

"""
==	x equals y
<	x is less than y
<=	x is less than or equal to y
>	x is greater than y
>=	x is greater than or equal to y
!=	x is not equal to y
<<	x IN y, where y is a list or query
>>	x IS y, where y is None/NULL
%	x LIKE y where y may contain wildcards
**	x ILIKE y where y may contain wildcards
^	x XOR y
~	Unary negation (e.g., NOT x)
"""