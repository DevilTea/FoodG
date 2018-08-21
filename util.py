from math import radians, cos, sin, tan, asin, sqrt, atan, acos
from urllib import parse


class Util():
    @staticmethod
    def getDistance(locationA, locationB):
        latA, lonA = locationA.values()
        latB, lonB = locationB.values()
        ra = 6378140  # radius of equator: meter
        rb = 6356755  # radius of polar: meter
        flatten = (ra - rb) / ra  # Partial rate of the earth
        # change angle to radians
        radLatA = radians(latA)
        radLonA = radians(lonA)
        radLatB = radians(latB)
        radLonB = radians(lonB)

        pA = atan(rb / ra * tan(radLatA))
        pB = atan(rb / ra * tan(radLatB))
        x = acos(sin(pA) * sin(pB) + cos(pA) *
                 cos(pB) * cos(radLonA - radLonB))
        c1 = (sin(x) - x) * (sin(pA) + sin(pB))**2 / cos(x / 2)**2
        c2 = (sin(x) + x) * (sin(pA) - sin(pB))**2 / sin(x / 2)**2
        dr = flatten / 8 * (c1 - c2)
        distance = ra * (x + dr)
        return distance

    @staticmethod
    def get_restaurant_info_md(user, restaurant):
        values = {'query': restaurant['name'],
                  'query_place_id': restaurant['place_id']}
        data = parse.urlencode(values).encode('utf-8')
        info_url = "https://www.google.com/maps/search/?api=1&" + str(data)[2:-1]
        distance = "約 " + \
            str(int(Util.getDistance(user.location,
            restaurant['location']))) + " 公尺"

        return "Foodge找到了～\n\n" + \
                "🍽店名🍽 \t" + restaurant['name'] + "\n\n" + \
                "⭐️評分⭐️ \t" + str(restaurant['rating']) + "\n\n" + \
                "🗺地址🗺 \t" + restaurant['vicinity'] + "\n\n" + \
                "📍距離📍 \t" + distance + "\n\n" + \
                "[➡️點擊開啟 Google Map⬅️](" + \
                info_url + ")"
