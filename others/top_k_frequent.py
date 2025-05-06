from heapq import heappop, heappush
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = list(Counter(nums).items())

        def partition(left, right):
            pivot = cnt[left][:]
            while left < right:
                while left < right and cnt[right][1] <= pivot[1]:
                    right -= 1
                cnt[left] = cnt[right]

                while left < right and cnt[left][1] >= pivot[1]:
                    left += 1

                cnt[right] = cnt[left]

            cnt[left] = pivot
            return left

        left = 0
        right = len(cnt) - 1

        while left < right:
            mid = partition(left, right)
            if mid > k:
                right = mid-1
            elif mid < k:
                left = mid+1
            else:
                break

        return [cnt[i][0] for i in range(k)]

print(Solution().topKFrequent(nums = [3,0,1,0], k = 1))