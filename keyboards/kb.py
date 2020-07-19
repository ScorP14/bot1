from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from utils.db_api.models.models import Users


def get_keyboard(id_tg):
    user = Users.get_or_none(id_tg)
    if not user:
        user = Users()
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
        [
            KeyboardButton('/help'),
            KeyboardButton('/check'),
            KeyboardButton('/add') if not user.telegram_id else KeyboardButton('/del'),
            KeyboardButton('/subt') if not user.sub else KeyboardButton('/subf')
        ], [KeyboardButton('Cancel')]])
    return kb



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
