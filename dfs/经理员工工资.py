"""
you have a organization tree, if a manager's salary is lower than the avarage of it's reports
( direct reports and indirect reports), then it's underpaid
find out the count of underpaid manager

follow up: if pay extra money to make all underpaid manager not underpaied, what's the minum money will spend.
for example:
A(100)
- B(200)
	- C(100)
	- D(60)
then A is underpaid : B + C + D / 3 = (200 + 100 + 60)/3 = 120 > 100
B is not underpaied since no reports

这本质上是一个 树的后序遍历问题（Post-order traversal）：

对每个节点（管理者）：

递归获取其所有子节点的薪资总和与人数；

判断当前节点是否 underpaid；

同时累计所需补齐的最少金额。
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.reports = []  # list of Employee


def count_underpaid_and_min_raise(root):
    underpaid_count = 0
    min_extra_pay = 0

    def dfs(node):
        nonlocal underpaid_count, min_extra_pay

        if not node.reports:
            return (node.salary, 1)  # sum, count

        total_sum, total_count = 0, 0

        for report in node.reports:
            s, c = dfs(report)
            total_sum += s
            total_count += c

        avg = total_sum / total_count

        if node.salary < avg:
            underpaid_count += 1
            needed = avg - node.salary
            min_extra_pay += needed

        return (total_sum + node.salary, total_count + 1)

    dfs(root)
    return underpaid_count, round(min_extra_pay, 2)
# 组织结构：
# A(100)
# └── B(200)
#     ├── C(100)
#     └── D(60)

A = Employee("A", 100)
B = Employee("B", 200)
C = Employee("C", 100)
D = Employee("D", 60)

B.reports = [C, D]
A.reports = [B]

print(count_underpaid_and_min_raise(A))
# 输出: (1, 20.0)
