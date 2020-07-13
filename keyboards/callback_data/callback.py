from aiogram.utils.callback_data import CallbackData

# Главное меню
cbd_menu = CallbackData('cbd_menu', 'key')
# Меню пользователя
cdb_menu_user = CallbackData('cdb_menu_user', 'key')
cdb_menu_user_sub = CallbackData('cdb_menu_user_sub', 'key')
cdb_user_sub_alert_mes = CallbackData('cdb_user_sub_alert_mes', 'answer')

# Меню категорий
cdb_menu_category = CallbackData('cdb_menu_category', 'key')


# Меню Расходов
cdb_menu_expenses = CallbackData('cdb_menu_expenses', 'key')




test_callback_data = CallbackData('test', 'key')
test_del_callback_data = CallbackData('del', 'key')