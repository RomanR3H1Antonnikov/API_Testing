import json
import requests

import test_
from test2_ import TestDeleteLocation
from test3_ import TestCheckLocation


class TestNewLocation:

    def test_create_new_location(self):

        base_url = "https://rahulshettyacademy.com"
        key = "?key=qaclick123"
        post_resource = "/maps/api/place/add/json"
        get_resource = "/maps/api/place/get/json"
        new_address = '50 Sovetskaya street, RU'

        post_url = base_url + post_resource + key
        print(post_url)

        json_location = {
            "location" : {
                "lat": -38.3494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        place_ids = []

        for i in range(5):
            json_location["address"] = f"29, side layout, cohen 09"

            result_post = requests.post(post_url, json=json_location)
            print(result_post.json())

            print(f"Статус-код: {result_post.status_code}")
            assert result_post.status_code == 200
            print("Статус-код POST корректен")

            check_response_post = result_post.json()

            status = check_response_post.get('status')
            print(status)
            assert status == "OK"
            print("Поле status корректно")

            place_id = check_response_post.get('place_id')
            print(f"Поле place_id: {place_id}")

            place_ids.append(place_id)

        with open("place_id_db", "w", encoding='utf-8') as file:
            json.dump(place_ids, file, indent=4, ensure_ascii=False)

        with open("place_id_db", "r", encoding='utf-8') as file:
            temp = json.load(file)

        print(temp)

        place_id = place_ids[0]
        print(f"Поле place_id: {place_id}")

        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)

        result_get = requests.get(get_url)
        print(result_get.json())

        print(f"Статус-код: {result_get.status_code}")
        assert result_get.status_code == 200
        print("Статус-код GET корректен")

        put_test = test_.TestPutLocation()
        put_test.test_put_new_location(place_id)

        result_get = requests.get(get_url)
        print(result_get.json())
        check_response_get = result_get.json()
        print(f"Статус-код: {result_get.status_code}")
        assert result_get.status_code == 200
        print("Статус-код GET корректен")

        actual_address = check_response_get.get('address')
        print(actual_address)
        assert  actual_address == new_address
        print('Адрес изменился')

        with open("place_id_db", "r", encoding='utf-8') as file:
            temp = json.load(file)

        delete_test = TestDeleteLocation()
        delete_test.test_delete_new_location(temp[1])
        delete_test.test_delete_new_location(temp[3])

        check_test = TestCheckLocation()
        check_test.test_check_new_location(temp)


start = TestNewLocation()
start.test_create_new_location()
print('Тест прошёл успешно')