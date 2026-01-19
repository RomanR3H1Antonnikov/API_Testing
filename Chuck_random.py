import requests


class TestCreateJoke:

    url = "https://api.chucknorris.io/jokes/random"

    def test_create_random_joke(self):

        types = 'dev'
        path_random_joke_general = f'?category={types}'
        url_random_joke_general = self.url + path_random_joke_general
        print(url_random_joke_general)

        result = requests.get(url_random_joke_general)
        print(result.json())

        print(f"Статус код: {result.status_code}")
        assert result.status_code == 200, f"Ошибка! Статус код: {result.status_code}"  # проводим проверку статус кода запроса
        print('Статус код корректен')

        check_joke = result.json()  # записываем ответ в формате json в переменную
        joke_type = check_joke.get("categories")  # записываем тип шутки в переменную joke_type
        the_joke = check_joke.get('value')  # записываем саму шутку в переменную the_joke

        print(joke_type)  # Вывод типа шутки

        assert joke_type == [types], f"Категория несоответствует! Текущая категория: {joke_type}, ожидаемая: {types}"
        # проводим проверку на соответствие категории
        print("Тест прошёл успешно")

        assert "Chuck" in the_joke, f"Имя величайшего не содержится в шутке! Шутка: {the_joke}"  # Проверка содержания имени в шутке

        print(the_joke)  # Вывод шутки

start = TestCreateJoke()
start.test_create_random_joke()
