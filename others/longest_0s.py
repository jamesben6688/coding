import random

# Generate a random length between 10 and 20
# length = random.randint(10, 20)
#
# # Generate a string of 0s and 1s of the chosen length
# binary_string = ''.join(random.choice('01') for _ in range(length))
# print(binary_string)


class Solution:
    def get_longest_0s(self, s):
        left = 0
        ans_left, max_len = -1, -1
        cnt = 0

        for i in range(len(s)):
            if s[i] == '0':
                cnt += 1
            else:
                cnt = 0
            if cnt > max_len:
                max_len = cnt  # i+1-cnt=left
                ans_left = i - cnt

                if i == len(s) - 1:
                    ans_left += 1

        return ans_left, max_len


print(Solution().get_longest_0s("0111100"))
