import requests

url = "https://api.chucknorris.io/jokes/random"
print(url)  # выводим на печать URL, по которому отправляем запрос
result = requests.get(url)
print("Статус код: " + str(result.status_code))
assert 200 == result.status_code, f"Ошибка! Статус код: {result.status_code}"  # проводим проверку статус кода запроса
print("Успешно, статус код верен!")
result.encoding = "utf-8"  # приводим ответ к правильному виду благодаря указанию кодировки
print(result.text)