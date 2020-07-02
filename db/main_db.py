from peewee import *
import datetime
from config import DB_DIR


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
    categor = CharField(max_length=255, primary_key=True, unique=True, verbose_name='Категорая')
    main_categor = BooleanField()
    aliases = TextField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.telegram_id}: {self.name} {self.sub}, {self.date_add}'


def check_for_user(id_tg):
    try:
        User.select().where(User.telegram_id == id_tg).get()
        return True
    except DoesNotExist:
        return False


def get_user_by_id(id_tg):
    try:
        user = User.select().where(User.telegram_id == id_tg).get()
    except:
        return False
    return user


def sub_user_true(id_tg):
    user = get_user_by_id(id_tg)
    if user:
        user.sub = True
        user.save()
        return user
    return False


def sub_user_false(id_tg):
    user = get_user_by_id(id_tg)
    if user:
        user.sub = False
        user.save()
        return user
    return False


def check_for_user_sub(id_tg):
    try:
        User.select().where(User.telegram_id == id_tg, User.sub is True).get()
        return True
    except DoesNotExist:
        return False


def add_user(id_tg, name):
    User.create(telegram_id=id_tg, name=name)
    return True


def del_user(id_tg):
    User.delete_by_id(id_tg)


def select_all():
    sel = User.select()
    for i in sel:
        print(i)

"""
547865: Вася_4 False, 2020-06-30 20:46:12.118072
555974: Вася_13 False, 2020-06-30 20:46:12.118072
655629: Вася_12 False, 2020-06-30 20:46:12.118072
670480: Вася_7 False, 2020-06-30 20:46:12.118072
813745: Вася_11 False, 2020-06-30 20:46:12.118072
555974: Вася_8 False, 2020-06-30 20:46:12.118072
924850: Вася_9 False, 2020-06-30 20:46:12.11807
"""