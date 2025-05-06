from collections import defaultdict


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
            O(n)
        """
        cnt = defaultdict(int)
        ans = [' ' for _ in range(len(s))]

        max_len = 0
        for ch in s:
            cnt[ch] += 1
            max_len = max(max_len, cnt[ch])

        if max_len > (len(s) + 1) // 2:
            return ""

        odd = 1
        even = 0

        for ch in cnt:
            while cnt[ch] > 0 and cnt[ch] <= len(s) // 2 and odd < len(s):
                ans[odd] = ch
                cnt[ch] -= 1
                odd += 2

            while cnt[ch] > 0 and even < len(s):
                ans[even] = ch
                cnt[ch] -= 1
                even += 2

        return "".join(ans)


print(Solution().reorganizeString('abb'))