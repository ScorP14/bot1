from aiogram import types

from main import dp


@dp.message_handler()
async def check(mes: types.Message):
    '''Ехо'''
    await mes.answer('echp last -' + mes.text)
