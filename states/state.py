from aiogram.dispatcher.filters.state import State, StatesGroup

asd = {"id": "2014053875060353937",
       "from": {
           "id": 468933460, "is_bot": False, "first_name": "FaN", "last_name": "TiK", "username": "FaNaTiK123",
           "language_code": "ru"
       },
       "message": {
           "message_id": 1501, "from": {
               "id": 802097136, "is_bot": True, "first_name": "scorp_test", "username": "ScorP14_test_bot"
           },
           "chat": {
               "id": 468933460, "first_name": "FaN", "last_name": "TiK",
               "username": "FaNaTiK123", "type": "private"
           },
           "date": 1593879040, "text": "Главное меню", "reply_markup":
               {
                   "inline_keyboard": [
                       [
                           {"text": "Пользователь", "callback_data": "main_menu:User"},
                           {"text": "Категории", "callback_data": "main_menu:Category"}]
                       ,
                       [{"text": "Выход", "callback_data": "Cancel"}
                        ]
                   ]
               }
       },
       "chat_instance": "-3568473991813159236", "data": "main_menu:User"}
asd = {'@': 'main_menu', 'key': 'User'}
