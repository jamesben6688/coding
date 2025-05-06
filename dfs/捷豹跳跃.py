class Solution:
    def jump(self, matrix, in_order, out_order):
        m = len(matrix)

        ans = []
        path = []
        visited = set()
        def dfs(row):
            if row == len(matrix):
                ans.append(path[:])
                return

            for i in range(len(matrix[new_order[row]])):
                path.append(matrix[new_order[row]][i])
                dfs(row+1)
                path.pop()

        order = [0, 1, 2]
        new_order = []
        for o in in_order:
            new_order.append(order[o])

        order = new_order
        new_order = []
        for o in out_order:
            new_order.append(order[o])
        print(new_order)

        dfs(0)

        return ans

# (0 1 2) -> (2 0 1) -> (1 2 0)
# [[m n] [a b] [0 1]]  (2 0 1)
# [[0 1] [m n] [a b]]  (1 2 0)

print(Solution().jump(
[["a","b"], [0, 1], ["m","n"]], in_order=[2, 0, 1], out_order=[2, 0, 1]
))