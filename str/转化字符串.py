"""
 给一个string 比如 a{a,b}ba, 大括号里面的string就是表示多种构成string的方式 比如这个例子的结果就是aaba, abba。
 要求就是写一个function， 通过string parse 把所有可能得结果输出
"""


class Solution:
    def __init__(self):
        self.i = 0

    def parse(self, s):
        ans = []
        def dfs(s):

            j = s.find("}")
            if j == -1:
                ans.append(s)
                return

            i = s.rfind("{", 0, j-1)
            a, c = s[:i], s[j+1:]
            for b in s[i+1:j].split(","):
                dfs(a+b+c)
        dfs(s)
        return ans


print(Solution().parse("a{{a,b}ba,d}e"))
