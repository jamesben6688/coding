class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        n = len(nums)

        ans = []
        for i in range(n-2):
            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue

            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break

            left = i + 1
            right = n-1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
        return ans


print(Solution().threeSum([0,1,1]))