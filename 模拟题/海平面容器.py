"""

题目是 求水位低于seaLevel 的数组
给定一组表示地形高度的正整数(在二维中，比如《超级马里奥》)和一个表示平坦海平面的整数，
返回一个表示每个独特水体体积的整数容器。
input:
int[] arr = {1, 5, 1, 3, 4, 3, 1, 2, 7, 5, 6};
            [3, 0, 3, 0, 1, 3, 2, 0, 0, 0]
int seaLevel = 4;
output: [3, 4,6]
如果有高于海平面的跳过，output 是 4-1 =3
"""

from typing import List

def water(heights: List[int], sea_level: int) -> List[int]:
    res = []
    if not heights:
        return res

    start = False
    vol = 0

    for i in range(len(heights)):
        if heights[i] < sea_level:
            start = True
            vol += sea_level - heights[i]
        if start and (i == len(heights) - 1 or heights[i + 1] >= sea_level):
            res.append(vol)
            start = False
            vol = 0

    return res

print(water([3, 0, 3, 0, 1, 3, 2, 0, 0, 0], 4))
