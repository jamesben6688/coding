"""
第二轮 一个奇怪的sorting算法 要挂就是这一轮 sorting需要swap数字 要求是数字不能向左移动超过2位，求最优的sorting结果
解题思路：
我们可以采用贪心策略 + 有限窗口冒泡：

从左到右遍历数组。

对于每一个位置 i，我们在位置 i 到 i+2 范围内（右边的两个元素）寻找最小值，并尝试将它移动到当前位置 i，前提是它至多往左移动 2 格。

为了让排序尽可能接近最终升序，每次都把局部最小值往前移，但最多只能左移 2 格。

✅ 示例：
原数组：[3, 1, 2, 4]

目标是尽可能变成升序 [1, 2, 3, 4]，但有如下限制：

1 的原始位置是 1，最多能移动到位置 -1（不合法），但它移动到 0 是合法的（移动 1 位）。

2 最多能移动到 0（移动 2 位）。

最终最优排序结果是：[1, 2, 3, 4] ✅

🚫 示例（限制起作用）：
原数组：[1, 2, 5, 3, 4]

3 原始位置是 3，最远能移动到位置 1（不能到位置 0）。

所以 3 无法插到最前面，只能移动最多两步。

最终合法最优排序结果为：[1, 2, 3, 5, 4] ✅（不是完全有序，但满足限制）
"""


def constrained_sort(arr):
    n = len(arr)
    for i in range(n):
        # 在 i ~ min(i+2, n-1) 区间内寻找最小值
        min_idx = i
        for j in range(i + 1, min(i + 3, n)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # 如果最小值距离 i 在两位以内，则把它冒泡到 i
        while min_idx > i:
            # swap with the previous
            arr[min_idx], arr[min_idx - 1] = arr[min_idx - 1], arr[min_idx]
            min_idx -= 1
    return arr

"""
    冒泡排序
"""

def constrained_sort_arbitrary(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    pos_map = {val: idx for idx, val in enumerate(sorted_arr)}  # value → target index

    swaps = 0

    for i in range(n):
        val = arr[i]
        correct_idx = pos_map[val]
        if i - correct_idx > 2:
            print("Too chaotic")
            return

    # Bubble Sort with constraint
    arr = arr[:]  # copy to preserve original
    for i in range(n):
        for j in range(n - 1):
            if pos_map[arr[j]] > pos_map[arr[j + 1]]:
                # Check if arr[j+1] is moving left more than 2 positions
                if j - pos_map[arr[j + 1]] > 2:
                    print("Too chaotic")
                    return
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    print(f"Sorted: {arr}, Swaps: {swaps}")


print(constrained_sort([1, 2, 5, 3, 4]))
