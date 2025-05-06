import bisect
from collections import defaultdict
from sortedcontainers.sortedlist import SortedList


class Plane:
    def __init__(self):
        self.planes = defaultdict(SortedList)
        self.ids = defaultdict(list)

    def update_plane_info(self, planeID, departureTime, departurePlace):
        self.planes[departurePlace].add([departureTime, planeID])
        self.ids[planeID] = [departureTime, departurePlace]


    def search_plane(self, time, departurePlace):
        # 要求只返回一个距离目标时间最近的飞机id
        id = bisect.bisect(self.planes[departurePlace], time, key=lambda x: x[0])
        if id > 1:
            if abs(self.planes[id]-time) < abs(self.planes[id-1]-time):
                return id
            else:
                return id-1
        else:
            return id

    def delete_plane_info(self, planeID, departureTime):
        d_time, d_place = self.ids[planeID]
        ids = bisect.bisect_left(self.planes[d_place], departureTime, key=lambda x: x[0])
        self.planes[d_place].remove(ids)
        
