from aiogram import types

from utils.db_api.models.user import User


def identification(func):
    async def decor(mes: types.Message):
        user = User.check_for_user(mes.from_user.id)
        if user:
            await func(mes)
        else:
            return await mes.answer('Вы не User')
    return decor


def not_identification(func):
    async def decor(mes: types.Message):
        user = User.check_for_user(mes.from_user.id)
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





def test_decor(func):
    async def decor(query: types.CallbackQuery, callback_data: dict):
        print(query.data)
        print(callback_data)

        await func(query)
    return decor