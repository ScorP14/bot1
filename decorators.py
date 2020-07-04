from aiogram import types
from db.main_db import check_for_user, User


def identification(func):
    async def decor(mes: types.Message):
        user = check_for_user(mes.from_user.id)
        if user:
            await func(mes)
        else:
            return await mes.answer('Доступ закрыт')
    return decor


def subscriber(func):
    async def decor(mes: types.Message):
        user = User.get(User.telegram_id == mes.from_user.id)
        if user.sub:
            await func(mes)
        else:
            return await mes.answer('Пользователь не подписан')
    return decor



