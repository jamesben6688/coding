import random

class RandomSampler:
    def __init__(self, n):
        self.n = n
        self.total = n
        self.mapping = {}  # 模拟下标的交换

    def pick(self):
        if self.total == 0:
            raise Exception("No more items to pick")

        rand_idx = random.randint(0, self.total - 1)

        # 映射值：rand_idx → mapping[rand_idx] if exists, else rand_idx
        val = self.mapping.get(rand_idx, rand_idx)

        # 将 rand_idx 映射到末尾的 total - 1
        self.mapping[rand_idx] = self.mapping.get(self.total - 1, self.total - 1)

        self.total -= 1
        print(self.mapping)
        return val

    def reset(self):
        self.mapping.clear()
        self.total = self.n


sampler = RandomSampler(10)

results = []
for _ in range(10):
    results.append(sampler.pick())

print(sampler.mapping)

print("Random picks:", results)

# sampler.pick() # 再调用会抛异常，因为已经抽完了
sampler.reset()   # 可选，重置状态继续抽样
