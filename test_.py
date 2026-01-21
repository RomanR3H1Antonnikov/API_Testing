import requests
from base_location import BaseLocation


class TestPutLocation(BaseLocation):

    new_address = '50 Sovetskaya street, RU'

    def test_put_new_location(self, place_id):
        put_url = self.build_url(self.update_resource)

        json_put_location = {
            'place_id': place_id,
            "address": self.new_address,
            "key": "qaclick123"
        }

        result_put = requests.put(put_url, json=json_put_location)
        assert result_put.status_code == 200

        check_response_put = result_put.json()
        msg = check_response_put.get('msg')
        assert msg == "Address successfully updated"
