import requests


class TestCreateJokeCategory:

    url = "https://api.chucknorris.io/jokes/random"
    joke_category_list = [
    "animal",
    "career",
    "celebrity",
    "dev",
    "explicit",
    "fashion",
    "food",
    "history",
    "money",
    "movie",
    "music",
    "political",
    "religion",
    "science",
    "sport",
    "travel"
    ]

    def start_question(self):
        print("Введите категорию, на которую вы хотите получить шутку:")
        category = input()
        rez_list = []
        for x in range(len(self.joke_category_list)):
            rez_list.append(start.test_create_random_joke_positive(self.joke_category_list[x], 200))
        if category in rez_list:
            print("Данная категория существует! Отправляем запрос на получение..")
            start.test_create_random_joke_positive(category, 200)
        else:
            print("Данной категории не существует! Попробуйте позже")


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

        check_joke = result.json()
        joke_value = check_joke.get('value')
        print(joke_value)

        joke_category = check_joke.get('categories')
        print(joke_category)
        assert joke_category[0] == category, (f"Категория некорректна,"
            f" ожидаемая категория: {category}, полученная: {joke_category[0]}")

        return joke_category[0]



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
        print("Поле Error корректно")

        print("Тест прошёл успешно!")



start = TestCreateJokeCategory()
start.start_question()
print("Тест прошёл успешно")