import os

from peewee import SqliteDatabase

API_TOKEN = '802097136:AAGIr2s_5ZbiCSyV0qsZmdihsLjGHQRiQuk'
ADMIN = 468933460


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB = r'\utils\db_api\db\main.db'
DB_DIR = f'{BASE_DIR}{DB}'


db = SqliteDatabase(DB_DIR)

