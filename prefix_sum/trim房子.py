class Solution:
    def get_min_floor(self, nums):
        """
            空间可以优化。不用前缀和。

            用一个数记录<i左边的和。

            然后每次sum-nums[i]就是右边的总和

            空间O(lgN)

        :param nums:
        :return:
        """
        nums = sorted(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)

        ans = -1
        mn_floors = prefix_sum[-1]
        cur = 0
        print(prefix_sum)
        n = len(nums)  # [i, n-2] => n-i
        for i in range(n):
            cur = prefix_sum[i] + prefix_sum[n]-prefix_sum[i+1]-(n-i-1)*nums[i]  # [i, n-1]
            print(i, cur)
            if cur < mn_floors:
                mn_floors = cur
                ans = nums[i]

        return ans


print(Solution().get_min_floor([1, 3, 5]))
