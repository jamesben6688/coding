class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        n = len(s)

        def dfs():
            nonlocal i
            cur = ""
            while i < n:
                ch = s[i]
                if ch.isalpha():
                    cur += ch
                    i += 1
                elif ch.isdigit():
                    num = 0
                    while i < n and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    if i < n and s[i] == '[':
                        i += 1  # skip '['
                        decoded = dfs()
                        cur += decoded * num
                elif ch == ']':
                    i += 1
                    return cur
            return cur

        return dfs()


print(Solution().decodeString("3[a]2[bc]"))
