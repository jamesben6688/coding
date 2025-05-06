def find_combinations(n):
    stack = [[0, []]]  # 初始栈，存储当前和（初始为0）和当前组合（初始为空）

    while stack:
        current_sum, current_combination = stack.pop()  # 从栈中取出当前和及组合

        # 如果当前组合的和等于目标值，打印组合
        if current_sum == n:
            print(" ".join(map(str, current_combination)))
            continue

        # 如果当前和大于目标值，不需要继续
        if current_sum > n:
            continue

        # 尝试添加 1 和 2，并推入栈中继续探索
        for num in [1, 2]:
            new_combination = current_combination + [num]
            stack.append([current_sum + num, new_combination])

# 示例：寻找和为 4 的所有组合
n = 4
find_combinations(n)

class Solution:

    def get_n(self, n):
        ans = []
        path = []
        def dfs(cur):
            nonlocal ans, path
            if cur >= n:
                if cur == n:
                    # print(path[:])
                    ans.append(path[:])
                return
            for i in range(1, 3):
                path.append(i)
                dfs(cur+i)
                path.pop()
        dfs(0)
        return ans


print(Solution().get_n(4))
