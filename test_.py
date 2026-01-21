import requests


class TestPutLocation:

    base_url = "https://rahulshettyacademy.com"
    key = "?key=qaclick123"
    post_resource = "/maps/api/place/add/json"
    get_resource = "/maps/api/place/get/json"
    put_resource = '/maps/api/place/update/json'
    new_address = '50 Sovetskaya street, RU'

    def test_put_new_location(self, place_id):
        put_url = self.base_url + self.put_resource + self.key
        print(put_url)

        json_put_location = {
            'place_id': place_id,
            "address": self.new_address,
            "key": "qaclick123"
        }

        result_put = requests.put(put_url, json=json_put_location)
        print(result_put.json())

        print(f'Статус-код: {result_put.status_code}')
        assert result_put.status_code == 200
        print('Статус-код PUT корректен')

        check_response_put = result_put.json()

        msg = check_response_put.get('msg')
        print(msg)
        assert msg == "Address successfully updated"
        print('Поле MSG корректно')