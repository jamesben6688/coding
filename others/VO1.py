"""
设计一个允许赊账的balance book, 支持扣款付款查询余额功能 要能跑通
https://www.1point3acres.com/bbs/thread-1114191-1-1.html
"""


class BalanceBook:
    def __init__(self):
        # 初始化余额为0
        self.balance = 0

    def spend(self, amount):
        """扣款，消费 amount"""
        if amount < 0:
            raise ValueError("消费金额不能为负数")
        self.balance -= amount
        print(f"消费了 {amount}，当前余额: {self.balance}")

    def pay(self, amount):
        """付款，向余额中添加 amount"""
        if amount < 0:
            raise ValueError("付款金额不能为负数")
        self.balance += amount
        print(f"付款 {amount}，当前余额: {self.balance}")

    def get_balance(self):
        """查询当前余额"""
        return self.balance


# 测试示例
if __name__ == "__main__":
    # 创建一个余额簿实例
    balance_book = BalanceBook()

    # 查询初始余额
    print(f"初始余额: {balance_book.get_balance()}")

    # 扣款操作
    balance_book.spend(50)  # 扣款 50，余额为 -50

    # 付款操作
    balance_book.pay(30)  # 付款 30，余额为 -20

    # 再次扣款
    balance_book.spend(100)  # 扣款 100，余额为 -120

    # 查询余额
    print(f"当前余额: {balance_book.get_balance()}")

    # 付款操作
    balance_book.pay(150)  # 付款 150，余额为 30

    # 查询最终余额
    print(f"最终余额: {balance_book.get_balance()}")
