import requests


def test_country_code_kg():
    # Код страны по фильтру "ru"
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=ru'
    response = requests.get(url)
    # Проверка успешности запроса
    assert response.status_code == 200
    # Получение данных в формате JSON
    data = response.json()
    # Создание списка li для значения country_code
    li = [item['country']['code'] for item in data['items']]
    # Проверка, что количество значений "kg" равно длине списка li
    assert li.count('ru') == len(li)
    print("pass")


# Запуск теста
test_country_code_kg()
