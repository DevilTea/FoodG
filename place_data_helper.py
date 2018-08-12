import json

from place_api import PlaceAPI


PLACE_API_KEY = None
with open('config.json', 'r') as f:
    PLACE_API_KEY = json.load(f)['PLACE_API_KEY']
    f.close()

place_api = PlaceAPI(PLACE_API_KEY)

class PlaceDataHelper():
    @staticmethod
    def get_restaurants(location, distance, food_name):
        raw_places_data = place_api.get_raw_places_data(location, distance, food_name)
        places_data = {}

        for raw_data in raw_places_data:
            places_data[raw_data['name']] = {
                'place_id': raw_data['place_id'],
                'name': raw_data['name'],
                'vicinity': raw_data['vicinity'],
                'rating': raw_data['rating'],
                'location': raw_data['geometry']['location']
            }
        return places_data
    
    @staticmethod
    def is_restaurant_name_exist(restaurant_name, restaurants):
        return restaurants.get(restaurant_name) is not None

    @staticmethod
    def get_restaurant_by_name(restaurant_name, restaurants):
        return restaurants.get(restaurant_name)
