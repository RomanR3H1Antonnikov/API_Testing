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

        check_joke = result.json()
        joke_type = check_joke.get("categories")
        print(joke_type)

        joke_category = check_joke.get('categories')
        assert joke_category == [types], f"Категория несоответствует! Текущая категория: {joke_category}, ожидаемая: {types}"
        # проводим проверку на соответствие категории
        print("Тест прошёл успешно")

        the_joke = check_joke.get('value')
        assert "Chuck" in the_joke, f"Имя величайшего не содержится в шутке! Шутка: {the_joke}"  # Проверка содержания имени в шутке

        print(the_joke)  # Вывод шутки

start = TestCreateJoke()
start.test_create_random_joke()
