class Solution:
    def min_str(self, s):
        cnt = 0
        ans = []
        for i in range(len(s)):
            if s[i] == "(":
                cnt += 1
            else:
                cnt -= 1

            if cnt < 0:
                ans.append((i, "("))
                cnt = 0

        if cnt > 0:
            for i in range(cnt):
                ans.append()

