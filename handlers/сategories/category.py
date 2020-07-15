from aiogram import types

from keyboards.callback_data.callback import cbd_menu, cdb_menu_category
from keyboards.in_line_keyboard.categories import get_kb_categories
from keyboards.in_line_keyboard.menu import in_kb_main
from setup import dp, bot


@dp.callback_query_handler(cbd_menu.filter(key='Category'))
async def menu_category(query: types.CallbackQuery):
    await query.answer()
    await bot.edit_message_text(
        f'Категории',
        query.from_user.id,
        query.message.message_id, reply_markup=get_kb_categories()
    )


@dp.callback_query_handler(cdb_menu_category.filter(key='Back'))
async def menu_category_back(query: types.CallbackQuery):
    await bot.edit_message_text('Главное меню',
                                query.from_user.id, query.message.message_id,
                                reply_markup=in_kb_main)


@dp.callback_query_handler(cdb_menu_category.filter(key='Exit'))
async def menu_category_exit(query: types.CallbackQuery):
    return await bot.edit_message_text('Досвидание :)',
                                       query.from_user.id, query.message.message_id)

