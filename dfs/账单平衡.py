# from typing import List
# from collections import defaultdict
#
# class Solution:
#     def minTransfers(self, transactions: List[List[int]]) -> int:
#         debts = defaultdict(int)
#         for a, b, t in transactions:
#             debts[a] -= t
#             debts[b] += t
#
#         debts = [[x, debts[x]] for x in debts]
#         ans = float('inf')
#         path = []
#
#         def dfs(start):
#             nonlocal ans
#             while start < len(debts) and debts[start][1] == 0:
#                 start += 1
#
#             if start == len(debts):
#                 if len(path) < ans:
#                     ans = len(path)
#
#             for i in range(start + 1, len(debts)):
#                 if debts[start][1] * debts[i][1] < 0:
#                     amount = min(abs(debts[start][1]), abs(debts[i][1]))
#                     prev_start, prev_i = debts[start][1], debts[i][1]
#                     if debts[start][1] < 0:
#                         path.append((debts[i][0], debts[start][0], amount))
#                         debts[start][1] += amount
#                         debts[i][1] -= amount
#                     else:
#                         path.append((debts[start][0], debts[i][0], amount))
#                         debts[start][1] -= amount
#                         debts[i][1] += amount
#
#                     dfs(start)
#                     path.pop()
#                     debts[start][1] = prev_start
#                     debts[i][1] = prev_i
#
#                     if debts[start][1] + debts[i][1] == 0:
#                         break
#
#         dfs(0)
#         return ans

from collections import defaultdict

class Solution:
    def minTransfersWithPath(self, transactions):
        balance = defaultdict(int)

        # Step 1: 计算每个人的净债务
        for frm, to, amt in transactions:
            balance[frm] -= amt
            balance[to] += amt

        # Step 2: 过滤出净债不为0的人
        debt_list = [(id, amt) for id, amt in balance.items() if amt != 0]
        ids = [id for id, _ in debt_list]
        debts = [amt for _, amt in debt_list]

        res = float('inf')
        final_path = []

        # Step 3: 回溯 + 路径记录
        def dfs(start, path):
            nonlocal res, final_path

            # 跳过已清债的人
            # 这个必须放在前面, 防止原数组中都已经弄好了
            while start < len(debts) and debts[start] == 0:
                start += 1
            if start == len(debts):
                if len(path) < res:
                    res = len(path)
                    final_path = path[:]
                return

            for i in range(start + 1, len(debts)):
                if debts[start] * debts[i] < 0:  # 一正一负才能配对

                    # 转账金额为两人之间的最小绝对值
                    amount = min(abs(debts[start]), abs(debts[i]))
                    prev_start, prev_i = debts[start], debts[i]
                    # 分类讨论：谁给谁转账
                    if debts[start] < 0:
                        # start 欠钱，start 给 i 转账
                        from_id = ids[i]
                        to_id = ids[start]
                        # 模拟转账：start 给 i 转 amount 元
                        debts[start] += amount
                        debts[i] -= amount
                    else:
                        # start 有盈余，i 给 start 转账
                        from_id = ids[start]
                        to_id = ids[i]
                        # 模拟转账：i 给 start 转 amount 元
                        debts[start] -= amount
                        debts[i] += amount

                    # 记录当前转账路径
                    path.append((from_id, to_id, amount))

                    # 继续从当前 start 尝试配对，直到清零
                    dfs(start, path)

                    # 回溯：撤销当前转账
                    path.pop()
                    debts[start] = prev_start
                    debts[i] = prev_i

                    # 剪枝：完全抵消后无需尝试其他配对
                    if debts[start] + debts[i] == 0:
                        break

        dfs(0, [])
        return res, final_path


print(Solution().minTransfers(
    [[0,3,2],[1,4,3],[2,3,2],[2,4,2]]
))
