import requests
from base_location import BaseLocation


class TestDeleteLocation(BaseLocation):

    def test_delete_new_location(self, place_id):
        delete_url = self.build_url(self.delete_resource)

        json_delete_location = {
            "place_id": place_id
        }

        result_delete = requests.delete(delete_url, json=json_delete_location)
        assert result_delete.status_code == 200

        check_response_delete = result_delete.json()
        status = check_response_delete.get('status')
        assert status == "OK"
