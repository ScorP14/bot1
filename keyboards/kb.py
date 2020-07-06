from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from utils.db_api.main_db import User, get_10user


def get_keyboard(id_tg):
    user = User.get_or_none(id_tg)
    if not user:
        user = User()
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
        [
            KeyboardButton('/help'),
            KeyboardButton('/check'),
            KeyboardButton('/add') if not user.telegram_id else KeyboardButton('/del'),
            KeyboardButton('/subt') if not user.sub else KeyboardButton('/subf')
        ], [KeyboardButton('Cancel')]])
    return kb


test_mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
    [
        KeyboardButton(text='/add'),
        KeyboardButton(text='/del'),
        KeyboardButton(text='/sub'),
        KeyboardButton(text='/check'),
    ],
    [
        KeyboardButton(text='/cancel')
    ]
])

'''Callback_data------------------------'''
main_callback_data = CallbackData('main_menu', 'key')
main_user_callback_data = CallbackData('main_menu_user', 'key')
main_category_callback_data = CallbackData('main_menu_category', 'key')

inline_keyboard_main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Пользователь',
                             callback_data=main_callback_data.new(key='User')),
        InlineKeyboardButton(text='Категории', callback_data='main_menu:Category'),
    ],
    [
        InlineKeyboardButton(text='Выход', callback_data='Cancel')
    ]
])

inline_keyboard_main_user = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Стать пользователем?)', callback_data=main_user_callback_data.new(key='Add')),
        InlineKeyboardButton(text='Перестать быть польз.:(', callback_data='main_menu_user:Del'),
    ],
    [
        InlineKeyboardButton(text='Подписаться', callback_data=main_user_callback_data.new(key='Sub')),
        InlineKeyboardButton(text='Отписаться', callback_data='main_menu_user:Del_Sub'),
    ]
    ,
    [
        InlineKeyboardButton(text='Выход', callback_data='Cancel')
    ]
])


inline_keyboard_main_category = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Все расходы', callback_data=main_user_callback_data.new(key='Add')),
        InlineKeyboardButton(text='Перестать быть польз.:(', callback_data='main_menu_user:Del'),
        InlineKeyboardButton(text='Последние 5 расходов', callback_data='main_menu_user:Del'),
    ],
    [
        InlineKeyboardButton(text='Расход за день', callback_data=main_user_callback_data.new(key='Sub')),
        InlineKeyboardButton(text='Расход за неделю', callback_data='main_menu_user:Del_Sub'),
        InlineKeyboardButton(text='Расход за месяц', callback_data='main_menu_user:Del_Sub'),
        InlineKeyboardButton(text='Расход за год', callback_data='main_menu_user:Del_Sub'),
    ]
    ,
    [
        InlineKeyboardButton(text='Выход', callback_data='Cancel')
    ]
])

test_callback_data = CallbackData('test', 'key')
test_del_callback_data = CallbackData('del', 'key')


def get_kb_test():
    keyboard = InlineKeyboardMarkup(row_width=1).add(
        *[
            InlineKeyboardButton(
            text=f'{user.telegram_id}: {user.name}, {user.date_add.strftime("%d/%m/%Y:%H-%M-%S")}',
            callback_data=test_del_callback_data.new(key=user.telegram_id))
            for user in get_10user()
        ]
    )
    return keyboard

'''
test_cb = CallbackData('post', 'action')

kb = types.InlineKeyboardMarkup().row(
    types.InlineKeyboardButton('OK', callback_data=test_cb.new(action='OK')),
    types.InlineKeyboardButton('NO', callback_data=test_cb.new(action='NO'))
)




@dp.message_handler(commands=['start'])
async def test_func(message: types.Message):
    like_an = likes.get(message.from_user.id, 0)
    print(likes)
    await message.reply(f'Vote! You have {like_an} votes now.', reply_markup=kb)


@dp.callback_query_handler(test_cb.filter(action=['OK', 'NO']))
async def callback_vote_action(query: types.CallbackQuery, callback_data: dict):
    print(callback_data)
    print(query)
    await query.answer()
    callback_data_action = callback_data['action']
    print(callback_data_action)
    likes_count = likes.get(query.from_user.id, 0)

    if callback_data_action == 'OK':
        likes_count += 1
    else:
        likes_count -= 1

    likes[query.from_user.id] = likes_count  # update amount of likes in storage

    await bot.edit_message_text(
        f'You voted {callback_data_action}! Now you have {likes_count} vote[s].',
        query.from_user.id,
        query.message.message_id,
        reply_markup=kb,
    )





@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    # default row_width is 3, so here we can omit it actually
    # kept for clearness

    text_and_data = (
        ('Yes!', 'yes'),
        ('No!', 'no'),
    )
    # in real life for the callback_data the callback data factory should be used
    # here the raw string is used for the simplicity
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)

    keyboard_markup.row(*row_btns)
    keyboard_markup.add(
        # url buttons have no callback data
        types.InlineKeyboardButton('aiogram source', url='https://github.com/aiogram/aiogram'),
    )

    await message.reply("Hi!\nDo you love aiogram?", reply_markup=keyboard_markup)


# Use multiple registrators. Handler will execute when one of the filters is OK
@dp.callback_query_handler(text='no')  # if cb.data == 'no'
@dp.callback_query_handler(text='yes')  # if cb.data == 'yes'
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    # always answer callback queries, even if you have nothing to say
    await query.answer(f'You answered with {answer_data!r}')

    if answer_data == 'yes':
        text = 'Great, me too!'
    elif answer_data == 'no':
        text = 'Oh no...Why so?'
    else:
        text = f'Unexpected callback data {answer_data!r}!'

    await bot.send_message(query.from_user.id, text)

'''
