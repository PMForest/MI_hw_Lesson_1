"""Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
сохранить JSON-вывод в файле *.json."""

import requests
import json
url = 'https://api.github.com'
user = 'PMForest'
x = requests.get(f'{url}/users/{user}/repos')
with open('data.json', 'w') as f:
    json.dump(x.json(),f)
for i in x.json():
    print(i['name'])

