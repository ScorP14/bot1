from aiogram import types

from utils.db_api.models.func_model_user import get_user
from utils.db_api.models.models import Users


def identification(func):
    async def decor(mes: types.Message):
        user = get_user(mes.from_user.id)
        if user:
            await func(mes)
        else:
            return await mes.answer('Вы не пользователь')
    return decor


def not_identification(func):
    async def decor(mes: types.Message):
        user = get_user(mes.from_user.id)
        if not user:
            await func(mes)
        else:
            return await mes.answer('Пользователь уже создан')
    return decor


def subscriber(func):
    async def decor(mes: types.Message):
        user = Users.get(Users.telegram_id == mes.from_user.id)
        if user.sub:
            await func(mes)
        else:
            return await mes.answer('Пользователь не подписан')
    return decor


def not_subscriber(func):
    async def decor(mes: types.Message):
        user = Users.get(Users.telegram_id == mes.from_user.id)
        if not user.sub:
            await func(mes)
        else:
            return await mes.answer('Пользователь подписан')
    return decor
