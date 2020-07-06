from aiogram import types

from utils.db_api.main_db import check_for_user, User


def identification(func):
    async def decor(mes: types.Message):
        user = check_for_user(mes.from_user.id)
        if user:
            await func(mes)
        else:
            return await mes.answer('Вы не User')
    return decor


def not_identification(func):
    async def decor(mes: types.Message):
        user = check_for_user(mes.from_user.id)
        if not user:
            await func(mes)
        else:
            return await mes.answer('Вы User')
    return decor


def subscriber(func):
    async def decor(mes: types.Message):
        user = User.get(User.telegram_id == mes.from_user.id)
        if user.sub:
            await func(mes)
        else:
            return await mes.answer('User no SUB')
    return decor


def not_subscriber(func):
    async def decor(mes: types.Message):
        user = User.get(User.telegram_id == mes.from_user.id)
        if not user.sub:
            await func(mes)
        else:
            return await mes.answer('User SUB')
    return decor

