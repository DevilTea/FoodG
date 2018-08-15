from math import radians, cos, sin, tan, asin, sqrt, atan, acos

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
        x = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(radLonA - radLonB))  
        c1 = (sin(x) - x) * (sin(pA) + sin(pB))**2 / cos(x / 2)**2  
        c2 = (sin(x) + x) * (sin(pA) - sin(pB))**2 / sin(x / 2)**2  
        dr = flatten / 8 * (c1 - c2)  
        distance = ra * (x + dr)  
        return distance