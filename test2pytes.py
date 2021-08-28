import json
import requests


def test_contre_code_kg():                                  # Код страны по фильтру "kg"
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=kg'
    response = requests.request('GET', url)
    data = (response.json())
    data = json.dumps(data)
    body = json.loads(data)
    li = []                                                 # пустой список li для значения country_code
    for item in body['items']:                              # цикл for по ключам ['country']['code']
        code = (item['country']['code'])
        li.append(code)
    i = 0                                                   # возвращает длину списка li
    while i < len(li):
        i += 1
    sample = li.count('kg')                                 # количество значений "kg" в списке li
    assert sample == i


test_contre_code_kg()

