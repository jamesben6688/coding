from typing import List
import math


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        """
            按照角度, 先排序, 然后用滑动窗口
        """
        angles = []
        ans = 0
        for x, y in points:
            dx = x - location[0]
            dy = y - location[1]
            if dx == 0 and dy == 0:
                ans += 1
            else:
                angles.append(math.atan2(dy, dx) * 180 / math.pi)

        for angle in angles:
            angles.append(angle + 360)

        angles = sorted(angles)

        left = 0
        extra = -1
        # print(angles)
        for i in range(len(angles)):
            while left < len(angles) and angles[i] - angles[left] > angle:
                left += 1

            extra = max(extra, i + 1 - left)
        return ans + extra


print(Solution().visiblePoints(
points =
[[1,1],[1,1],[1,1]],
angle =
1,
location =
[1,1]
))

