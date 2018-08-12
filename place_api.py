import requests


class PlaceAPI():
    def __init__(self, PLACE_API_KEY):
        self.PLACE_API_KEY = PLACE_API_KEY

    def get_raw_places_data(self, location, distance, food_name):
        lat, lng = location.values()
        response = requests.get(
            'https://maps.googleapis.com/maps/api/place/search/json',
            params={
                'location': str(lat) + ',' + str(lng),
                'radius': int(distance),
                'name': str(food_name),
                'types': 'food',
                'sensor': True,
                'language': 'zh-TW',
                'key': self.PLACE_API_KEY
            }
        )
        return response.json()['results']
