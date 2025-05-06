"""
give you some buckets , you know the capacity of each bucket, return if you can use the buckets
to get target gallon of water.assume you have infinity buckets of each size.
for example , target is 11, buckets [7, 4],true (7 + 4)
target 8, buckets[7, 5]. return true, 7-5 = 2 do 4 rounds. follow up, how to make the operate times minum.

 思路：
我们可以将问题视为一个图搜索问题，每个水量（从 0 到目标水量）是一个节点。

每次操作可以通过加法或减法（使用给定的水桶）来得到一个新的水量。

目标是找到最小的操作次数，使得水量达到目标。

✅ 算法：
广度优先搜索（BFS）：从目标水量开始，通过BFS进行广度优先的搜索。每次尝试加上或减去水桶的容量，直到到达目标水量。

去重：使用一个 visited 集合来记录已经访问过的水量，避免重复计算。
"""

from collections import deque

def min_operations_to_target(target, buckets):
    # BFS 队列
    queue = deque([(0, 0)])  # (当前水量, 操作次数)
    visited = set([0])

    while queue:
        current, steps = queue.popleft()

        # 如果当前水量等于目标水量，返回操作次数
        if current == target:
            return steps

        # 遍历所有桶的容量，进行加法和减法操作
        for bucket in buckets:
            # 加法操作
            new_water = current + bucket
            if new_water <= target and new_water not in visited:
                visited.add(new_water)
                queue.append((new_water, steps + 1))

            # 减法操作
            new_water = current - bucket
            if new_water >= 0 and new_water not in visited:
                visited.add(new_water)
                queue.append((new_water, steps + 1))

    return -1  # 如果没有找到路径
