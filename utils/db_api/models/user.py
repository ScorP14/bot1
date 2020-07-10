import datetime
from peewee import *

from data.config import db
from main import logger
from utils.db_api.utility_for_db import get_one_day_data_for_db, get_month_data_for_db


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

    @staticmethod
    def check_for_user(id_tg):
        user = User.get_or_none(id_tg)
        if user:
            return True
        return False

    @staticmethod
    def select_one_month_by_date(year, month):
        start, end = get_month_data_for_db(year, month)
        sel = User.select().where(User.date_add.between(start, end)).order_by(User.date_add)
        return sel

    @staticmethod
    def select_one_day_by_date(year, month, day):
        start, end = get_one_day_data_for_db(year, month, day)
        print(start, end)
        sel = User.select().where(User.date_add.between(start, end)).order_by(User.date_add)
        return sel

    @staticmethod
    def get_user(id_tg):
        return User.get_or_none(id_tg)

    @staticmethod
    def swap_sub(id_tg):
        user = User.get_or_none(id_tg)
        if user.sub:
            user.sub = False
            user.save(only=[User.sub])
            return user.sub
        user.sub = True
        user.save(only=[User.sub])
        return user.sub

    @staticmethod
    def check_for_user_sub(id_tg):
        try:
            User.select().where(User.telegram_id == id_tg, User.sub == True).get()
            return True
        except DoesNotExist:
            return False

    @staticmethod
    def add_user(id_tg, name, sub=False):
        user = User.get_or_none(id_tg)
        if user:
            return user, False
        user = User.create(telegram_id=id_tg, name=name, sub=sub)
        logger.info(f'Пользователь создан: {id_tg}-{name}, {user}')
        return user, True

    @staticmethod
    def del_user(id_tg):
        user = User.get_or_none(id_tg)
        if user:
            user.delete_by_id(id_tg)
            logger.info(f'Пользователь удален: {user} в {datetime.datetime.now()}')
            return True
        return False

    @staticmethod
    def select_all_user():
        sel = User.select()
        for i in sel:
            print(i)

