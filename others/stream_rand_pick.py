import random

class RandomPickStream:
    def __init__(self, target: int):
        self.target = target        # 目标值
        self.count = 0              # 目标值出现的次数
        self.result = None          # 当前被选中的索引
        self.index = 0              # 当前流的下标

    def process(self, num: int):
        """处理数据流中下一个数字"""
        if num == self.target:
            self.count += 1
            if random.randint(1, self.count) == 1:
                self.result = self.index
        self.index += 1

    def get(self) -> int:
        """返回当前等概率选中的索引"""
        return self.result