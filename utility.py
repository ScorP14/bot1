from aiogram import types
from db.main_db import check_for_user


def auit(func):
    async def decor(mes: types.Message):
        check = check_for_user(mes.from_user.id)
        if check:
            await func(mes)
        else:
            return await mes.answer('Доступ закрыт')
    return decor





