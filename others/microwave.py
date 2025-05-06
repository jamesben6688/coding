class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, sec: int) -> int:
        def calc(s: str) -> int:
            cost = pushCost * len(s)
            cur = startAt
            for ch in s:
                if ord(ch) - ord('0') != cur:
                    cost += moveCost
                    cur = ord(ch) - ord('0')
            return cost

        ans = float('inf')
        if 60 <= sec < 6000:
            ans = calc(f"{sec // 60}{sec % 60 :02}")

        if sec < 100:
            ans = min(ans, calc(str(sec)))  # 仅输入秒数

        elif sec % 60 < 40:
            ans = min(ans, calc(f"{sec // 60 - 1}{sec % 60 + 60}"))  # 借一分钟给秒数

        return ans


print(Solution().minCostSetTime(startAt = 1, moveCost = 2, pushCost = 1, sec = 600))

