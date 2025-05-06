from collections import deque, defaultdict
import random


class Solution:
    def __init__(self, nums, k):
        self.cool = defaultdict(list)
        self.pool = nums[:]
        self.k = k
        self.turn = 0

    def pick(self):
        ans = []
        l = len(self.pool)-1

        idx = random.randint(0, l)
        ans = self.pool[idx]
        self.pool[idx], self.pool[-1] = self.pool[-1], self.pool[idx]

        self.cool[self.turn+self.k].append(self.pool[-1])
        self.pool.pop()
        self.turn += 1

        if self.turn in self.cool:
            self.pool.extend(self.cool[self.turn])
            self.cool.pop(self.turn)

        return ans


rp = Solution([1, 2, 3, 4, 5], k=3)
for _ in range(15):
    print(rp.pick(), end=' ')

