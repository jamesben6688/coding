# from functools import lru_cache
#
# def solve(nums, target):
#     ops = ['+', '*']
#
#     # 递归所有表达式组合
#     @lru_cache(None)
#     def compute(i, j):
#         results = []
#         if i == j:
#             results.append((str(nums[i]), nums[i]))
#         else:
#             for k in range(i, j):
#                 left_exprs = compute(i, k)
#                 right_exprs = compute(k+1, j)
#                 for l_expr, l_val in left_exprs:
#                     for r_expr, r_val in right_exprs:
#                         for op in ops:
#                             if op == '+':
#                                 val = l_val + r_val
#                             elif op == '*':
#                                 val = l_val * r_val
#                             expr = f"({l_expr}{op}{r_expr})"
#                             results.append((expr, val))
#         return results
#
#
#     # 执行搜索
#     for expr, val in compute(0, len(nums)-1):
#         if val == target:
#             return f"{expr}={target}"
#     return "No solution"
#
#
# print(solve([2, 3, 4], 20))       # (2+3)*4=20
# print(solve([1, 2, 3, 4], 21))    # (1+2)*(3+4)=21
# print(solve([1, 1, 1, 1], 100))   # No solution


"""
给一个没有运算符的等式，填入(,),+,*四种符号使等式成立（任意解），或返回不成立，第一问只有3个数在等式左侧如：
输入2 3 4 = 20 输出 （2+3)*4=20
Follow up:
如果等式左侧的数字有多个（任意个）怎么解。
"""
from functools import cache


class Solution:
    def add_operators(self, num: list, target: int):
        ans = []
        ops = ['+', '*']
        @cache
        def dfs(i, j):  # []
            if i == j:
                return [[str(num[i]), num[i]]]

            cur = []
            for k in range(i, j):
                ls = dfs(i, k)
                rs = dfs(k+1, j)

                for l_exp, l in ls:
                    for r_exp, r in rs:
                        for op in ops:
                            if op == "+":
                                cur.append([f"({l_exp}+{r_exp})", l+r])
                            if op == "*":
                                cur.append([f"({l_exp}*{r_exp})", l * r])
            return cur

        res = dfs(0, len(num)-1)  # 必须要记录所有的结果
        print(res)
        for r_exp, r in res:
            if r == target:
                if r_exp[0] == "(":
                    r_exp = r_exp[1:]
                if r_exp[-1] == ")":
                    r_exp = r_exp[:-1]
                ans.append(f"{r_exp}={target}")
        return ans

s =Solution()
print(s.add_operators([2, 3, 4], 20))
