import json


class BaseLocation:
    base_url = "https://rahulshettyacademy.com"
    key = "?key=qaclick123"

    add_resource = "/maps/api/place/add/json"
    get_resource = "/maps/api/place/get/json"
    update_resource = "/maps/api/place/update/json"
    delete_resource = "/maps/api/place/delete/json"

    place_id_file = "place_id_db"
    existing_place_id_file = "place_id_existing_db"

    def read_place_ids(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [str(x) for x in data]

    def write_place_ids(self, filename, place_ids):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(place_ids, f, indent=4, ensure_ascii=False)

    def build_url(self, resource):
        return self.base_url + resource + self.key

    def build_get_url(self, place_id):
        return self.build_url(self.get_resource) + "&place_id=" + place_id
