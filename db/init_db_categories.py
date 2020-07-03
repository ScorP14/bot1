import json

from db.main_db import Categories

file = 'categories.json'

with open(file, encoding="utf-8") as f:
    templates = json.load(f)

# print(templates['categories'])
dic = templates['categories']
for vul in dic.values():
    get_name = vul['name']
    get_aliasses = vul['aliases']
    get_main = vul['main']
    #cat = Categories.create(category=get_name, main_category=get_main, aliases=get_aliasses)
