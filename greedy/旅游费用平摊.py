"""
一堆人出去旅行，每个人都有付钱买东西，有人付的多，有人付的少给了两个class
class Person{
	int id
	double payment
}
class Transfer{
	int fromId;
	int toId;
	double payment
}
写一个function 可以split everything evenly between people and settle the balance.
Eg: input [person1,10],[person2, 12] outPut[person 1, person 2, 1];


ChatGPT said:
你给的问题是 费用平均分摊（也叫“AA 制结算”），目标是：

所有人的支出平均，每个人要么给别人补差额，要么从别人那收回来。

✅ 例子解释：
text
Copy
Edit
person1 paid 10
person2 paid 12
平均每人 11
→ person1 需要付 1 给 person2
✅ 解法思路：
计算总共花了多少钱，平均每人该花多少。

计算每个人的 balance = payment - average。

正数说明多付了，应该收钱。

负数说明少付了，应该付钱。

两个队列，一个存 should pay 的人，一个存 should receive 的人。

用 greedy 匹配 settle 掉他们之间的金额。

leetcode 485

"""

class Person:
    def __init__(self, id, payment):
        self.id = id
        self.payment = payment

class Transfer:
    def __init__(self, fromId, toId, payment):
        self.fromId = fromId
        self.toId = toId
        self.payment = payment

    def __repr__(self):
        return f"Transfer(from: {self.fromId}, to: {self.toId}, amount: {self.payment:.2f})"

def splitPaymentsEvenly(people):
    n = len(people)
    total = sum(p.payment for p in people)
    avg = total / n

    balances = [(p.id, round(p.payment - avg, 2)) for p in people]
    creditors = []  # should receive
    debtors = []    # should pay

    for id, balance in balances:
        if balance > 0:
            creditors.append([id, balance])
        elif balance < 0:
            debtors.append([id, -balance])

    transfers = []
    i = j = 0
    while i < len(debtors) and j < len(creditors):
        debtor_id, debt = debtors[i]
        creditor_id, credit = creditors[j]
        payment = min(debt, credit)
        transfers.append(Transfer(debtor_id, creditor_id, payment))
        debtors[i][1] -= payment
        creditors[j][1] -= payment
        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1

    return transfers
