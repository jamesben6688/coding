import random
from typing import List

class Solution:
    def findKthLargestUnique(self, nums: List[int], k: int) -> int:
        """
            K-th unique: count_unique: n/2+n/4+n/8+... = O(N)



        :param nums:
        :param k:
        :return:
        """
        def is_unique_in_range(nums, left, right, val):
            for i in range(left, right):
                if nums[i] == val:
                    return False
            return True

        def count_unique(nums, left, right):
            count = 0
            for i in range(left, right):
                if is_unique_in_range(nums, left, i, nums[i]):
                    count += 1
            return count

        def quickselect_unique(nums, left, right, k):
            if left > right:
                raise ValueError("Not enough unique elements")

            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]

            # 3-way partition
            lt, i, gt = left, left, right
            while i <= gt:
                if nums[i] > pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] < pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            # Count unique numbers in nums[left:lt]
            uniq_count = count_unique(nums, left, lt)

            if uniq_count == k - 1:
                return pivot
            elif uniq_count >= k:
                return quickselect_unique(nums, left, lt - 1, k)
            else:
                return quickselect_unique(nums, gt + 1, right, k - uniq_count - 1)

        return quickselect_unique(nums, 0, len(nums) - 1, k)
