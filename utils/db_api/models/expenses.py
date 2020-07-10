import datetime

from peewee import *

from data.config import db
from utils.db_api.models.categories import Categories
from utils.db_api.models.user import User
from utils.db_api.utility_for_db import parse_text_for_expenses


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

    @staticmethod
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