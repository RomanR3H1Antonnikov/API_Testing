import requests


class TestCreateJokeCategory:

    url = "https://api.chucknorris.io/jokes/random"

    def test_create_random_joke_positive(self, category, expected_status_code):
        path_random_joke_category = f'?category={category}'
        url_random_jake_category = self.url + path_random_joke_category
        print(url_random_jake_category)

        result = requests.get(url_random_jake_category)
        print(result.json())

        result_status_code = result.status_code
        print(f"Статус-код: {result_status_code}")
        assert result_status_code == expected_status_code, (f"Статус-код некорректен!"
            f" Ожидаемый статус-код: {expected_status_code}, полученный: {result_status_code}")
        print("Статус-код корректен!")

        check_joke = result.json()
        joke_value = check_joke.get('value')
        print(joke_value)

        joke_category = check_joke.get('categories')
        print(joke_category)
        assert joke_category[0] == category, (f"Категория некорректна,"
            f" ожидаемая категория: {category}, полученная: {joke_category[0]}")
        print("Категория корректна!")

        print("Тест прошёл успешно!")



    def test_create_random_joke_negative(self, category, expected_status_code):
        path_random_joke_category = f'?category={category}'
        url_random_jake_category = self.url + path_random_joke_category
        print(url_random_jake_category)

        result = requests.get(url_random_jake_category)
        print(result.json())

        result_status_code = result.status_code
        print(f"Статус-код: {result_status_code}")
        assert result_status_code == expected_status_code, (f"Статус-код некорректен!"
            f" Ожидаемый статус-код: {expected_status_code}, полученный: {result_status_code}")
        print("Статус-код корректен!")

        check_joke = result.json()
        print(check_joke)

        error = check_joke.get('error')
        print(error)
        assert error == "Not Found"
        print("Поле Errror корректно")

        print("Тест прошёл успешно!")




start = TestCreateJokeCategory()
start.test_create_random_joke_positive("animal", 200)
start.test_create_random_joke_positive("career", 200)
start.test_create_random_joke_positive("celebrity", 200)
start.test_create_random_joke_positive("dev", 200)
start.test_create_random_joke_positive("explicit", 200)
start.test_create_random_joke_positive("fashion", 200)
start.test_create_random_joke_positive("food", 200)
start.test_create_random_joke_positive("history", 200)
start.test_create_random_joke_positive("money", 200)
start.test_create_random_joke_positive("movie", 200)
start.test_create_random_joke_positive("music", 200)
start.test_create_random_joke_positive("political", 200)
start.test_create_random_joke_positive("religion", 200)
start.test_create_random_joke_positive("science", 200)
start.test_create_random_joke_positive("sport", 200)
start.test_create_random_joke_positive("travel", 200)
start.test_create_random_joke_negative("hello", 404)
print("Тест прошёл успешно")