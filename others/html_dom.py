from collections import deque


class TreeNode:
    def __init__(self, val, is_leaf, idx=None, child=None):
        self.val = val
        self.idx = idx
        self.is_leaf = is_leaf
        self.child = child

class Solution:
    def get_doms(self, root, s):
        leaf_nodes = []
        que = deque([root])
        while que:
            q_size = len(que)
            for i in range(q_size):
                cur = que.popleft()
                if cur.is_leaf:
                    leaf_nodes.append([cur.val, cur.idx])
                else:
                    for child in cur.child:
                        que.append(child)

        used = [False for _ in range(len(leaf_nodes))]
        n = len(leaf_nodes)
        ans = []
        f = []

        def dfs(cur_s):
            nonlocal f, ans
            if len(cur_s) >= len(s):
                if cur_s == s:
                    f = ans[:]
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    ans.append(i)
                    if cur_s == "":
                        l1 = len(leaf_nodes[i][0])
                        for j in range(l1):
                            tmp = cur_s
                            cur_s = cur_s + leaf_nodes[i][0][j:]
                            dfs(cur_s)
                            cur_s = tmp

                    elif len(cur_s + leaf_nodes[i][0]) >= len(s):
                        l2 = len(leaf_nodes[i][0])
                        for j in range(l2):
                            tmp = cur_s
                            cur_s = cur_s + leaf_nodes[i][0][:j+1]
                            dfs(cur_s)

                            cur_s = tmp
                    else:
                        tmp = cur_s
                        cur_s += leaf_nodes[i][0]
                        dfs(cur_s)
                        cur_s = tmp
                    used[i] = False
                    ans.pop()

        dfs("")
        return f


root = TreeNode("Div", False)
node1 = TreeNode("b", False)
node2 = TreeNode("is", True, 1)
node3 = TreeNode("i", False)
node4 = TreeNode("This", True, 0)
node5 = TreeNode("fun", True, 2)

root.child = [node1, node2, node3]
node1.child = [node4]
node3.child = [node5]

s = "Thisisfun"

print(Solution().get_doms(root, s))
