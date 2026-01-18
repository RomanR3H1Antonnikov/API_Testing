import requests

url = "https://official-joke-api.appspot.com/jokes/random"
print(url)
result = requests.get(url)
print("Статус код: " + str(result.status_code))
assert 200 == result.status_code, f"Ошибка! Статус код: {result.status_code}"  # проводим проверку статус кода запроса
if result.status_code == 200:
    print("Успешно, статус код верен!")
else:
    print("Провал, статус код неверен!")
result.encoding = "utf-8"  # приводим ответ к правильному виду благодаря указанию кодировки
print(result.text)