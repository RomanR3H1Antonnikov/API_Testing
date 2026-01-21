import requests
from base_location import BaseLocation


class TestCheckLocation(BaseLocation):

    def classify_place_ids(self, place_ids):
        existing = []
        missing = []

        for id in place_ids:
            url = self.build_get_url(id)
            resp = requests.get(url)

            if resp.status_code == 200:
                existing.append(id)
            elif resp.status_code == 404:
                missing.append(id)
            else:
                raise AssertionError(f"Некорректный статус-код: {resp.status_code} для place_id: {pid}")

        return existing, missing

    def test_check_new_location(self, place_ids):
        existing, missing = self.classify_place_ids(place_ids)

        assert len(existing) == 3
        assert len(missing) == 2

        self.write_place_ids(self.existing_place_id_file, existing)
