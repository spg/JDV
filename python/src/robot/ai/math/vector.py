import math

class Vector:
    @staticmethod
    def angle(v1, v2):
        return math.atan2(v2[1],v2[0]) - math.atan2(v1[1],v1[0])