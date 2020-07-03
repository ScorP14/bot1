from peewee import *
import datetime

from peewee import logger

from config import DB_DIR


db = SqliteDatabase(DB_DIR)


class User(Model):
    telegram_id = IntegerField(unique=True, primary_key=True, verbose_name='ID_telegram')
    name = CharField(max_length=100, null=False, verbose_name='Имя')
    date_add = DateTimeField(default=datetime.datetime.now().strftime("%m/%d/%Y:%H.%M.%S"), verbose_name='Дата создания')
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

    def __str__(self):
        return f'{self.text_mes} - {self.user}: {self.price}'

us = User.get_or_none(343554)
ras = Expenses()









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


def sub_user_true(id_tg):
    user = User.get_or_none(id_tg)
    if user:
        user.sub = True
        user.save()
        return user
    return False


def sub_user_false(id_tg):
    user = User.get_or_none(id_tg)
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
        logger.info(f'Пользователь удален: {user} в {datetime.datetime.now()}')
        user.delete_by_id(id_tg)
        return True
    return False



us = User.get_or_none(468933460)
def asd():
    us = User.get_or_none(468933460)
    cate = Categories.select()
    mes = 'еда 2500'.lower()
    mes = mes.split()
    for i in cate:
        alias = i.aliases.lower().split()
        if mes[0] in alias:
            print(i.category)
            rashod = Expenses.create(user=us, category_id=i, price=float(mes[1]), text_mes=mes)
            print(True)
            break




ex = Expenses.select().get()
print(ex.user, ex.category)


"""
547865: Вася_4 False, 2020-06-30 20:46:12.118072
555974: Вася_13 False, 2020-06-30 20:46:12.118072
655629: Вася_12 False, 2020-06-30 20:46:12.118072
670480: Вася_7 False, 2020-06-30 20:46:12.118072
813745: Вася_11 False, 2020-06-30 20:46:12.118072
555974: Вася_8 False, 2020-06-30 20:46:12.118072
924850: Вася_9 False, 2020-06-30 20:46:12.11807
"""