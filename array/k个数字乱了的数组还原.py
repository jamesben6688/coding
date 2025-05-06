"""

给定一个有序的数组和一个数字k，表示这个数组中有k个数是乱序的，还原这个数组 （感觉面试官希望一个小于nlogn的解)

1. 把原数组弄成k个递增子数组, 时间O(N)
2. 合并k个子数组, O(Nlog(K)), 使用最小堆合并
"""
from heapq import *


def restore(arr):
    ans = []
    segs = []
    tmp = [arr[0]]

    n = len(arr)
    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            tmp.append(arr[i])
        else:
            segs.append(tmp[:])
            tmp = [arr[i]]
    segs.append(tmp[:])

    heap = []
    for i in range(len(segs)):
        if len(segs[i]) > 0:
            heappush(heap, (segs[i][0], i, 0))

    while heap:
        val, arr_idx, ele_idx = heappop(heap)
        ans.append(val)

        if ele_idx+1 < len(segs[arr_idx]):
            heappush(heap, (segs[arr_idx][ele_idx+1], arr_idx, ele_idx+1))

    return ans


print(restore([2, 3, 4, 1, 5, 6]))
