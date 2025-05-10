

from typing import List


class Employee:
    def __init__(self, val, members: [List, None] = None):
        self.val = val
        self.members = members


class Department:
    def __init__(self, ceo: Employee):
        self.ceo = ceo
    def count_underpaid_avg(self):
        ans = []
        budget = 0
        def dfs(node: Employee):
            nonlocal ans, budget
            if node.members is None:
                return node.val, 1

            sum_v = 0
            cnt = 0

            for mem in node.members:
                cur_v, cur_cnt = dfs(mem)
                sum_v += cur_v
                cnt += cur_cnt
            if sum_v > node.val * cnt:
                ans.append(node.val)
                budget += sum_v / cnt - node.val

            return sum_v+max(node.val, sum_v/cnt), cnt + 1

        dfs(self.ceo)
        return ans, budget


dept = Department(ceo=Employee(100, [Employee(80,
                                              [Employee(90), Employee(50)]
                                              ),
                                     Employee(60, [Employee(70)])]))

print(dept.count_underpaid_avg())

salaries = {
    0: 100, 1: 80, 2: 60, 3: 90, 4: 50, 5: 70
}
tree = {
    0: [1, 2],  # root manager 0 管理 1, 2
    1: [3, 4],
    2: [5]
}


"""
    0 100
        1: 80
            3: 90
            4: 50
        2: 70
            5: 70
"""