"""
删除所有 0（度数为 0 的点）
如果序列为空，返回 True ✅（合法）
将序列按降序排序
取出最大度 d=D[0]，删除它
从后续 d 个数中每个减去 1（因为你要把当前节点与它们连边）
如果任何值变成负数 → ❌不合法，返回 False
回到第 1 步，继续执行

给一个array [1,1,2,3], tell whether it's true to connect them together.
最多组成 (1*cnt(1)+2*cnt(2)+3*cnt(3)) //2 条边

sum(arr) >= 2*边 -> True
每个element代表一个插座，大小代表连接点的个数。 element只能是1，2，3，返回true or false.
每个连接点只能用一次 input的数组顺序不重要 我们可以自由的改变array的顺序 只要能找到一种可行的连接方式 就返回true
[1,1] --> true
0- -0
[1,2,1] --> true
0- -0- -0
[1,3,1,1,] --> true
0- -0- -0
  |
  |
  0
[1,2,1,1]
0- -0- -0-0
follow up：
如果element有可能是任何postive number怎么办？ sum(arr) >= 2*边 -> True
如果要求不能有空的连接点怎么办？ sum() == 2*边
自己能和自己连接的时候？ sum() - 2*边 是偶数
自己不能和自己连接的时候？ sum() == 2*(len-1)

"""
def havel_hakimi_construct(degrees):
    from collections import deque

    n = len(degrees)
    deg_list = [(degrees[i], i) for i in range(n)]  # (degree, node index)
    edges = []

    while True:
        # 清除所有度数为 0 的节点
        deg_list = [x for x in deg_list if x[0] > 0]
        if not deg_list:
            break  # 构造完成

        # 按度数降序排列
        deg_list.sort(reverse=True)
        d, u = deg_list.pop(0)  # 取出最大度节点 u

        if d > len(deg_list):
            return None  # 不足够的点连接，非法序列

        for i in range(d):
            dv, v = deg_list[i]
            deg_list[i] = (dv - 1, v)
            edges.append((u, v))  # 添加一条边

        # 继续下一轮

    return edges
