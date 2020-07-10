from peewee import *

from data.config import db


class Categories(Model):
    category = CharField(max_length=255, primary_key=True, unique=True, verbose_name='Категорая')
    main_category = BooleanField(verbose_name='Основной расход?', default=False)
    aliases = TextField(verbose_name='Ключи')

    class Meta:
        database = db

    def __str__(self):
        return f'{self.category} - {self.main_category}: {self.aliases}'

    @staticmethod
    def get_list_categories():
        cat = Categories.select()
        list_categories = [i.category for i in cat]
        return list_categories

    @staticmethod
    def select_all_category():
        sel = Categories.select()
        for i in sel:
            if i.main_category:
                print(i)
