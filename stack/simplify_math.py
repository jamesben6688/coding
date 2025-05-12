class Solution:
    def simplify(self, s):
        ops = [1]
        sign = 1
        i = 0
        from collections import Counter
        n = len(s)
        ans = Counter()
        while i < n:
            if s[i] == " ":
                i += 1
            elif s[i] == "+":
                sign = ops[-1]
                i += 1
            elif s[i] == "-":
                sign = -ops[-1]
                i += 1
            elif s[i] == "(":
                ops.append(sign)
                i += 1
            elif s[i] == ")":
                ops.pop()
                i += 1
            else:
                ans[s[i]] += sign
                i += 1
        return ans


print(Solution().simplify("a-b-(a-(c-a))"))




from collections import defaultdict


class Solution:
    def __init__(self):
        self.i = 0

    def calculate(self, s: str) -> int:
        n = len(s)
        oper = "+"
        num = 0
        stack = []
        while self.i < n:
            ch = s[self.i]
            self.i += 1

            if ch.isalpha():
                num = [[ch, 1]]

            if ch == "(":
                num = self.calculate(s)

            if ch in "+-*/)" or self.i == len(s):
                if oper == "+":
                    for item in num:
                        stack.append(item)
                elif oper == "-":
                    for item in num:
                        stack.append([item[0], -item[1]])
                oper = ch
                num = ""

            if ch == ")" or self.i == len(s):
                break
        return stack  # sum(stack)


if __name__ == '__main__':
    s = "a-b+(a-(c-a))"
    stack = Solution().calculate(s)
    res = defaultdict(int)
    for item in stack:
        res[item[0]] += item[1]
    ans = ""
    for k, v in res.items():
        if v > 1:
            ans += f"+{v}{k}"
        elif v < -1:
            ans += f"{v}{k}"
        elif v == -1:
            ans += f"-{k}"
        elif v == 1:
            ans += f"+{k}"
    ans = ans[1:] if ans[0] == "+" else ans
    print(ans)

