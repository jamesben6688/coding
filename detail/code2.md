1.
判断是否有
`A->B->C
`这样的sequence
```python
from collections import defaultdict


class Solution:

    def has_path(self, edges):
        graph = defaultdict(list)
        visited = defaultdict(bool)
        path = []
        ans = []
        cnt = defaultdict(int)
        for s, t in edges:
            graph[s].append(t)
            if 'A' in s and 'B' in t:
                cnt[t] += 1
            visited[s] = False
            visited[t] = False

        def dfs(cur):
            nonlocal path, ans
            if 'C' in cur:
                ans.append(path[:])
                return True

            if visited[cur]: return False

            visited[cur] = True
            if 'A' in cur:
                for ne in graph[cur]:
                    if 'B' in ne and cnt[ne] >= 2:
                        path.append(ne)
                        dfs(ne)
                        # if dfs(ne): return True
                        path.pop()

            if 'B' in cur:
                for ne in graph[cur]:
                    if 'B' in ne and cnt[ne] >= 2 or 'C' in ne:
                        path.append(ne)
                        dfs(ne)
                        # if dfs(ne): return True
                        path.pop()
            visited[cur] = False
            return False

        for k in graph:
            if 'A' in k:
                path.append(k)
                dfs(k)
                # if dfs(k):
                #     print(ans)
                # return True
                path.pop()
        print(ans)
        return False


edges = [
    ['A1', 'B1'],
    ['A1', 'B2'],
    ['A3', 'B1'],
    ['B1', 'C1'],
    ['B2', 'C2']
]

print(Solution().has_path(edges))

```

follow - up:

2.
backpropagation, backward
```python
from einops import *
import numpy as np
import matplotlib.pyplot as plt


class Softmax:
    def __init__(self, train=True):
        self.grad = None
        self.train = train

    def forward(self, x, y):
        prob = np.exp(x - np.max(x, axis=1, keepdims=True))
        prob /= np.sum(prob, axis=1, keepdims=True)

        if self.train:
            loss = -np.sum(np.log(prob[range(len(y)), y])) / len(y)

            self.grad = prob.copy()
            self.grad[range(len(y)), y] -= 1
            self.grad /= len(y)
            return prob, loss

        else:
            return prob

    def backward(self):
        return self.grad


class Linear:
    def __init__(self, in_channels, out_channels, lr):
        self.w = np.random.rand(in_channels, out_channels)
        self.b = np.random.rand(out_channels)
        self.lr = lr

    def forward(self, x):
        self.x = x
        output = einsum(x, self.w, 'b c1, c1 c2 -> b c2') + self.b
        return output

    def backward(self, prev_grad):
        cur_grad = einsum(rearrange(self.x, 'b c -> c b'), prev_grad, 'c1 b, b c2 -> c1 c2')

        self.w -= self.lr * cur_grad
        self.b -= self.lr * np.sum(prev_grad, axis=0)
        return cur_grad


class Network:
    def __init__(self, in_channels, out_channels, n_classes, lr):
        self.lr = lr
        self.linear = Linear(in_channels, out_channels, lr)
        self.softmax = Softmax()

    def forward(self, x, y=None):
        out = self.linear.forward(x)
        out = self.softmax.forward(out, y)
        return out

    def backward(self):
        grad = self.softmax.backward()
        grad = self.linear.backward(grad)

        return grad


if __name__ == "__main__":
    data = np.array([[2, 1, 0],
                     [2, 2, 0],
                     [5, 4, 1],
                     [4, 5, 1],
                     [2, 3, 0],
                     [3, 2, 0],
                     [6, 5, 1],
                     [4, 1, 0],
                     [6, 3, 1],
                     [7, 4, 1]])

    # x = np.concatenate([np.array([[1]] * data.shape[0]), data[:, :2]], axis=1)
    x = data[:, :-1]
    y = data[:, -1:].flatten()

    net = Network(2, 2, 2, 0.1)
    # loss_fn = CrossEntropy(n_classes=2)
    for epoch in range(500):
        prob, loss = net.forward(x, y)
        # loss = loss_fn.forward(out, y)
        # grad_ = loss_fn.backward()
        grad = net.backward()
        print(loss)

    for d in data:
        if d[2] == 0:
            plt.scatter(*d[:2], color='red')
        else:
            plt.scatter(*d[:2], color='green')

    net.softmax.train = False
    test_data = np.array([[0, 0], [0, 4], [8, 6], [10, 10]])
    res = net.forward(np.array([[0, 0], [0, 4], [8, 6], [10, 10]]))
    res = np.argmax(res, axis=1)
    for i in range(len(test_data)):
        if res[i] == 0:
            plt.scatter(*test_data[i], color="blue")
        else:
            plt.scatter(*test_data[i], color='pink')
    plt.show()
    # print(net.forward(np.array([[0, 0], [0, 4], [8, 6], [10, 10]])), y)
```

3.
公交车站(bus
station) https://leetcode.cn/problems/bus-routes/
```python
"""
            dijstra 算法
            时间复杂度: O(S), S为所有公交站的总数量

                因为每天路线最多走一次, 每个station最多遍历一次
            空间复杂度: O(S)
        """
if source == target: return 0

stop_route = defaultdict(list)

n = len(routes)
for i in range(n):
    route = routes[i]
    for station in route:
        stop_route[station].append(i)

que = deque([source])
dis = {source: 0}
visit = set()

while que:
    x = que.popleft()
    dis_x = dis[x]

    for route in stop_route[x]:
        if route not in visit:
            visit.add(route)
            for station in routes[route]:
                if station not in dis:
                    dis[station] = dis[x] + 1
                    que.append(station)

                if station == target:
                    return dis[station]

return -1
```
方法二: bfs
```python


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
            将每条公交路线当成一个node,如果两条公交路线之间有shared station,
            则两个node之间加上1条边。

            时间复杂度: O(nm**2+n**2)
            空间复杂度: O(m**2+n**2)

            题解: https://godweiyang.com/2020/03/07/leetcode-815/
        """
        if source == target: return 0

        graph = defaultdict(list)
        edges = defaultdict(list)

        n = len(routes)

        for i in range(n):
            route = routes[i]
            for station in route:
                for other_route in graph[station]:
                    if i != other_route:
                        edges[i].append(other_route)
                        edges[other_route].append(i)
                graph[station].append(i)

        que = deque()
        visit = set()

        for route in graph[source]:
            que.append(route)
            visit.add(route)

        target_route = set()
        for t in graph[target]:
            target_route.add(t)

        ans = 0

        while len(que) > 0:
            q_size = len(que)
            ans += 1
            for i in range(q_size):
                node = que.popleft()
                if node in target_route:
                    return ans

                for neighbor in edges[node]:
                    if neighbor not in visit:
                        que.append(neighbor)
                        visit.add(neighbor)
        return -1


```
5.
为YouTube平台做一个推荐系统，如果视频A
similar
to
B （weighted）且
B
similar
to
C （weighted），那么A
similar
to
C （weight = AB * BC）。问如何找最similar的k个。

思路: 使用dijstra计算某个节点A到其他所有节点的最长距离, 距离计算公式是按照乘法而不是加法。

然后选择k个最相似的pair
```python
import random
from collections import defaultdict, deque
from heapq import *


class Solution:
    def top_k_similar_pair(self, videos, edges, k):
        n = len(videos)
        graph = defaultdict(defaultdict)
        for i, j, s in edges:
            graph[i].update({j: s})
            graph[j].update({i: s})

        ans = []
        added = set()
        for v in videos:
            que = []
            heappush(que, (-1, v))
            # que.append(v)
            visited = set()
            visited.add(v)
            sim = {x: [0, []] for x in videos}
            sim[v] = [1, [v]]
            while que:
                s, x = heappop(que)
                s = -s
                visited.add(x)
                if x != v:
                    # ans.append((s, v, x))
                    if v + x not in added:
                        heappush(ans, (s, v, x))
                        added.add(v + x)
                        added.add(x + v)
                    if len(ans) > k:
                        heappop(ans)
                for ne in graph[x]:
                    if ne not in visited and graph[x][ne] * s > sim[ne][0]:
                        sim[ne][0] = graph[x][ne] * s
                        sim[ne][1] = sim[x][1] + [ne]
                        heappush(que, (-sim[ne][0], ne))
            print(v, sim)
        return sorted(ans, reverse=True)


videos = ['A', 'B', 'C', 'D', 'E']

# 随机生成视频之间的边和相似度（边的权重）
# edges = [
#     ('A', 'B', random.uniform(0.1, 0.9)),
#     ('B', 'C', random.uniform(0.1, 0.9)),
#     ('A', 'C', random.uniform(0.1, 0.9)),
#     ('A', 'D', random.uniform(0.1, 0.9)),
#     ('D', 'E', random.uniform(0.1, 0.9)),
#     ('B', 'D', random.uniform(0.1, 0.9)),
#     ('C', 'E', random.uniform(0.1, 0.9)),
# ]

edges = [
    ('A', 'B', 0.33867226227162095),
    ('B', 'C', 0.34360356636396683),
    ('A', 'C', 0.5743097086426759),
    ('A', 'D', 0.24451056675643512),
    ('D', 'E', 0.4516762261475651),
    ('B', 'D', 0.14118118101300095),
    ('C', 'E', 0.7648222463034106)
]

# print(edges)
print(Solution().top_k_similar_pair(videos, edges, 10))
```

followup: 如果graphnode不存在本地怎么办。
可以使用分布式存储, 计算距离的时候。节点内部的相似度和节点之间的相似度。

5.
Given
an
undirected
graph, and two
nodes
A, B.Find
the
shortest
path
between
them.
follow - up: Find
all
nodes in their
shorteat
path.
带路径的dijstra
```python
from collections import defaultdict
from heapq import *


class Solution:
    def shortest_path(self, n, edges, start, end):
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        visited = [False for _ in range(n)]
        visited[start] = True
        dis = [[float('inf'), ""] for _ in range(n)]
        dis[start] = [0, f"{start}"]
        que = [(0, start)]

        while que:
            cur_dis, cur = heappop(que)
            if cur == end:
                return dis[cur]
            visited[cur] = True
            for ne in graph[cur]:
                if not visited[ne] and cur_dis + 1 < dis[ne][0]:
                    # dis[ne] = cur_dis + ne
                    dis[ne] = [cur_dis + 1, dis[cur][1] + str(ne)]
                    heappush(que, (dis[ne][0], ne))
        return ""


edges = [
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 3),
    (2, 0),
    (2, 3),
    (3, 1),
    (3, 2),
    (3, 4),
    (4, 3)
]
n = 5
start = 0
end = 4
print(Solution().shortest_path(n, edges, start, end))
```

7.
化简数学表达式。比如a - (b + a - (c + a)) = -b + a + c.
方法1: dfs:
```python
from collections import defaultdict


class Solution:
    def __init__(self):
        self.i = 0

    def calculate(self, s: str) -> int:
        n = len(s)
        oper = "+"
        num = 0
        stack = []
        while self.i < n:
            ch = s[self.i]
            self.i += 1

            if ch.isalpha():
                num = [[ch, 1]]

            if ch == "(":
                num = self.calculate(s)

            if ch in "+-*/)" or self.i == len(s):
                if oper == "+":
                    for item in num:
                        stack.append(item)
                elif oper == "-":
                    for item in num:
                        stack.append([item[0], -item[1]])
                oper = ch
                num = ""

            if ch == ")" or self.i == len(s):
                break
        return stack  # sum(stack)


if __name__ == '__main__':
    s = "a-b+(a-(c-a))"
    stack = Solution().calculate(s)
    res = defaultdict(int)
    for item in stack:
        res[item[0]] += item[1]
    ans = ""
    for k, v in res.items():
        if v > 1:
            ans += f"+{v}{k}"
        elif v < -1:
            ans += f"{v}{k}"
        elif v == -1:
            ans += f"-{k}"
        elif v == 1:
            ans += f"+{k}"
    ans = ans[1:] if ans[0] == "+" else ans
    print(ans)

```
方法2: stack:
```python


class Solution:
    def simplify(self, s):
        ops = [1]
        sign = 1
        i = 0
        from collections import Counter
        n = len(s)
        ans = Counter()
        while i < n:
            if s[i] == " ":
                i += 1
            elif s[i] == "+":
                sign = ops[-1]
                i += 1
            elif s[i] == "-":
                sign = -ops[-1]
                i += 1
            elif s[i] == "(":
                ops.append(sign)
                i += 1
            elif s[i] == ")":
                ops.pop()
                i += 1
            else:
                ans[s[i]] += sign
                i += 1
        return ans


print(Solution().simplify("a-b-(a-(c-a))"))
```
9.Top K Frequent Elements https://leetcode.cn/problems/top-k-frequent-elements/description/ https://leetcode.com/problems/top-k-frequent-elements/description/
无向图中连通分量的数目
DFS / BFS / 并查集
Number of Connected Components in an Undirected Graph https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
11. 计算器1[EN](https: // leetcode.com / problems / basic - calculator / description /)
12.
有个传送带，传送带上来的货物是 1 2 7 9 22
这种的整数。你有无穷大的等候区
需要把来的货先卸货
然后k个一组打包带走
这k个货的最远距离必须在d以内, 比如d = 3, k = 3，245
就可以，145
就不行。然后input是一个一个的整数
如果能打包了
就output三个数
不能打包就啥也不输出
```python


def process_goods(d, k):
    waiting_area = []

    while True:
        # 接收一个新货物
        new_goods = input("请输入新货物：")
        if new_goods == "":  # 如果没有输入，结束循环
            break

        new_goods = int(new_goods)

        # 将新货物加入到等待区
        waiting_area.append(new_goods)

        # 判断是否能组成一个合法的包
        if len(waiting_area) >= k:
            # 取出所有货物的排列组合，进行判断
            waiting_area.sort()  # 对货物进行排序

            for i in range(len(waiting_area) - k + 1):
                selected_goods = waiting_area[i:i + k]
                if selected_goods[-1] - selected_goods[0] <= d:
                    # 满足条件，输出并移除这 k 个货物
                    print(selected_goods[0], selected_goods[1], selected_goods[2])
                    # 移除已经打包的 k 个货物
                    del waiting_area[i:i + k]
                    break


```
13.
键盘matrix由字符组成，问能不能在给定的某个步数内组成一个单词。
DFS解决
```python
class Solution:
    def jump(self, keyboard, word, dis):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(keyboard)
        n = len(keyboard[0])

        def dfs(i, j, idx, step):
            if idx == len(word):
                return True

            if step <= 0: return False

            for d in range(4):
                ii = i + dirs[d][0]
                jj = j + dirs[d][1]
                if 0 <= ii < m and 0 <= jj < n:
                    if keyboard[ii][jj] == word[idx]:
                        if dfs(ii, jj, idx + 1, dis):
                            return True
                    elif dfs(ii, jj, idx, step - 1):
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if keyboard[i][j] == word[0]:
                    if dfs(i, j, 1, dis):
                        return True
        return False


print(Solution().jump(
    [["Q", "X", "P", "L", "E"],
     ["W", "A", "C", "I", "N"]],
    'QPCW',
    2
))
```
Follow
up问如果按键有重复的怎么做: 加入一个visited数组

14. 3 sum问题 https://leetcode.com/problems/3sum/description/
```python


class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        n = len(nums)

        ans = []
        for i in range(n - 2):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue

            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break

            left = i + 1
            right = n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
        return ans


print(Solution().threeSum([0, 1, 1]))
```

16. 餐厅等座系统
for loop 用原来的函数即可
    ```python
class ListNode:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        dummy = ListNode('dummy')
        dummy.next = dummy.previous = dummy
        self.head = self.tail = dummy

    def append(self, node):
        node.next = self.tail
        node.previous = self.tail.previous
        self.tail.previous.next = node
        self.tail.previous = node

    def remove(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous

    def popleft(self):
        node = self.head.next
        self.remove(node)
        return node

    def print(self):
        node = self.head.next
        while node != self.tail:
            print(node.value)
            node = node.next


from collections import namedtuple, defaultdict

Customer = namedtuple('Customer', ['name', 'party_size'])


class WaitList:
    def __init__(self, sizes):
        self.tables = defaultdict(int)
        for table in sizes:
            self.tables[table] += 1
        # table size => doubly linked list
        self.waiting = defaultdict(DoublyLinkedList)
        # customer => node from the doubly linked list
        self.customers = dict()

    def add(self, customer):
        table = customer.party_size
        self.tables[table] -= 1
        node = ListNode(customer)
        self.waiting[table].append(node)
        self.customers[customer] = node

    def remove(self, customer):
        table = customer.party_size
        self.tables[table] += 1
        node = self.customers[customer]
        self.waiting[table].remove(node)
        del self.customers[customer]

    def serve(self, seats):
        table = seats
        node = self.waiting[table].popleft()
        customer = node.value
        self.remove(customer)
        print('served', customer.name)


sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wl = WaitList(sizes)
bob1 = Customer('Bob1', 4)
wl.add(bob1)
bob2 = Customer('Bob2', 4)
wl.add(bob2)
wl.serve(4)  # served Bob1
wl.serve(4)  # served Bob2
tom = Customer('Tom', 10)
wl.add(tom)
wl.remove(tom)
wl.add(tom)
wl.serve(10)  # served Tom

```
17. 给了一些排序的不重复的区间。给你一个新区间，要求合并，并计算总长度。
18. 课程表的变体: 先修课程对[0, 1] 表示：想要学习课程 0 ，你需要先完成课程
1 。
请你判断是否可能完成所有课程的学习？
19.未知网格最短路径 https://leetcode.com/problems/shortest-path-in-a-hidden-grid/description/
网格中的每个位置只会是可通行和不可通行两种状态。题目保证机器人的起点和终点不同，且都是可通行的。

你需要找到起点到终点的最短路径，然而你不知道网格的大小、起点和终点。你只能向
GridMaster
对象查询。

17.[coins II零钱兑换](https://leetcode.cn/problems/coin-change/submissions/532352681)
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            dp[i] = dp[i-coins[j]] + 1
        """
        dp = [inf for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return dp[-1] if dp[-1] < inf else -1


```
19. number of islands II.
20. 给出一堆东西和一个东西，找出和这个东西最相近的东西。这个东西是三维，比如色彩的。 可以使用kd树解决。
21. 小于N的数字中, 1 的数目
22. 给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回
所需会议室的最小数量 。 meeting - rooms - ii
解决方案: 1.
扫描线;
2. 堆
23. 找相似视频中rating最高的movie.
解决方案: dfs + heap

This question is about writing a simplified movie recommendation system.Each movie has a title and a rating, and we have a separate process that has marked some movies as similar to other movies. For our purpose, we want to assume that similarity is a transitive property: if the process has marked movie A as similar to movie B, and movie B similar to movie C, we will also consider movie A as similar to movie C even if the process didn \'t mark it explicitly. Given a movie from the list,  return its N similar movies with highest rating. For example, if we have the following four movies:     "Movie A"     with rating 6 "Movie B" with rating 7 "Movie C" with rating 8 "Movie D" with rating 9 and the process has determined the following similarities: "Movie A" is similar to "Movie B" "Movie B" is similar to "Movie C" and we request 1 recommendation based on "Movie A", then the answer will be "Movie C" which is the one movie with highest rating among those similar to "Movie A".

23.实现YouTubeMusic的Top100推荐。这个Top100  
MusicList排序是用户最近收听的frequency。用户手动加入List的Music需要排在List最上面。  
我的做法：LFU套壳  
LFU: [CN](
    https: // leetcode.cn / problems / lfu - cache / solutions / 2457716 / tu - jie - yi - zhang - tu - miao - dong - lfupythonja - f56h /)
```python
"""
写一个功能实现YouTube Music的Top100推荐。
这个Top100 Music List排序是用户最近收听的frequency。用户手动加入List的Music需要排在List最上面。
我的做法：LFU套壳
"""
from collections import defaultdict
from typing import Optional


# 题解: https://leetcode.cn/problems/lfu-cache/solutions/2457716/tu-jie-yi-zhang-tu-miao-dong-lfupythonja-f56h/

class Node:
    # 提高访问属性的速度，并节省内存
    """
        需要多级双向链表
    """
    __slots__ = 'prev', 'next', 'key', 'value', 'freq'

    def __init__(self, key=0, val=0):
        self.key = key
        self.value = val
        self.freq = 1  # 新书只读了一次


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}

        def new_list() -> Node:
            dummy = Node()  # 哨兵节点
            dummy.prev = dummy
            dummy.next = dummy
            return dummy

        self.freq_to_dummy = defaultdict(new_list)

    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key_to_node:  # 没有这本书
            return None
        node = self.key_to_node[key]  # 有这本书
        self.remove(node)  # 把这本书抽出来
        dummy = self.freq_to_dummy[node.freq]
        if dummy.prev == dummy:  # 抽出来后，这摞书是空的
            del self.freq_to_dummy[node.freq]  # 移除空链表
            if self.min_freq == node.freq:  # 这摞书是最左边的
                self.min_freq += 1
        node.freq += 1  # 看书次数 +1
        self.push_front(self.freq_to_dummy[node.freq], node)  # 放在右边这摞书的最上面
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:  # 有这本书
            node.value = value  # 更新 value
            return
        if len(self.key_to_node) == self.capacity:  # 书太多了
            dummy = self.freq_to_dummy[self.min_freq]
            back_node = dummy.prev  # 最左边那摞书的最下面的书
            del self.key_to_node[back_node.key]
            self.remove(back_node)  # 移除
            if dummy.prev == dummy:  # 这摞书是空的
                del self.freq_to_dummy[self.min_freq]  # 移除空链表
        self.key_to_node[key] = node = Node(key, value)  # 新书
        self.push_front(self.freq_to_dummy[1], node)  # 放在「看过 1 次」的最上面
        self.min_freq = 1

    # 删除一个节点（抽出一本书）
    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev

    # 在链表头添加一个节点（把一本书放在最上面）
    def push_front(self, dummy: Node, x: Node) -> None:
        x.prev = dummy
        x.next = dummy.next
        x.prev.next = x
        x.next.prev = x


```

24.给一个数组nums，要求找到最短的连续子数组，包含至少k个不同的整数。如果不存在这样的子数组，返回 - 1。
输入: nums = [4, 3, 5, 3, 3, 1, 2, 3], k = 3
输出: 4 // 可能的解是[5, 3, 3, 1]
或[3, 5, 3, 1]
```python
from collections import Counter


class Solution:
    def shortest(self, nums, k):
        left = 0
        i = 0

        n = len(nums)
        cnt = Counter()

        min_len = float('inf')
        ans = []
        while i < n:
            cnt[nums[i]] += 1
            while len(cnt) >= k:
                if i + 1 - left < min_len:
                    min_len = i + 1 - left
                    ans = nums[left:i + 1][:]
                elif i + 1 - left == min_len:
                    ans.append(nums[left:i + 1][:])

                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    cnt.pop(nums[left])
                left += 1

            i += 1
        return ans


print(Solution().shortest(nums=[4, 3, 5, 3, 3, 1, 2, 3], k=3))

```

25. 977.有序数组的平方[CN](https: // leetcode.cn / problems / squares - of - a - sorted - array / description /)
给你一个按非递减顺序排序的整数数组nums，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

56. 合并区间[CN](https: // leetcode.cn / problems / merge - intervals / description /)

27. 有一堆任务，每个任务需要固定时间在单个CPU上跑，而且每个任务有自己的开始时间。给你一定数量的CPU，让你找出所有任务完成的最小时间。
```python
from copy import deepcopy


class Solution:
    def min_time(self, tasks, num_cpus):
        mn_time = float('inf')
        finish = [False for _ in range(len(tasks))]
        cpu_time = [0 for _ in range(num_cpus)]
        cpu_schedule = [[] for _ in range(num_cpus)]
        ans = []

        def dfs(n_finish):
            nonlocal mn_time, ans
            if n_finish == len(tasks):
                if max(cpu_time) < mn_time:
                    mn_time = max(cpu_time)
                    ans = deepcopy(cpu_schedule)
                return

            for i in range(len(tasks)):
                if not finish[i]:
                    finish[i] = True
                    n_finish += 1

                    for j in range(num_cpus):
                        tmp_time = cpu_time[j]
                        cpu_time[j] = tasks[i][1] + max(cpu_time[j], tasks[i][0])
                        cpu_schedule[j].append(i)
                        dfs(n_finish)
                        cpu_schedule[j].pop()
                        cpu_time[j] = tmp_time
                    n_finish -= 1
                    finish[i] = False

        dfs(0)
        return mn_time, ans


# Example usage:
tasks = [(0, 5), (1, 3), (2, 1), (4, 2)]  # (start_time, duration)
num_cpus = 2  # 6
print(Solution().min_time(tasks, num_cpus))  # Output will be the minimum time to complete all tasks
```
Follow - up：在给定任务和完成时间的情况下，找出最少需要多少个CPU才能让所有任务尽快搞定。

使用二分法, 然后按照上面的思路解决
```python
"""
    方案, 结合cpu_schedule.

    cpu数量[1, len(tasks)], 每次计算最短时间。
    1. 对于给定cpu数量, 计算最短时间
    2. 如果最短时间 满足题目要求, 即:
        2.1 小于给定完成时间
        2.2 比上一次cpu数量时间要短
            right = (left+right)/2
    3. 如果不满足:   
            left = (left_right)/2            

    尝试减少cpu数量, 
"""
from copy import deepcopy


class Solution:
    def min_time(self, tasks, num_cpus):
        mn_time = float('inf')
        finish = [False for _ in range(len(tasks))]
        cpu_time = [0 for _ in range(num_cpus)]
        cpu_schedule = [[] for _ in range(num_cpus)]
        ans = []

        def dfs(n_finish):
            nonlocal mn_time, ans
            if n_finish == len(tasks):
                if max(cpu_time) < mn_time:
                    mn_time = max(cpu_time)
                    ans = deepcopy(cpu_schedule)
                return

            for i in range(len(tasks)):
                if not finish[i]:
                    finish[i] = True
                    n_finish += 1

                    for j in range(num_cpus):
                        tmp_time = cpu_time[j]
                        cpu_time[j] = tasks[i][1] + max(cpu_time[j], tasks[i][0])
                        cpu_schedule[j].append(i)
                        dfs(n_finish)
                        cpu_schedule[j].pop()
                        cpu_time[j] = tmp_time
                    n_finish -= 1
                    finish[i] = False

        dfs(0)
        return mn_time, ans

    def min_cpus(self, tasks, time):
        left = 1
        right = len(tasks)

        while left < right:
            mid = left + (right - left) // 2
            cur_time, _ = self.min_time(tasks, mid)

            if cur_time <= time:
                right = mid
            else:
                left = mid + 1

        return left


tasks = [(0, 5), (1, 3), (2, 1), (4, 2)]
time = 12
print(Solution().min_cpus(tasks, time))
```

29. 给你一个Matrix, 让你写back - propagation。
Follow - up: 做多线程优化。

30.
一堆正方形蛋糕，每个蛋糕有自己的位置和大小。让你找一个垂直切割线的位置，把所有的蛋糕切成两半，而且两边蛋糕的量要一模一样。
```python
class Cake:
    def __init__(self, x, y, width, height):
        self.x = x  # 蛋糕的x坐标
        self.y = y  # 蛋糕的y坐标
        self.width = width  # 蛋糕的宽度
        self.height = height  # 蛋糕的高度


def get_area_below_line(cake, l):
    delta_line = l - cake.y
    if delta_line > cake.height:
        return cake.width * cake.height
    elif delta_line < 0:
        return 0
    else:
        return cake.width * (l - cake.y)


def find_cut_line(cakes):
    # 计算所有蛋糕的总面积
    total_area = sum(cake.width * cake.height for cake in cakes)

    bottom_line = float('inf')
    top_line = -float('inf')

    total_area = 0
    for cake in cakes:
        bottom_line = min(bottom_line, cake.y)
        top_line = max(top_line, cake.y + cake.height)
        total_area += cake.height * cake.width

    l = bottom_line
    r = top_line

    while l < r:
        mid = l + (r - l) / 2
        area_sum = 0
        for cake in cakes:
            area_sum += get_area_below_line(cake, mid)

        if abs(area_sum * 2 - total_area) < 1e-6:
            return mid
        elif area_sum * 2 > total_area:
            r = mid
        else:
            l = mid

    return None


# 示例使用
cakes = [
    (0, 0, 5, 10),  # 蛋糕1：左下角(0,0)，宽5高10
    (0, 10, 6, 12),  # 蛋糕2：左下角(0,10)，宽6高12
    (6, 5, 4, 8)  # 蛋糕3：左下角(5,5)，宽4高8
]

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

plt.xlim(left=0, right=20)
plt.ylim(top=20, bottom=0)
#
for x, y, w, h in cakes:
    rect = mpatches.Rectangle((x, y), w, h,
                              fill=False,
                              color="red",
                              linewidth=2)
    plt.gca().add_patch(rect)

cakes = [Cake(*x) for x in cakes]
cutting_line = find_cut_line(cakes)
print(f"The cutting line is at y = {cutting_line}")

plt.axhline(y=cutting_line, color='g', linestyle='--', linewidth=2)

plt.show()

```

32.[jump game2](https: // leetcode.cn/problems/jump-game-ii/)，
```python

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
            DP
        """
        n = len(nums)
        dp = [float('inf') for _ in range(len(nums))]
        dp[0] = 0

        for i in range(n):
            for j in range(i + 1, min(n - 1, i + nums[i]) + 1):
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[-1]

    def jump(self, nums: List[int]) -> int:
        """
            贪心
        """
        cur_max = nxt_max = 0
        n = len(nums)
        step = 0

        if n <= 1: return 0

        for i in range(n):
            nxt_max = max(nxt_max, i + nums[i])

            if nxt_max >= n - 1: break

            if i >= cur_max:
                cur_max = nxt_max
                step += 1

        return step + 1
```

follow up 1
是如何用dp做 （我是用的greedy），
`dp[i + nums[i]] = min(dp[j], 1 + dp[i])
`
follow up 2
是如果只能每次偶数次跳的格数只能是偶数，奇数只能奇数，要怎么做？
```python
class Solution:
    def jump(self, nums):
        n = len(nums)
        dp = [float('inf') for _ in range(len(nums))]
        dp[0] = 0

        for i in range(n):
            for j in range(i + 1, min(n - 1, i + nums[i]) + 1):
                if dp[i] % 2 == 0 and (j - i) % 2 == 0:
                    dp[j] = min(dp[j], dp[i] + 1)

                if dp[i] % 2 == 1 and (j - i) % 2 == 1:
                    dp[j] = min(dp[j], dp[i] + 1)

        return dp[-1], dp


print(Solution().jump([2, 3, 1, 1, 4]))
```

34. 992. K 个不同整数的最短子数组[CN](https: // leetcode.cn / problems / subarrays -
with-k - different - integers / description /)
```python
from collections import Counter


class Solution:
    def shortest(self, nums, k):
        left = 0
        i = 0

        n = len(nums)
        cnt = Counter()

        min_len = float('inf')
        ans = []
        while i < n:
            cnt[nums[i]] += 1
            while len(cnt) >= k:
                if i + 1 - left < min_len:
                    min_len = i + 1 - left
                    ans = nums[left:i + 1][:]
                elif i + 1 - left == min_len:
                    ans.append(nums[left:i + 1][:])

                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    cnt.pop(nums[left])
                left += 1

            i += 1
        return ans


print(Solution().shortest(nums=[4, 3, 5, 3, 3, 1, 2, 3], k=3))
```
36. set of linear sets，linear sets的意思是[L, R]包含了L到R之间的所有数字。比如[1, 3] = 1， 2， 3.
我们有{[], [], ...[]}一个set的lienar sets，要求a set with minimum number of elements to have the intersections with all elements in the set of linear sets.
```python
"""
问题描述
给定一组 线性区间（线性集），每个区间 [L, R] 包含从 L 到 R 的所有整数，我们的目标是找到一个最小的集合，
包含该集合与每个线性集的交集（即有至少一个元素与每个区间重合）。

解决思路
这个问题可以通过 贪心算法 来解决。我们通过以下步骤来构建解决方案：

排序区间： 首先，我们将所有区间按它们的右端点（R）进行排序。排序的目的是确保我们可以尽量早地选定一个能够与尽可能多的区间发生交集的点。

贪心选择点： 然后，遍历排序后的区间，依次选择点：

对于每一个区间 [L, R]，我们要确保至少有一个点与它发生交集。

如果当前的集合中没有任何一个点与区间 [L, R] 有交集，那么我们就选择区间的右端点 R 作为一个新点，因为这个点能够与当前区间产生交集，
并且它可能还会与后面的区间产生交集。

终止条件： 当我们遍历完所有区间后，得到的点集合就是最小的点集合，能够与所有区间产生交集。

"""
def min_intersection_points(sets):
    # Step 1: Sort the intervals by their right endpoint (R)
    sets.sort(key=lambda x: x[1])

    # Step 2: Initialize a list to store the result points
    points = []

    # Step 3: Process each interval in the sorted list
    for interval in sets:
        # If the last point does not intersect the current interval
        if not points or points[-1] < interval[0]:
            # Add the right endpoint of the current interval to the points list
            points.append(interval[1])

    # Return the number of points that form the minimal set of intersections
    return points


# Example usage:
# sets = [[1, 3], [2, 5], [4, 8], [7, 10]]
# sets = [[1,2],[2,3],[3,4],[4,5]]
sets = [[10, 16], [2, 8], [1, 6], [7, 12]]
result = min_intersection_points(sets)
print(result)  # Output the points of the minimum intersection set
```

38. N个棋手下棋。There is a chess contest between N players.Each chess player has a distinct rank(positive integer number from  1 to N). We assume that in a chess game between two players, the player ranked higher always wins.The ranks remain constant during the contest. Unfortunately, we don 't know the player ranks. But we know the outcome of M games in the following format: Player  # 1 won #2 Player  # 2 won #4 ... Given the results of M games above, are there any players whose rank can be precisely determined?"
使用拓补排序 + BFS解决
```python
from collections import defaultdict, deque


class Solution:
    def rank(self, wins, n):
        graph = defaultdict(list)

        indegrees = [0 for _ in range(n)]

        for a, b in wins:
            graph[a].append(b)
            indegrees[b] += 1

        que = deque()
        ans = []

        cur_rank = []
        for i in range(n):
            if indegrees[i] == 0:
                cur_rank.append(i)
                que.append(i)
        ans.append(cur_rank[:])
        cur_rank.clear()

        while que:
            q_size = len(que)
            for i in range(q_size):
                cur = que.popleft()

                for ne in graph[cur]:
                    indegrees[ne] -= 1
                    if indegrees[ne] == 0:
                        cur_rank.append(ne)
                        que.append(ne)

            ans.append(cur_rank[:])
            cur_rank.clear()

        return ans


print(Solution().rank([[0, 1], [2, 0]], n=3))
```
35. 棋盘路径问题，从左下角出发，到右下角终点，每次只能往右，右上，或右下，求路径总数。
被问了DFS和DP两种做法。
```python


class Solution:
    def uniquePaths_1(self, m: int, n: int) -> int:
        ans = 0
        dirs = [(0, 1), (-1, 1), (1, 1)]

        def dfs(i, j):
            nonlocal ans
            if i == m - 1 and j == n - 1:
                ans += 1

            for d in dirs:
                ii = i + d[0]
                jj = j + d[1]

                if 0 <= ii < m and 0 <= jj < n:
                    dfs(ii, jj)

        dfs(0, 0)
        return ans

    def uniquePaths(self, m: int, n: int) -> int:
        dirs = [(0, 1), (-1, 1), (1, 1)]
        dp = [[0 for _ in range(n)] for i in range(m)]
        for i in range(n):
            dp[0][i] = 1
        """
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1] + dp[i+1][j-1]
        """
        for j in range(1, n):
            for i in range(1, m):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

                if i < m - 1:
                    dp[i][j] += dp[i + 1][j - 1]
        # print(dp[-1][-1])
        return dp[-1][-1]


print(Solution().uniquePaths_1(3, 3))

```

38. most talkative person base on history
heap做
```python
from collections import Counter

"""
类似于群聊的log file，每一行有timestamp， username，text message。

Part 1: 求问找到most talkative的user。很简单hashmap。
Part 2: 找到top k most talkative users，用的heap， 
Part 3: implement helper function parse_log()，主要是string的操作，每一题都问了runtime。
"""


def most_talkative_person(chat_history):
    # 初始化一个字典来记录每个人的发言次数
    # talk_count = {}
    talk_count = Counter()

    # 遍历每条聊天记录
    for record in chat_history:
        talk_count[record['name']] += 1
        # name = record['name']
        # message = record['message']
        #
        # # 更新该人的发言次数
        # if name in talk_count:
        #     talk_count[name] += 1
        # else:
        #     talk_count[name] = 1

    # 找到发言次数最多的人
    # most_talkative = max(talk_count, key=talk_count.get)
    mx_name = ""
    mx_cnt = 0
    for name in talk_count:
        if talk_count[name] > mx_cnt:
            mx_cnt = talk_count[name]
            mx_name = name
    return mx_name, mx_cnt


# 示例输入
chat_history = [
    {"name": "Alice", "message": "Hi, how are you?"},
    {"name": "Bob", "message": "I'm good, thanks! How about you?"},
    {"name": "Alice", "message": "I'm doing well too."},
    {"name": "Alice", "message": "What have you been up to?"},
    {"name": "Bob", "message": "Just working on some stuff."},
    {"name": "Charlie", "message": "Hey everyone!"},
    {"name": "Alice", "message": "Good to hear!"}
]

# 调用函数
most_talkative, count = most_talkative_person(chat_history)
print(f"The most talkative person is {most_talkative} with {count} messages.")
```

39. 写一个4096 * 4096 image的convolution，256 个channel，28 个batch，3 * 3 的kernel，output channel是128 channels。
follow - up: 怎么并行，给出多种并行方案
[conv](https://blog.csdn.net/u012897374/article/details/140221735?spm=1011.2415.3001.5331)
   
40.实时检测数据流里面的party事件有一个不断到来的数据流(user_id, timestamp, place_id)，表示某个用户在某时间出现在某地点。 规则如下：

• 如果用户去往新 place_id，就离开旧 place_id。 party事件：某place_id在过去60分钟内一直有同样的至少100个人。• 需要在第一时间检测party，而不能仅在数据流的report(user_id, timestamp, place_id)API 调用时判断（否则会漏掉一些 party 事件）。

```python
from collections import defaultdict
from collections import deque

"""
要实时检测数据流中的 party 事件，我们可以通过滑动窗口（sliding window）技术来处理每个用户在各个地点的活动记录，并及时检测是否满足 "party" 的条件：某个 place_id 在过去 60 分钟内一直有至少 100 个人。以下是如何设计这个系统的思路。

系统需求回顾：
实时处理：数据流是实时到达的，我们需要实时处理这些事件，而不能依赖于批量报告。

用户活动记录：每个用户的活动是 (user_id, timestamp, place_id)，记录了用户在某个时间出现在某个地点。

party 事件：如果在某个 place_id 上有至少 100 个不同的用户在过去 60 分钟内访问过这个地方，则视为发生了一个 "party" 事件。

解决方案设计：
1. 滑动窗口：
由于 party 事件的判断需要查看过去 60 分钟的数据，所以我们需要使用滑动窗口来保存最近 60 分钟内的数据。这要求我们能够实时更新窗口中的活动记录。

2. 数据结构选择：
使用一个字典或哈希表来记录每个 place_id 和每个时间段内的用户集合。

每个 place_id 对应一个哈希表，哈希表的键是 user_id，值是该用户的最后访问时间（timestamp）。

通过维护每个 place_id 上的用户数据，我们能够快速判断是否满足 "party" 事件的条件。

3. 实时检测：
每当一个新的事件 (user_id, timestamp, place_id) 到来时，首先更新该 place_id 上用户的访问时间。

然后移除 60 分钟之前的用户记录，这样我们总是能够保持每个 place_id 最近 60 分钟的访问记录。

最后检查该 place_id 上在 60 分钟内的独立用户数，如果至少有 100 个不同的用户，则触发 "party" 事件。

"""
from collections import defaultdict


class PartyDetector:
    def __init__(self, windows=60):
        """
            {
                place_id: {user_id: timestamp}
            }

        """
        self.places = defaultdict(defaultdict)
        self.user_places = defaultdict(str)  # {user_id: place_id}
        self.window = windows

    def report(self, user_id, timestamp, place_id):
        if user_id in self.user_places:
            old_place = self.user_places[user_id]
            if old_place != palce_id:
                self.places[old_place].pop(user_id)
        self.places[place_id].update({user_id: timestamp})

    def detect_party(self, timestamp):
        for place_id, user_times in self.places.items():
            for user_id, t in user_times.items():
                if t < timestamp - self.window:
                    # to_remove.append(user_id)
                    self.places.pop(user_id)
                else:
                    break

            users = list(set(self.places[place_id].keys()))

            if len(users) >= 3:
                print(f"found party at place: {place_id} from time {timestamp - self.window} to {timestamp}")


def got_data(data_source=""):
    return 'user1', 1000, 'placeA'  # 示例返回数据


party_detector = PartyDetector()

import time

# 每分钟检查是否有 party 事件
cur_time = 1000
while True:
    # for current_time in range(1000, 1062):
    # 模拟报告数据流
    user_id, timestamp, place_id = got_data()
    assert cur_time == timestamp, 'invalid timestamp'
    if user_id:
        party_detector.report(user_id, timestamp, place_id)

    party_detector.detect_party(cur_time)
    time.sleep(1)  # 模拟 1 秒钟的延迟，表示每次都在不同的时间戳运行检测
    cur_time += 1

```
40.
电话号码的字母组合[CN](
    https: // leetcode.cn / problems / letter - combinations - of - a - phone - number / description /)
41.
设计一个允许赊账的balance
book, 支持扣款付款查询余额功能
要能跑通
```python
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

```
43. 计算器I, 计算器III
44. 最长重复子串 1062
[1316. 不同的循环子字符串 https://leetcode.cn/problems/distinct-echo-substrings/description/?envType=problem-list-v2&envId=KRLwHNJi
DP, s1, s2是否存在公共子串
rabin - karp算法 + 二分
字符串哈希
```python
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        """
            二分法+ 字符串哈希
            O(nlog(n))

            题解: https://www.bilibili.com/video/BV1Lf4y1b78a/?spm_id_from=333.337.search-card.all.click&vd_source=515dedd17a7416a93307429c1b2dfa6b
        """

        def init_hash(self, text):
            self.base = 131

        self.mod_val = 10 ** 9 + 7

        str_hash = [0 for _ in range(1 + len(text))]
        pows = [1 for _ in range(1 + len(text))]

        for i in range(1, len(text) + 1):
            pows[i] = pows[i - 1] * self.base % self.mod_val
            str_hash[i] = (str_hash[i - 1] * self.base + ord(text[i - 1])) % self.mod_val

        self.str_hash = str_hash
        self.pows = pows

    def get_hash(self, left, right):
        """
            [left, right]
        """
        return (self.str_hash[right] - self.str_hash[left] * self.pows[
            right - left] % self.mod_val + self.mod_val) % self.mod_val

        def longestRepeatingSubstring_1(self, s: str) -> int:
            """
                首先判断长度为L的子串是否出现了2次。
                使用哈希表。每遍历到一个位置, 加入set。如果后来还遇到, 则返回True
            """
            init()

    def longestRepeatingSubstring(self, s: str) -> int:
        """
            动态规划: O(n**2)
            相当于求s1, s2的最长公共子串

            题解: https://www.bilibili.com/video/BV1Lf4y1b78a/?spm_id_from=333.337.search-card.all.click&vd_source=515dedd17a7416a93307429c1b2dfa6b
        """
        s = "#" + s
        n = len(s)

        dp = [[0 for i in range(n)] for j in range(n)]

        ans = 0
        for i in range(n):
            for j in range(n):
                if i != j and s[i] == s[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])

        return ans


```

46. 一个data center 有集群，大概就是需要快速分发文件到所有的机器里。 所有集群星行连接同一个switch ，每个wire bandwidth 一致，求最快分发方式。

要考虑多并发和fault tolerance
```python
"""
https://www.1point3acres.com/bbs/thread-1113415-1-1.html Google ng VO 奇怪面经

一个data center 有集群，大概就是需要快速分发文件到所有的机器里。
所有集群星行连接同一个switch ，每个wire bandwidth 一致，求最快分发方式。
我说了个bfs ，面试官认为还不够快，要考虑多并发和fault tolerance
"""


class FileDistribution:
    def __init__(self, machines):
        self.machines = machines  # machines 是一个机器列表
        self.files = {}  # 用于存储每个机器的文件块

    def split_file(self, file):
        # 假设我们将文件分成N块
        file_blocks = [file[i:i + len(file) // 4] for i in range(0, len(file), len(file) // 4)]
        return file_blocks

    def distribute_file(self, file):
        file_blocks = self.split_file(file)

        # 假设我们采用树形分发结构来分发文件块
        for i, block in enumerate(file_blocks):
            # 分发文件块到机器
            self.files[self.machines[i]] = block
            print(f"分发文件块 {i + 1} 到 {self.machines[i]}")

    def get_file(self, machine):
        # 模拟获取文件块
        return self.files.get(machine, None)


# 示例
machines = ['machine1', 'machine2', 'machine3', 'machine4']
file_data = "This is a large file that needs to be distributed across the machines."
distribution = FileDistribution(machines)

# 分发文件
distribution.distribute_file(file_data)

# 查询某台机器的文件块
print(distribution.get_file('machine1'))
```

45. coding1.1: 给定一个包含多个人的 24 小时工作安排表，每个人都有姓名、班次开始时间和结束时间.
编写一个函数，输入该工作安排表和一个时间，然后返回在该时间工作的员工人数。
```python
from typing import List, Tuple


def count_employees_working_at_time(schedule: List[Tuple[str, int, int]], given_time: int) -> int:
    """
    计算给定时间有多少员工正在工作

    :param schedule: 员工的工作时间表，每个员工由姓名、开始时间和结束时间表示
    :param given_time: 给定时间，24小时制整数
    :return: 在该时间工作的员工人数
    """
    count = 0

    for name, start_time, end_time in schedule:
        # 检查给定时间是否在员工的工作时间范围内
        if start_time <= given_time < end_time:
            count += 1

    return count


# 示例
schedule = [
    ("Alice", 9, 17),  # Alice 9:00-17:00
    ("Bob", 8, 16),  # Bob 8:00-16:00
    ("Charlie", 13, 21),  # Charlie 13:00-21:00
    ("David", 12, 18)  # David 12:00-18:00
]

given_time = 15  # 查询 15:00 时在工作的人数
print(count_employees_working_at_time(schedule, given_time))  # 输出 4

```
coding1
.2:
编写一个函数，接收一个工作安排表，并返回一张不包含重叠时段的时间表，说明在每个时间段内谁在工作。
返回一个列表，其中的每个元素也是一个列表，包含“开始时间”、“结束时间”以及在该时间段内工作的人员列表。
```python
from typing import List, Tuple


def merge_schedule(schedule: List[Tuple[str, int, int]]):
    # 按开始时间排序
    schedule.sort(key=lambda x: x[1])  # 按开始时间排序

    ans = []

    cur = []
    t = []
    for item in schedule:
        t.append((item[0], item[1], 1))
        t.append((item[0], item[2], -1))

    t = sorted(t, key=lambda x: (x[1], -x[2]))

    prev_t = None
    for tt in t:
        if tt[2] > 0:
            if cur and tt[1] > prev_t:
                ans.append([prev_t, tt[1], cur[:]])
            cur.append(tt[0])
        else:
            if tt[1] > prev_t:
                ans.append([prev_t, tt[1], cur[:]])
            cur.remove(tt[0])
        prev_t = tt[1]
    return ans


# 示例
schedule = [
    ("Alice", 9, 12),  # Alice 9:00 - 12:00
    ("Bob", 10, 14),  # Bob 10:00 - 14:00
    ("Charlie", 11, 13),  # Charlie 11:00 - 13:00
    ("David", 13, 15),  # David 13:00 - 15:00
    ("Eve", 9, 11),  # Eve 9:00 - 11:00
]

result = merge_schedule(schedule)
for period in result:
    print(period)
```
46.[插入区间](https: // leetcode.com / problems / insert - interval / description /) insert
interval
47.[合并区间](https: // leetcode.com / problems / merge - intervals /)    merge
interval
48.
统计每个数出现的次数是不是都大于一个值
49.
第二道是能不能把一个数组group成每五个连续的数
50.
You are given a m x n grid where each cell contains an integer.Given a start cell(r1, c1) and a target value t, determine if there exists a path from  (r1, c1) to any cell that contains t.The path must only move through cells that have value k(excluding the start and end cells).

followup: 如果grid不規整（每個row有不同column size)怎麼辦
refactor solution so the grid can be abstractized to interface

```python
from typing import List


def is_path_to_target(grid: List[List[int]], r1: int, c1: int, t: int, k: int) -> bool:
    m, n = len(grid), len(grid[0])

    # Directions for moving: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # To store the visited cells
    visited = [[False] * n for _ in range(m)]

    # DFS helper function
    def dfs(r, c):
        # If out of bounds or already visited, return False
        if r < 0 or r >= m or c < 0 or c >= grid[r] or visited[r][c]:
            return False

        # If we reach the target cell
        if grid[r][c] == t:
            return True

        # # If the current cell is not k, we can't move through it
        # if grid[r][c] != k:
        #     return False

        # Mark the current cell as visited
        visited[r][c] = True

        # Explore all four possible directions
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if grid[new_r][new_c] in [k, target] and not visited[new_r][new_c] and dfs(new_r, new_c):
                return True

        visited[r][c] = False
        return False

    # Start the DFS from the given starting cell
    return dfs(r1, c1)


# Example Usage
grid = [
    [1, 7, 7, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
start_row, start_col = 0, 0
target = 11
k = 7

result = is_path_to_target(grid, start_row, start_col, target, k)
print(result)  # Output: True or False
```

51.迭代压缩字符串[CN](https: // leetcode.cn / problems / design - compressed - string - iterator / description /)

输入：
["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
[["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
输出：
[null, "L", "e", "e", "t", "C", "o", true, "d", true]
```python


class StringIterator:

    def __init__(self, compressedString: str):
        self.idx = 0
        self.num = 0
        self.ch = ''
        self.s = compressedString

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.num == 0:
            self.ch = self.s[self.idx]
            self.idx += 1

            while self.idx < len(self.s) and self.s[self.idx].isdigit():
                self.num = 10 * self.num + int(self.s[self.idx])
                self.idx += 1
        self.num -= 1
        return self.ch

    def hasNext(self) -> bool:
        return self.idx != len(self.s) or self.num != 0


s = StringIterator('L1e2t1C1o1d1e1')
print(s.next())
```

51. 232. 用栈实现队列[CN](https: // leetcode.cn / problems / implement - queue - using - stacks / description /)

52. random pick index[EN](https: // leetcode.com / problems / random - pick - index / description /)

53. number of islands[CN](https: // leetcode.cn / problems / number - of - islands / description /), [EN](
    https: // leetcode.com / problems / number - of - islands / description /)

54. 有向图，每个node的value是A, B, C的一种，返回图里是否存在A -> B(可以有一个或者多个) -> C的sequence。从所有A
node开始做dfs，对于A
node的neighbor只加B
node，对于B
node的neighbor只加B
node
或者返回true如果neighbor有C
node。

followup - 1: 要求有两个或以上的A
node指向同一个B
node。先count每个B
node有多少A
node指向它，然后从所有有两个及上的B
node开始遍历做dfs。
followup - 2: 如果sequence存在，要求返回path

```python
from collections import defaultdict


class Solution:

    def has_path(self, edges):
        graph = defaultdict(list)
        visited = defaultdict(bool)
        path = []
        ans = []
        cnt = defaultdict(int)
        for s, t in edges:
            graph[s].append(t)
            if 'A' in s and 'B' in t:
                cnt[t] += 1
            visited[s] = False
            visited[t] = False

        def dfs(cur):
            nonlocal path, ans
            if 'C' in cur:
                ans.append(path[:])
                return True

            if visited[cur]: return False

            visited[cur] = True
            if 'A' in cur:
                for ne in graph[cur]:
                    if 'B' in ne and cnt[ne] >= 2:
                        path.append(ne)
                        dfs(ne)
                        # if dfs(ne): return True
                        path.pop()

            if 'B' in cur:
                for ne in graph[cur]:
                    if 'B' in ne and cnt[ne] >= 2 or 'C' in ne:
                        path.append(ne)
                        dfs(ne)
                        # if dfs(ne): return True
                        path.pop()
            visited[cur] = False
            return False

        for k in graph:
            if 'A' in k:
                path.append(k)
                dfs(k)
                # if dfs(k):
                #     print(ans)
                # return True
                path.pop()
        print(ans)
        return False


edges = [
    ['A1', 'B1'],
    ['A1', 'B2'],
    ['A3', 'B1'],
    ['B1', 'C1'],
    ['B2', 'C2']
]

print(Solution().has_path(edges))
```

55.
sorted数组比如：【1, 2, 2, 3】用重复数组之和替代第一次出现的重复数：[1, 4, 3].面试官要求O（n）时间，O（1） 空间。
```python


class Solution:
    def replace(self, nums):
        left = 0
        prev = 0
        nums.append(None)
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[left] = nums[i - 1] * (i - prev)
                left += 1
                prev = i

        return nums[:left]


print(Solution().replace(nums=[1, 2, 2, 2, 3, 3, 5]))
```

56. 一个游戏有四种颜色共12个牌，让两个玩家每次实现一个move, 一个valid的move是把剩下的牌堆在同一个颜色上或者同一高度上。 实现move（） function。

57.最短路径 给出一个九宫格, 里面分别是数字1 - 9, 然后给出两个数字a, b, a != b 且a, b在1 - 9 之间, 找出所有路径

followup:如果只要最短路径如果对角线也是合法路径怎么处理

58. Let us call some numbers super prime cut(SPC) using the following definition.  If a number is less than 10, then being a prime is equivalent to being SPC.If a number is greater than 10, then the number is SPC if it is both prime, and, the number with the last digit cut off is also SPC.

n < 10: n is SPC <= > n is prime
n > 10: (n is prime and n with the last digit cut off is SPC) <= > n is SPC

For example, 2 is a super prime cut number, because 2 is less than 10 and 2 is a prime number.

As another example, 23 is also a super prime cut number:  23 is greater than 10. 23 is prime. If you remove the last digit of 23, you get 2, which is super prime cut. Implement a function that returns true if a number is a super prime cut number, and false otherwise.

1st followup - generate all super prime it for 1 between n.n - 2 ^ 32 
2nd followup - what if n is 2 ^ 63 - 1

59.给定一个每个人工作的时间表，有开始结束时间和名字，要求输出一个工作表，在每一个时间段有哪些人在工作
比如 （人，开始，结束） (A, 10, 30)(B, 20, 40)(C, 30, 40)
输出
{(10 - 20, A), (20 - 30, A & B), (30 - 40, B & C)

 60. 给一些sentence, 一个文档的宽度width.求文档能填多少行.这里要考虑:
如果当前行空间不够填新单词时候, 要把单词挪到下一行, 不需要拆分单词
如果width宽度过窄, 需要拆分单词
[写字符串需要的行数](https: // leetcode.cn / problems / number - of - lines - to - write - string /)
```python

```
第二轮, 实现两个接口, 一个是insertAd(), 一个是getAd().
insertAd()
是插入一个广告, 里面有两个元素(content, score).
getAd()
时候返回score分最高的content.但是每次getAd(), 分数都会－1, 且不能连续两次getAd返回同一个content内容.
第三轮, input一个数组, 每个元素都是个句子: [[I am sam], [sam I am], [....]], 然后给一个word, 求预测这个word最可能接的next
word是什么.这里应该是统计每个单词的下一个单词出现的频率, 然后返回当前单词最高频率的next
word.

65. 最长公共前缀
66.合并两个有序数组
给你两个按 非递减顺序 排列的整数数组nums1和nums2，另有两个整数m和n ，分别表示nums1和nums2中的元素数目。请你合并nums2到nums1中，使合并后的数组同样按非递减顺序排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组nums1中。为了应对这种情况，nums1的初始长度为m + n，其中前m个元素表示应合并的元素，后n个元素为0 ，应忽略。nums2 的长度为n 。

67. 295. 数据流的中位数

69.
给定多个矩形蛋糕的信息, 一个包含多个蛋糕的列表，每个蛋糕定义为一个对象，找到一个水平切割线, 将所有蛋糕分成两部分，使得：上方部分蛋糕的总面积等于下方部分蛋糕的总面积。
```python

class Cake:
    def __init__(self, x, y, width, height):
        self.x = x  # 蛋糕的x坐标
        self.y = y  # 蛋糕的y坐标
        self.width = width  # 蛋糕的宽度
        self.height = height  # 蛋糕的高度


def get_area_below_line(cake, l):
    delta_line = l - cake.y
    if delta_line > cake.height:
        return cake.width * cake.height
    elif delta_line < 0:
        return 0
    else:
        return cake.width * (l - cake.y)


def find_cut_line(cakes):
    # 计算所有蛋糕的总面积
    total_area = sum(cake.width * cake.height for cake in cakes)

    bottom_line = float('inf')
    top_line = -float('inf')

    total_area = 0
    for cake in cakes:
        bottom_line = min(bottom_line, cake.y)
        top_line = max(top_line, cake.y + cake.height)
        total_area += cake.height * cake.width

    l = bottom_line
    r = top_line

    while l < r:
        mid = l + (r - l) / 2
        area_sum = 0
        for cake in cakes:
            area_sum += get_area_below_line(cake, mid)

        if abs(area_sum * 2 - total_area) < 1e-6:
            return mid
        elif area_sum * 2 > total_area:
            r = mid
        else:
            l = mid

    return None


# 示例使用
cakes = [
    (0, 0, 5, 10),  # 蛋糕1：左下角(0,0)，宽5高10
    (0, 10, 6, 12),  # 蛋糕2：左下角(0,10)，宽6高12
    (6, 5, 4, 8)  # 蛋糕3：左下角(5,5)，宽4高8
]

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

plt.xlim(left=0, right=20)
plt.ylim(top=20, bottom=0)
#
for x, y, w, h in cakes:
    rect = mpatches.Rectangle((x, y), w, h,
                              fill=False,
                              color="red",
                              linewidth=2)
    # facecolor="red")
    plt.gca().add_patch(rect)

cakes = [Cake(*x) for x in cakes]
cutting_line = find_cut_line(cakes)
print(f"The cutting line is at y = {cutting_line}")

plt.axhline(y=cutting_line, color='g', linestyle='--', linewidth=2)

plt.show()

```

70. 给一堆坐标（x, y），问能不能找到三个坐标在同一个线上
```python
两层for循环。
step1: 选择points[i]
作为参考点
step2: 计算points[i]
与其他所有点的斜率, 如果同斜率 >= 2, 则表明有3点共线
```
71.满足条件的最长路径（返回长度，follow up是返回最长路径）用的dfs + backtracking

73.
微波炉
microwave: [设置时间的最少代价](https: // leetcode.cn / problems / minimum - cost - to - set - cooking - time /)
```python
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, sec: int) -> int:
        def calc(s: str) -> int:
            cost = pushCost * len(s)
            cur = startAt
            for ch in s:
                if ord(ch) - ord('0') != cur:
                    cost += moveCost
                    cur = ord(ch) - ord('0')
            return cost

        ans = float('inf')
        if 60 <= sec < 6000:
            ans = calc(f"{sec // 60}{sec % 60 :02}")

        if sec < 100:
            ans = min(ans, calc(str(sec)))  # 仅输入秒数

        elif sec % 60 < 40:
            ans = min(ans, calc(f"{sec // 60 - 1}{sec % 60 + 60}"))  # 借一分钟给秒数

        return ans


print(Solution().minCostSetTime(startAt=1, moveCost=2, pushCost=1, sec=600))

```
74. Maximum Frequency of Number Given a sorted array,   
Example:  
[1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6]  
Answer: 4(3 is repeated 4 times). The time complexity should be better than O(n).  
二分法
```python
from bisect import bisect_left, bisect_right


def findMaxFrequency(nums):
    n = len(nums)
    if n == 0:
        return 0
    max_frequency = 0
    i = 0
    while i < n:
        # 使用二分查找找到当前数字的范围
        num = nums[i]
        left = bisect_left(nums, num)
        right = bisect_right(nums, num) - 1
        max_frequency = max(max_frequency, right - left + 1)
        i = right + 1  # 跳过当前块
    return max_frequency


```

75. 前k个高频(top k frequency)
```python


class Solution:
    def topKFrequent_1(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        que = []
        for item in cnt:  # O(nlog(k))
            heappush(que, (cnt[item], item))

            if len(que) > k:
                heappop(que)
        print(que)
        return [x[1] for x in que]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = list(Counter(nums).items())

        def partition(l, r):
            pivot = cnt[l][:]
            while l < r:
                while l < r and cnt[r][1] <= pivot[1]:
                    r -= 1
                cnt[l] = cnt[r]

                while l < r and cnt[l][1] >= pivot[1]:
                    l += 1
                cnt[r] = cnt[l]

            cnt[l] = pivot
            return l

        left = 0
        right = len(cnt) - 1

        while left < right:
            mid = partition(left, right)
            if mid > k - 1:
                right = mid - 1
            elif mid < k - 1:
                left = mid + 1
            else:
                break

        return [cnt[i][0] for i in range(k)]
```

76. a set of messages消息, 每一个message都带着timestamp，要求把message  
print出来，但是如果在10个timestamp内message出现了重复，后面出现的那个message就不print。  
follow
up是如果出现重复，第一次和第二次的message都不能被print。
```python
from collections import deque, defaultdict


class MessageHandler:
    def __init__(self, window_size=10):
        # 初始化队列和集合
        self.window_size = window_size  # 时间窗口大小，单位为秒
        self.messages = defaultdict(deque)  # 队列，存储消息和时间戳

    def print_message(self, message, timestamp):
        if message in self.messages and timestamp - self.messages[message][-1] < self.window_size:
            pass
            self.messages[message].pop()
            if len(self.messages[message]) == 0:
                self.messages.pop(message)
        else:
            # print(message, timestamp)
            self.messages[message].append(timestamp)


# 示例
handler = MessageHandler()

# 模拟消息和时间戳
messages = [
    ("Hello", 1),
    ("Hi", 5),
    ("Hello", 8),
    ("Hello", 12),
    ("Hi", 15),
    ("Hello", 16),
    ("Hi", 18)
]

for msg, ts in messages:
    handler.print_message(msg, ts)

print(handler.messages)
```

76. 两个 file，第二个包含banned words，要检查第一个file的内容，如果有banned words，就要把那个词换成‘XXX’。 followup问如果第一个file size很大怎么办。

78. 2162. 设置时间的最少代价[CN](https: // leetcode.cn / problems / minimum - cost - to - set - cooking - time / submissions /)
常见的微波炉可以设置加热时间，且加热时间满足以下条件：

78. 外星人字典

79. next word prediction 给定一个有多个句子的list，每个句子也是一个包含多个词语的list。根据每个词的bigram
freq.写一个词语预测。follow
up问了时间空间复杂度，怎么优化空间复杂度这些
bigram
```python
from collections import defaultdict


# 统计 bigram 频率
def build_bigram_freq(sentences):
    # 可以把查找的时候里面设计成最大堆, 节省查找的时间
    # 但是建模的时间更长
    bigram_freq = defaultdict(lambda: defaultdict(int))

    # 遍历每个句子
    for sentence in sentences:
        for i in range(len(sentence) - 1):
            word1 = sentence[i]
            word2 = sentence[i + 1]
            bigram_freq[word1][word2] += 1

    return bigram_freq


# 给定一个词，预测下一个最可能的词
def predict_next_word(word, bigram_freq):
    if word in bigram_freq:
        next_word_freq = bigram_freq[word]
        # 获取频率最高的下一个词
        predicted_word = max(next_word_freq, key=next_word_freq.get)
        return predicted_word
    else:
        return None  # 如果该词后面没有记录，则返回 None


# 示例句子列表
sentences = [
    ["I", "am", "learning", "Python"],
    ["I", "am", "learning", "data", "science"],
    ["I", "like", "Python"],
    ["I", "like", "ML"],
    ["I", "like", "DL"],
    ["Python", "is", "great"]
]

# 构建 bigram 频率字典
bigram_freq = build_bigram_freq(sentences)

# 给定词语，预测下一个词
word = "I"
predicted_word = predict_next_word(word, bigram_freq)
print(f"The next word after '{word}' is: {predicted_word}")
```

79.   KD树
    
```python
import math


class KdNode:
    def __init__(self, point, left=None, right=None):
        self.point = point  # 存储的点
        self.left = left  # 左子树
        self.right = right  # 右子树


class KdTree:
    def __init__(self, points):
        self.root = self.build_tree(points, depth=0)

    def build_tree(self, points, depth):
        if not points:
            return None

        # 选择划分维度，循环使用
        k = len(points[0])  # 假设所有点有相同的维度
        axis = depth % k  # 使用当前深度决定维度

        # 按照当前维度对点进行排序
        points.sort(key=lambda x: x[axis])

        # 找到中位数
        median = len(points) // 2

        # 创建当前节点
        node = KdNode(
            point=points[median],
            left=self.build_tree(points[:median], depth + 1),
            right=self.build_tree(points[median + 1:], depth + 1)
        )

        return node

    def nearest_neighbor(self, target):
        return self._nearest_neighbor(self.root, target, depth=0, best=None)

    def _nearest_neighbor(self, node, target, depth, best):
        if node is None:
            return best

        # 计算当前节点到目标点的距离
        dist = self._distance(node.point, target)

        # 更新最佳点
        if best is None or dist < self._distance(best, target):
            best = node.point

        # 当前轴
        k = len(target)
        axis = depth % k

        # 比较目标点与当前节点的值，决定搜索哪边的子树
        if target[axis] < node.point[axis]:
            best = self._nearest_neighbor(node.left, target, depth + 1, best)
            # 如果可能存在更好的点在右子树中，考虑右子树
            if target[axis] + dist >= node.point[axis]:
                best = self._nearest_neighbor(node.right, target, depth + 1, best)
        else:
            best = self._nearest_neighbor(node.right, target, depth + 1, best)
            # 如果可能存在更好的点在左子树中，考虑左子树
            if target[axis] - dist <= node.point[axis]:
                best = self._nearest_neighbor(node.left, target, depth + 1, best)

        return best

    def _distance(self, point1, point2):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))


points = [
    (1, 1),
    (2, 7),
    (3, 1),
    (4, 1)
]

# 创建 k-d 树
kd_tree = KdTree(points)

# 查询最近邻
# target = (6, 5)
target = (3.1, 7.1)
nearest = kd_tree.nearest_neighbor(target)
print(f"Nearest neighbor to {target} is {nearest}")
```

80. 无向图联通分量数目
方法1: dfs
```python


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False for _ in range(n)]

        def dfs(i):
            for ne in graph[i]:
                if not visited[ne]:
                    visited[ne] = True
                    dfs(ne)

        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += 1
                dfs(i)
        return ans


```

方法2: unionfind, 并查集
```python


class UnionFind:
    def __init__(self, n):
        self.father = [x for x in range(n)]
        self.ans = n

    def find(self, x):
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])

        return self.father[x]

    def union(self, x, y):
        father_x = self.find(x)
        father_y = self.find(y)

        if father_x != father_y:
            self.father[father_x] = father_y
            self.ans -= 1


class Solution:
    def countComponents_1(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False for _ in range(n)]

        def dfs(i):
            for ne in graph[i]:
                if not visited[ne]:
                    visited[ne] = True
                    dfs(ne)

        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += 1
                dfs(i)
        return ans

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)

        return uf.ans


```

81. 上个月面的一题类似227
计算器，但是要判断输入是否合法
input: +(2, 5)
output: 7
input: -(3, *(4, 1))
output: -1
input: 0
output: 0
input: +(3, 3, 3)
需要throw
exception，因为只允许2个参数来运算
```python


class SyntaxException(Exception):
    pass


class DivisionByZeroException(Exception):
    pass


def parse(s, index, sign):
    num1, num2 = 0, 0
    i = index
    # para 1
    if s[i:].startswith("+("):
        num1, i = parse(s, i + 2, "+")
    elif s[i:].startswith("-("):
        num1, i = parse(s, i + 2, "-")
    elif s[i:].startswith("*("):
        num1, i = parse(s, i + 2, "*")
    elif s[i:].startswith("/("):
        num1, i = parse(s, i + 2, "/")
    elif s[i].isdigit():
        while i < len(s) and s[i].isdigit():
            num1 = num1 * 10 + int(s[i])
            i += 1
    else:
        raise SyntaxException(f"invalid char at {i}: {s[i:i + 3]}")
    # comma
    if i == len(s):
        return num1, i
    elif s[i] == ",":
        i += 1
    else:
        raise SyntaxException(f"invalid char at {i}: {s[i:i + 3]}")
    # para 2
    if s[i:].startswith("+("):
        num2, i = parse(s, i + 2, "+")
    elif s[i:].startswith("-("):
        num2, i = parse(s, i + 2, "-")
    elif s[i:].startswith("*("):
        num2, i = parse(s, i + 2, "*")
    elif s[i:].startswith("/("):
        num2, i = parse(s, i + 2, "/")
    elif s[i].isdigit():
        while i < len(s) and s[i].isdigit():
            num2 = num2 * 10 + int(s[i])
            i += 1
    else:
        raise SyntaxException(f"invalid char at {i}: {s[i:i + 3]}")
    if s[i] == ')':
        if sign == "+":
            return num1 + num2, i + 1
        elif sign == "-":
            return num1 - num2, i + 1
        elif sign == "*":
            return num1 * num2, i + 1
        elif sign == "/":
            if int(num2) == 0:
                raise DivisionByZeroException(f"division by zero at {i}: {s[i:i + 3]}")
            return num1 / num2, i + 1
    else:
        raise SyntaxException(f"invalid char at {i}: {s[i:i + 3]}")


def cal(s):
    s = s.replace(" ", "")
    num, i = parse(s, 0, "+")
    return num


```

82. 一个Array，代表第i天航行的距离是arr[i]；能量有限可以选择航行or休息；初始能量k（上限也是k），当天航行能量 - 1，休息 + 1；问最多能航行多远。
```python
class Solution:
    def max_distance(self, arr, k):
        """
            dp[i][j] = max(dp[i-1][j+1]+arr[i], dp[i-1][j-1])

        :param arr:
        :param k:
        :return:
        """
        if k == 0: return 0

        n = len(arr)
        dp = [[0] * (k+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(k):
                # print(i, j)
                # if i==3 and j==0:
                #     print("")
                if j == 0:
                    dp[i+1][j] = dp[i][j+1]+arr[i]
                elif j == k:
                    dp[i+1][j] = dp[i][k]
                else:

                    dp[i+1][j] = max(dp[i][j+1]+arr[i], dp[i][j-1])

        return max(dp[-1])

print(Solution().max_distance(arr = [5, 2, 4, 1, 3], k=3))
print(Solution().max_distance(arr = [6, 7, 8, 5, 4, 3], k = 2))
print(Solution().max_distance(arr = [0, 0, 0, 0], k = 2))
print(Solution().max_distance(arr = [1, 1, 1, 1, 1], k = 5))
print(Solution().max_distance(arr = [10, 1, 1, 10, 1],k = 2))

dp[i][j] = max(dp[i - 1][j + 1] + arr[i], dp[i - 1][j - 1])
n > i - 1 >= 0, 0 <= j - 1 <= k, 0 <= j + 1 <= k
dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j + 1] + arr[i])(注意边界情况)
return max(dp[-1])  # the ith day with j energy, the longest distance

```
83.汇总区间LC[228](https: // leetcode.cn / problems / summary - ranges / submissions / 542756333 /)

85.
given two arrays, implement next() func to iterate through two arrays, array b is array a 's subarray. iterate array b first, then array a.No duplicate (bug free required) follow up: array b's elements are in order as array a. iterate them follow up: the side effect of the recursive function call  
86. Trucate message messages is: (A, 50), (B, 20), (C, 1000), (D, 50).(E, 400).Suppose  
解法: 二分法  

87.
给你一个bookshelf
里面有
不同的书
每本书有
name，author
等， name不是唯一的
可能会重复
还有个需求是
整个bookshelf
包含一个bookmark，这个bookmark只指向一本书
在
removeFromShelf
和
moveFromShelf的同时
也需要同时移除
或者
移动到新的位置
让你设计一个class
里面需要实现一些基本的功能实现
addToShelf(toIndex, list)
把当前的list的书加到bookshelf的list里面
从toIndex的位置开始
removeFromShelf(index)
把当前的index的书移除
moveFromShelf(fromIndex， toIndex， number) 例子
list里面有10本书
number等于2
fromIndex等于0
toIndex等于5
你需要把
0 - 1
的书移到
5 - 6
的位置
getBooks()
把当前的已在bookshelf的全部返回
getBookmark()
返回bookmark值
值得讲一下
bookmark
可以主动的去设置某本书
想象自己主动加个功能去做这个事
比如
6.
setBookmark(index)
使用double
linkedlist + hashmap

92.
O(1)
时间插入, 删除, 获取
double
linkedlist + hashmap
93.
1.
a
list
of
lists
with three elements representing person_number，start_day, and end_day inclusively.
94.
最大天数
3.
人数
参数
1
代表有哪些人在哪段时间不在
Output：
输出能够凑齐所有人的天数
题目挺简单的，用了扫描线
https: // leetcode.com / discuss / post / 4763526 / google - onsite - by - anonymous_user - 2
akx /
95.
电面，就一道类似于LRU的题。大概意思是，
用户在点开搜索框后，提供最近的K个搜索输入作为关键词推荐。然后这次的输入也将用于下次的推荐。例子：
search
history:
paris
tokyo
seattle
K = 2， 那么应该给出的就是：
paris
tokyo
注意：需要按时间排序，最近的搜索历史应该排在前面。如果历史里有重复的，就只记最近的一次。
follow - up: 如何k是一百万怎么办。
用sortedlist, 注意分布式负载均衡。

96.
不用递归, 返回第n个斐波拉契数
97.
用栈实现队列[用栈实现队列](
    https: // leetcode.cn / problems / implement - queue - using - stacks / submissions / 533499452 /)
98.[实现最小栈](https: // leetcode.cn / problems / min - stack / submissions / 533475057 /)
99.
binary
search
tree, 每个node有数值value和subtree的节点总数, 返回第n小的数
[EN](https: // leetcode.com / problems / kth - smallest - element - in -a - bst / description /)
100.
滑动窗口的平均值
输入一堆数，返回给定window
size的平均数, follow
up，返回平均数的时候，忽略最大的k个数
使用sortedList, Klg(N)
101.
大概就是给两个list，一组人的出生年份，和他们的死亡年份，然后找出一定范围内的年份中间哪个年份的人口最多。当然了，出生年份和死亡年份有重叠。

使用扫描线算法来做[1854](
    https: // leetcode.cn / problems / maximum - population - year / solutions / 766081 / ren - kou - zui - duo - de - nian - fen - by - leetcode - 5
m7r4 /)

101 数据流的平均值(滑动窗口平均值)
```python


class MovingAverage:

    def __init__(self, size: int):
        self.nums = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.nums) == self.size:
            self.sum -= self.nums.popleft()
        self.nums.append(val)
        self.sum += val

        return self.sum / len(self.nums)


```
102. MK平均值
deque + sortedList
```python
from collections import deque
from math import floor
from sortedcontainers import SortedList

M, K = 0, 0
DENO = 1  # 分母
curSum = 0
sl = SortedList()
queue = deque()


class MKAverage:
    def __init__(self, m: int, k: int):
        """用一个空的数据流和两个整数 m 和 k 初始化 MKAverage 对象
        """
        global M, K, DENO, sl, queue, curSum
        M, K = m, k
        DENO = M - 2 * K  # 分母，题目保证为正整数
        curSum = 0
        sl.clear()
        queue.clear()

    def addElement(self, num: int) -> None:
        """往数据流中插入一个新的整数 num ,1 <= num <= 1e5
        """
        global sl, queue, curSum
        queue.append(num)

        if len(queue) == M:
            # 初始化
            sl = SortedList(queue)
            curSum = sum(sl[K:-K])

        if len(queue) > M:
            # 加入后对区间和的影响，num会把sortedList里的元素挤到左边或者右边
            pos = sl.bisect_left(num)
            if pos < K:
                # 被挤到中间来了
                curSum += sl[K - 1]
            elif K <= pos <= M - K:
                curSum += num
            else:
                # 被挤到中间来了
                curSum += sl[M - K]
            sl.add(num)

            # 从deque里出来一个数对区间和的影响
            popped = queue.popleft()
            pos = sl.bisect_left(popped)
            if pos < K:
                # 左移
                curSum -= sl[K]
            elif K <= pos <= M - K:
                curSum -= popped
            else:
                # 右移
                curSum -= sl[M - K]
            sl.remove(popped)

    def calculateMKAverage(self) -> int:
        """对当前的数据流计算并返回 MK 平均数 ，结果需 向下取整到最近的整数 。
        """
        if len(sl) < M:
            return -1
        return floor(curSum / DENO)


```

103. 输入3个array，一个int D 找出how many tuples(i, j, k)  
满足以下所有条件  
| A[i] - B[j] | <= D  
| A[i] - C[k] | <= D  
| B[j] - C[k] | <= D  
新题，从没见过
先排序, 然后使用二分来做
```python
import bisect


class Solution:
    def num_triplets_1(self, a, b, c, d):
        ans = 0
        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(c)):
                    if abs(a[i] - b[j]) <= d and abs(a[i] - c[k]) <= d and abs(b[j] - c[k]) <= d:
                        ans += 1
        return ans

    def num_triplets(self, a, b, c, d):
        a = sorted(a)  # nlg(n)
        b = sorted(b)
        c = sorted(c)
        ans = 0
        for i in range(len(a)):
            x = a[i]
            l = bisect.bisect_left(b, x - d)
            r = bisect.bisect_right(b, x + d)

            for j in range(l, r):
                min_val = max(b[j] - d, a[i] - d)
                max_val = min(b[j] + d, a[i] + d)

                ll = bisect.bisect_left(c, min_val)
                rr = bisect.bisect_right(c, max_val)

                ans += rr - ll

        return ans

# import numpy as np
# a = np.random.randint(0, 10, (10,))
# b = np.random.randint(0, 10, (10,))
# c = np.random.randint(0, 10, (10,))

a = [9, 0, 3, 1, 3, 3, 9, 6, 9, 9]
b = [4, 7, 4, 9, 1, 2, 2, 0, 5, 7]
c = [4, 0, 3, 7, 8, 9, 5, 6, 0, 4]

print(Solution().num_triplets_1(a, b, c, d=4))

# print(",".join(str(a).split(" ")))
# print(",".join(str(b).split(" ")))
# print(",".join(str(c).split(" ")))
```

104. 湖泊数量 number of lakes
```cpp
{{'.', '.', '.', '.', '.', '.', '.', '.', '.'},
 {'x', 'x', 'x', '.', '.', 'x', 'x', 'x', '.'},
 {'x', '.', 'x', '.', 'x', '.', '.', 'x', '.'},
 {'x', 'x', '.', 'x', '.', 'x', '.', 'x', '.'},
 {'x', '.', '.', 'x', '.', 'x', 'x', '.', '.'},
 {'.', '.', '.', 'x', 'x', '.', '.', '.', '.'},
 {'.', '.', '.', '.', '.', '.', '.', '.', '.'}};
```

解决方案
```python
"""
1. 从给定的坐标(x, y) 出发, 用floodfill算法将所有的陆地的格子存入到一个set中。
"""
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右方向


def is_valid(x, y, ocean, visited):
    """检查坐标(x, y)是否在合法范围内，并且该位置尚未被访问过"""
    return 0 <= x < len(ocean) and 0 <= y < len(ocean[0]) and ocean[x][y] == 'x' and (x, y) not in visited


def flood_fill_land(ocean, x, y, visited):
    """Flood fill 从给定坐标 (x, y) 开始，找到所有的陆地并存入到 set 中"""
    stack = [(x, y)]
    visited.add((x, y))  # 记录已访问过的格子
    land_cells = set()  # 用于存储所有的陆地格子

    while stack:
        cx, cy = stack.pop()
        land_cells.add((cx, cy))  # 将当前格子加入陆地集合

        # 遍历四个方向
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny, ocean, visited):
                visited.add((nx, ny))
                stack.append((nx, ny))

    return land_cells


# 示例
ocean = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "x", "x", ".", ".", ".", "x", ".", ".", ".", "."],
    [".", "x", ".", ".", ".", "x", ".", "x", ".", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", "x", ".", ".", "."],
    [".", "x", "x", "x", ".", "x", "x", "x", ".", ".", "."],
    [".", "x", ".", "x", ".", "x", ".", "x", ".", ".", "."],
    [".", "x", "x", "x", ".", "x", ".", "x", "x", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", ".", "x", ".", "."],
    [".", ".", ".", ".", ".", "x", "x", "x", "x", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
]

point = (1, 1)  # 假设从 (1, 1) 开始

# 创建一个访问过的集合
visited = set()

# 获取所有陆地格子
land_cells = flood_fill_land(ocean, point[0], point[1], visited)
print(land_cells)

"""
第2步, 根据这些陆地的cell, 人为构造一个更小的矩形框, 最外面一层是水。然后里面就是原来的岛屿和水域, 从而缩小搜索面积。
"""


def construct_subgrid(ocean, land_cells):
    """根据陆地格子，构造一个更小的矩形框"""
    if not land_cells:
        return []

    # 找到陆地格子的最小和最大 x 和 y 坐标
    min_x = min(cell[0] for cell in land_cells)
    max_x = max(cell[0] for cell in land_cells)
    min_y = min(cell[1] for cell in land_cells)
    max_y = max(cell[1] for cell in land_cells)

    # 构建新的子网格，大小为 (max_x - min_x + 3) x (max_y - min_y + 3)
    # 外围一层水域，再加上原始的岛屿和水域
    subgrid = [['.'] * (max_y - min_y + 3) for _ in range(max_x - min_x + 3)]

    # 将原始的岛屿和水域映射到新的子网格
    for x, y in land_cells:
        new_x = x - min_x + 1  # 使得最小的 x 对应子网格的第一个位置
        new_y = y - min_y + 1  # 使得最小的 y 对应子网格的第一个位置
        subgrid[new_x][new_y] = 'X'

    # 返回构造好的子网格
    return subgrid


# 示例
ocean = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "x", "x", ".", ".", ".", "x", ".", ".", ".", "."],
    [".", "x", ".", ".", ".", "x", ".", "x", ".", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", "x", ".", ".", "."],
    [".", "x", "x", "x", ".", "x", "x", "x", ".", ".", "."],
    [".", "x", ".", "x", ".", "x", ".", "x", ".", ".", "."],
    [".", "x", "x", "x", ".", "x", ".", "x", "x", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", ".", "x", ".", "."],
    [".", ".", ".", ".", ".", "x", "x", "x", "x", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]

# 假设从 (1, 1) 开始，得到陆地的集合
land_cells = flood_fill_land(ocean, 1, 1, set())

# 构建新的子网格
subgrid = construct_subgrid(ocean, land_cells)

# 打印新的子网格
for row in subgrid:
    print(''.join(row))

"""
第三步, 对于新的子网格, 从有水的格子开始, 用洪水填充算法。如果最终碰到了边界, 则表明是属于海洋, 不是湖泊。如果最终都没有碰到边界, 则表明是一个内部湖泊, 湖泊数量加一。然后将以上遍历过程中所有岛屿对应的湖泊数量用一个哈希表存起来, 方便后面如果碰到了可以直接返回。
"""


def flood_fill_water(ocean, x, y, visited, is_ocean=False):
    """Flood fill 算法，判断该水域是否属于海洋。如果与边界接触，则是海洋。"""
    stack = [(x, y)]
    visited.add((x, y))
    water_cells = set()

    while stack:
        cx, cy = stack.pop()
        water_cells.add((cx, cy))

        # 如果当前格子触及边界，则是海洋
        if cx == 0 or cx == len(ocean) - 1 or cy == 0 or cy == len(ocean[0]) - 1:
            is_ocean = True

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny, ocean, visited) and ocean[nx][ny] == ".":
                visited.add((nx, ny))
                stack.append((nx, ny))

    return water_cells, is_ocean


def count_lakes_in_subgrid(ocean, land_cells):
    """ 在缩小的矩阵内计算湖泊的数量 """
    visited = set()
    lakes = 0
    island_lake_map = {}  # 用于缓存每个岛屿的湖泊数量

    # 对每个水域格子进行洪水填充，检查是否是湖泊
    for x in range(1, len(ocean) - 1):
        for y in range(1, len(ocean[0]) - 1):
            if ocean[x][y] == "." and (x, y) not in visited:
                # 使用洪水填充检查这个水域是否是海洋
                water_cells, is_ocean = flood_fill_water(ocean, x, y, visited, is_ocean=False)

                if is_ocean:
                    # 如果是海洋，不计入湖泊
                    continue
                else:
                    # 如果不是海洋，就是湖泊
                    lakes += 1

                # 将所有水域标记为已访问
                visited.update(water_cells)

    return lakes


# 示例
ocean = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "x", "x", ".", ".", ".", "x", ".", ".", ".", "."],
    [".", "x", ".", ".", ".", "x", ".", "x", ".", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", "x", ".", ".", "."],
    [".", "x", "x", "x", ".", "x", "x", "x", ".", ".", "."],
    [".", "x", ".", "x", ".", "x", ".", "x", ".", ".", "."],
    [".", "x", "x", "x", ".", "x", ".", "x", "x", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", ".", "x", ".", "."],
    [".", ".", ".", ".", ".", "x", "x", "x", "x", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]

# 假设从 (1, 1) 开始，得到陆地的集合
land_cells = flood_fill_land(ocean, 1, 1, set())

# 构建新的子网格
subgrid = construct_subgrid(ocean, land_cells)

# 计算湖泊的数量
lakes = count_lakes_in_subgrid(subgrid, land_cells)
print(f"湖泊数量：{lakes}")
```

105.[806.写字符串需要的行数](https://leetcode.cn/problems/number-of-lines-to-write-string/description/)


106.[二叉树中的最大路径和](https: // leetcode.cn / problems / binary - tree - maximum - path - sum / description /)


107. 最大连续1的个数 485

     
109. To determine if the paths of two robots in a 2 - dimensional space intersect based on the given instructions(F for forward, L for turn left, R for turn right), and then check whether their paths overlap at any point.
判断2个机器人的路径是否相交
将第一个机器人的路径描绘出来。然后看第二个机器人走的每一步是否在第一个机器人中出现过。
空间复杂度改为O(1), 链表是否相交:
```python

class Robot:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.cur_dir = 1
        """
            |(0)
       (3) - - (1)
            |(2)

        """
        self.dir_map = {
            0: (-1, 0),
            1: (0, 1),
            2: (1, 0),
            3: (0, -1)
        }

    def step(self, action):
        """
            F for forward, L for turn left, R for turn right
        :param action:
        :return:
        """
        if action == 'L':
            self.cur_dir = (self.cur_dir + 3) % 4
        elif action == 'R':
            self.cur_dir = (self.cur_dir + 1) % 4
        else:
            self.start_x += self.dir_map[self.cur_dir][0]
            self.start_y += self.dir_map[self.cur_dir][1]

        return (self.start_x, self.start_y)


class Solution:
    def robot_intersect(self, start1, dir1, start2, dir2):

        robot1 = Robot(*start1)
        robot2 = Robot(*start2)

        d1 = dir1
        d2 = dir2
        pt1 = start1
        pt2 = start2

        i = 0
        j = 0
        while pt1 != pt2:
            if i < len(dir1):
                pt1 = robot1.step(dir1[i])
                i += 1
            elif i == len(dir1):
                pt1 = (-1, -1)
            else:
                i = 0
                pt1 = start2
                dir1 = d2
                robot1 = Robot(*start2)

            if j < len(dir2):
                pt2 = robot2.step(dir2[j])
                j += 1
            elif j == len(dir2):
                pt2 = (-1, -1)
            else:
                j = 0
                pt2 = start1
                dir2 = d1
                robot2 = Robot(*start1)
            print(f"pt1: {pt1}, pt2: {pt2}")
        print(pt1)
        return pt1 != (-1, -1)


print(Solution().robot_intersect(
    start1=(0, 0), dir1="FFRFFF",
    start2=(1, 0), dir2="RFFLFF"
))

"""
robot1 = "FFRFFR"
robot2 = "RFFLFF"
# 机器人1路径: (0,0)->(0,1)->(0,2)->(0,2)->(1,2)->(2, 2)->(3, 2)
# 机器人2路径: (1,0)->(1,0)->(2,0)->(3,0)->(3,0)->(3, 1)->(3, 2)
# ✅ 交点: (2,2)
"""

```
109. 搭积木问 bfs
110. 找多维空间距离最近的点 KD树
111.中心对称数
112. 会议室2
113. 出的题是：the most frequent repeating substring that appears at least 3 times.
例子： aaaaabc > aaa
aaabc > a
直接数单个字母最长的数目n, 答案n - 2
114. 最长递增子数组 Given an array of size N, find the maximum length of non - decreasing subarray:
[0 7 3 10 2 4 6 8 0 9 - 20 4]
ans = 4, [2 4 6 8]

Follow up: You can choose any one index and change its value to any number that you like.What will be the longest non decreasing subarray now:  In the same example as before, the answer would now be:
ans = 6, [2 4 6 8 0 9], by changing 0 -> 8 so the subarray becomes non - decreasing.
```python
"""
最长递增子数组
"""

def max_increasing_subarr(arr):
    i = 0
    cur = 1
    ans = 1
    while i < len(arr):
        if i + 1 < len(arr) and arr[i] <= arr[i + 1]:
            cur += 1
        else:
            cur = 1
        ans = max(ans, cur)
        i += 1
    return ans
```

followup: 可以修改其中某一个值
```python
def maxIncreasingSubWithChange(arr):
    n = len(arr)
    if n <= 1:
        return n
    left = [1] * n  # left[i] is the max increasing subarray ending at i
    right = [1] * n  # right[i] is the max increasing subarray starting at i

    # 从左往右
    for pos in range(1, n):
        if arr[pos] >= arr[pos - 1]:
            left[pos] = left[pos - 1] + 1

    print(f"max len: {max(left)}")

    # 从右往左
    for pos in range(n - 2, -1, -1):
        if arr[pos] <= arr[pos + 1]:
            right[pos] = right[pos + 1] + 1

    max_res = max(left)
    # 修改pos[i]的值
    for pos in range(1, n - 1):
        if arr[pos - 1] <= arr[pos + 1]:
            # [#We](https://leetcode.com/problems/power-of-two) consider changing the element at pos

            max_res = max(max_res, left[pos - 1] + right[pos + 1] + 1)

        """
        防止这种[1, 2, 3, 4, 0, 3], 只能改1个0
        """
        for pos in range(n - 1):
            if arr[pos + 1] < arr[pos]:
                max_res = max(res, left[pos] + 1)
    # Consider changing the first element
    # 修改数组第一个值
    max_res = max(max_res, right[1] + 1)

    # Consider changing the last element
    # 修改数组最后一个值
    max_res = max(max_res, left[n - 2] + 1)
    return max_res


```
115.断开所有叶子节点的连接 cut leaf from root given a binary tree, with each edge having a cost associated.we want to cut the edges in such a way that all the leaf nodes get disconnected.find the min cost. given a binary tree, with each edge having a cost associated.we want to cut the edges in such a way that all the leaf nodes get disconnected from root which is 6. find the min cost.
如果是断开所有leaf node叶子节点与root之间的连接

```python
class TreeNode:
    def __init__(self, val, edge_cost, left=None, right=None):
        self.val = val
        self.edge_cost = edge_cost
        self.left = left
        self.right = right


class Solution:
    def min_cost(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.edge_cost

        left = 0
        right = 0
        if root.left is not None:
            left = self.min_cost(root.left)

        if root.right is not None:
            right = self.min_cost(root.right)

        # special case for handling root node
        if root.edge_cost == 0:
            # 该节点为root
            return left + right
        else:
            # 非root, 两种情况
            return min(left + right, root.edge_cost)


root = TreeNode(6, 0)
root.left = TreeNode(4, 5)
root.right = TreeNode(2, 1)
root.left.left = TreeNode(1, 10)

print(Solution().min_cost(root))
```

116. Find string in an HTML DOM
![在这里插入图片描述](https: // i - blog.csdnimg.cn / direct / 7
f50855ad5a44819932973b9f21295ed.png)

方法:
1 将所有的leaf node放到1个list里面
2 使用dfs暴力搜索

如果要返回能否拼接, True / False, 则可以使用DP
dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])
初始条件, 单个字符dp[i][i]
可以看是否能有某个单词的某位字符构成。有True, 没False.
```python
from collections import deque

"""
dfs暴搜
"""


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
                            cur_s = cur_s + leaf_nodes[i][0][:j + 1]
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

```
117.
美国大选
获胜可能性
方法1: dfs暴力搜索
方法2: DP
背包问题
```python
from pprint import pprint


def fin_domb(nums, target):
    n = len(nums)
    s = sum(nums)

    ans = 0
    dp = [[0 for _ in range(s + 1)] for i in range(n + 1)]

    # dp[i][j] top i states, win j votes

    for i in range(n + 1):
        dp[i][0] = 1

    for j in range(1, s + 1):
        for i in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]
            if j - nums[i - 1] >= 0:
                dp[i][j] += dp[i - 1][j - nums[i - 1]]
    for i in range(target, s + 1):
        ans += dp[-1][i]
    return ans


"""
    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
"""
print(fin_domb([2, 4, 7], 5))

"""
7
2 4
2 7
4 7
2 4 7
"""
```
118.
一条收费公路上有许多检查点（Checkpoint），每次一辆车通过一个检查点时，其车牌号和检查点名称都会被记录下来。在一天结束时，需要计算账单并发送给客户。
输入是一个log文件，里面记录了license
checkpoint
timestamp。要求输出每个车的账单。

首先沟通问题。看看到底是类似高速路。
还是应该用图graph来建模
速度要快

119.
抛一个6面的骰子，连续抛直到6为止，问期望的抛的次数是多少

设期望次数为E, 那么有：
[1]
1
次抛出6的概率为1 / 6，那么期望次数为1 * 1 / 6
[2]
本次抛出非6数字的概率为5 / 6，因为没有抛出6，因此期待抛出6还需要执行试验的次数仍为E，需要注意加上本次（1
次）失效的抛掷，即期望次数为(1 + E)(5 / 6)

综合可得：
E = 1 * (1 / 6) + (1 + E)(5 / 6)

解得: E = 6

120
leetcode排行榜LeaderBoard[力扣排行榜](https: // leetcode.cn / problems / design - a - leaderboard / description /)
使用hashmap + sortedList
```python


class Leaderboard:

    def __init__(self):
        self.id_score = defaultdict(int)
        self.scores = SortedList()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.id_score:
            self.scores.remove(self.id_score[playerId])

        self.id_score[playerId] += score
        self.scores.add(self.id_score[playerId])

    def top(self, K: int) -> int:
        # print(self.scores.values())
        return sum(self.scores[-K:])

    def reset(self, playerId: int) -> None:
        # del self.scores[playerId]
        self.scores.remove(self.id_score[playerId])
        self.id_score.pop(playerId)


```
121.
判断一堆圆是否属于同一个group, 圆相交则属于同一个group
Problem: A
circle is define
by
x - axis
position, y - axis
position, and a
radius.A
circle
group is a
collection
of
circles
that
overlap.Given
a
list
of
circles, figure
out if they
belong
to
a
single
circle
group.Formula
for calculating distance between two points: sqrt((x2 - x1) ^ 2 + (y2 - y1) ^ 2)

类似[引爆最多的炸弹](
    https: // leetcode.cn / problems / detonate - the - maximum - bombs / solutions / 1152450 / jian - tu - bao - li - mei - ju - suo - you - qi - dian - by - h4mj /)
step
1.
O(n ** 2)
简图, 相交则有1个无向边
step2: 任意1个node出发做dfs, 如果能遍历所有的node, 则True, 否则No.O(n ** 2)
方法1： 并查集
方法2: 洪水覆盖。从0号出发覆盖, 如果能全部覆盖到, True。否则False
```python


class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius


from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.fathers = [x for x in range(n)]
        self.cnt = n

    def find(self, x):
        if self.fathers[x] != x:
            self.fathers[x] = self.find(self.fathers[x])
        return self.fathers[x]

    def union(self, x, y):
        father_x = self.find(x)
        father_y = self.find(y)
        if father_x != father_y:
            self.fathers[father_x] = father_y
            self.cnt -= 1


class Solution:
    def is_one_group(self, circles):
        # graph = defaultdict(list)

        n = len(circles)
        uf = UnionFind(n)

        def l2_distance_squre(circle_1, circle_2):
            return (circle_1.center_x - circle_2.center_x) ** 2 + (circle_1.center_y - circle_2.center_y) ** 2

        for i in range(n):
            for j in range(i + 1, n):
                if l2_distance_squre(circles[i], circles[j]) <= (circles[i].radius + circles[j].radius) ** 2:
                    uf.union(i, j)

        return uf.cnt


print(Solution().is_one_group(
    # [Circle(0, 0, 3), Circle(4, 0, 3), Circle(2, 3, 2)],
    # [Circle(0, 0, 5), Circle(0, 0, 3)],  # 期望输出: 同一组
    [Circle(0, 0, 3), Circle(4, 0, 3),
     Circle(2, 3, 2), Circle(10, 10, 1)],  # 期望输出: 前三个同一组，第四个不同组
))
```
洪水覆盖法:
```python


class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius


from collections import defaultdict


class Solution:
    def is_one_group(self, circles):
        graph = defaultdict(list)
        n = len(circles)
        visited = [False] * n

        def l2_distance_squre(circle_1, circle_2):
            return (circle_1.center_x - circle_2.center_x) ** 2 + (circle_1.center_y - circle_2.center_y) ** 2

        for i in range(n):
            for j in range(i + 1, n):
                if l2_distance_squre(circles[i], circles[j]) <= (circles[i].radius + circles[j].radius) ** 2:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [0] * n

        def dfs(node):
            visited[node] = 1

            for ne in graph[node]:
                if not visited[ne]:
                    dfs(ne)

        dfs(0)
        return sum(visited) == n


print(Solution().is_one_group(
    # [Circle(0, 0, 3), Circle(4, 0, 3), Circle(2, 3, 2)],
    [Circle(0, 0, 5), Circle(0, 0, 3)],  # 期望输出: 同一组
    # [Circle(0, 0, 3), Circle(4, 0, 3),
    #  Circle(2, 3, 2), Circle(10, 10, 1)],  # 期望输出: 前三个同一组，第四个不同组
))
```
122.
给两个矩阵， 1
是石头
0
是水。判断你能否从第一行走到最后一行（可以4各方向上下左右走）
例子:
[[0, 1, 0, 1, 1],
 [0, 1, 1, 0, 1],
 [0, 0, 1, 1, 0],
 [0, 0, 0, 1, 1]]
True

[[0, 1, 0, 1, 1],
 [0, 1, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [0, 0, 0, 1, 1]]
False
```python


class Solution:
    def paths(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        visited = set()

        def dfs(i, j):
            if i == m - 1:
                return True
            visited.add((i, j))
            for di, dj in dirs:
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in visited and matrix[ii][jj] == 1:
                    if dfs(ii, jj):
                        return True
            visited.remove((i, j))
            return False

        for i in range(n):
            if matrix[0][i] == 1 and dfs(0, i):
                return True

        return False


print(Solution().paths(
    [[0, 1, 0, 1, 1],
     [0, 1, 1, 0, 1],
     [0, 0, 1, 1, 0],
     [0, 0, 0, 1, 1]]

    # [[0, 1, 0, 1, 1],
    # [0, 1, 1, 0, 1],
    # [0, 0, 0, 1, 0],
    # [0, 0, 0, 1, 1]]
))

```
Follow
up:
- 具体怎么走？
求1条路径
```python


class Solution:
    def paths(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        visited = set()
        path = []
        ans = []

        def dfs(i, j):
            nonlocal ans
            if i == m - 1:
                ans.append((path + [(i, j)])[:])
                return True

            path.append((i, j))
            visited.add((i, j))
            for di, dj in dirs:
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in visited and matrix[ii][jj] == 1:
                    dfs(ii, jj)
                    if dfs(ii, jj):
                        return True
            visited.remove((i, j))
            path.pop()
            return False

        for i in range(n):
            if matrix[0][i] == 1 and dfs(0, i):
                return True, ans

        return False, []


print(Solution().paths(
    [[0, 1, 0, 1, 1],
     [0, 1, 1, 0, 1],
     [0, 0, 1, 1, 1],
     [0, 0, 0, 1, 1]]

    # [[0, 1, 0, 1, 1],
    # [0, 1, 1, 0, 1],
    # [0, 0, 0, 1, 0],
    # [0, 0, 0, 1, 1]]
))
```
求所有的path
```python


class Solution:
    def paths(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        visited = set()
        path = []
        ans = []

        def dfs(i, j):
            nonlocal ans
            if i == m - 1:
                ans.append((path + [(i, j)])[:])
                return True

            path.append((i, j))
            visited.add((i, j))
            for di, dj in dirs:
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in visited and matrix[ii][jj] == 1:
                    dfs(ii, jj)
                    # if dfs(ii, jj):
                    #     return True
            visited.remove((i, j))
            path.pop()
            return False

        for i in range(n):
            if matrix[0][i] == 1 and dfs(0, i):
                pass
                # return True, ans
        return ans
        # return False, []


print(Solution().paths(
    [[0, 1, 0, 1, 1],
     [0, 1, 1, 0, 1],
     [0, 0, 1, 1, 1],
     [0, 0, 0, 1, 1]]

    # [[0, 1, 0, 1, 1],
    # [0, 1, 1, 0, 1],
    # [0, 0, 0, 1, 0],
    # [0, 0, 0, 1, 1]]
))

```
- 多少走法.
```python
return len(paths)
```
方法: dfs搜索
bfs搜索, 使用parent数组记录父亲节点
```python
from collections import deque


def canReach(matrix):
    # 获取矩阵的大小
    rows, cols = len(matrix), len(matrix[0])

    # 定义四个方向：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 广度优先搜索（BFS）
    def bfs():
        queue = deque()  # 使用队列
        # 标记访问过的位置
        visited = [[False] * cols for _ in range(rows)]
        parent = [[None] * cols for _ in range(rows)]  # 用于记录每个位置的父节点

        # 将第一行的所有 1 加入队列
        for c in range(cols):
            if matrix[0][c] == 1:
                queue.append((0, c))
                visited[0][c] = True

        # 开始 BFS
        while queue:
            r, c = queue.popleft()

            # 如果到达最后一行，返回 True
            if r == rows - 1:
                # 记录路径
                path = []
                while r is not None and c is not None:
                    path.append((r, c))
                    r, c = parent[r][c]
                path.reverse()  # 路径是反向的，需反转
                print("Path:", path)
                return True

            # 检查相邻的四个方向
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # 判断是否越界、是否是石头、是否访问过
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    parent[nr][nc] = (r, c)  # 记录父节点
                    queue.append((nr, nc))

        # 如果队列为空，说明无法到达最后一行
        return False

    # 调用 BFS
    return bfs()


# 测试例子
matrix = [
    [0, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1]
]

print(canReach(matrix))  # 输出 Path 和 True

```

[不同路径 III](https: // leetcode.cn / problems / unique - paths - iii /)
123.
给两个list, l1, l2。 返回两个list，第一个list是l1里的有但l2里没有的元素，第二个list是l2有但是l1没有的元素。（元素可以是数字，也可以是string）
这个比较简单好理解，就不给栗子啦！
Followup是如果l1和l2只有一个元素不一样，该怎么找
排序 / hashmap
124.
有两种人
一种是想合住
一种是不想合住
有不同房间数量的房子
怎么安排住宿？
125.
刚面完，题目要求实现字符串转换，例子如下：
A3B2 -> (A, 3), (B, 2)
(A3B2)
2 -> (A, 6), (B, 4)
A2(A3B2)
2 -> (A, 8), (B, 4)
[字符串解码](https: // leetcode.cn / problems / decode - string / submissions / 541567087 /) 用栈来做

类似于计算器的栈解法也可以
126.
抽象出来大概就是一个n - array
tree，node如果有children就视为manager。问整个tree中收入低于下属收入平均值的manager个数。
[统计值等于子树平均值的节点数](
    https: // leetcode.cn / problems / count - nodes - equal - to - average - of - subtree / solutions / 1477346 / by - hu - li - hu - wai - en3h /)
```cpp


class Solution {

int cnt;

public int averageOfSubtree(TreeNode root) {
dfs(root);


return cnt;
}

private
int[]
dfs(TreeNode
root) {
if (root == null) return new int[]{0, 0};

int[]
l = dfs(root.left);
int[]
r = dfs(root.right);
int
sum = (l[0] + r[0] + root.val), nodeNum = (l[1] + r[1] + 1), avg = sum / nodeNum;
if (avg == root.val) cnt++;
return new
int[]
{sum, nodeNum};
}
}
```
Follow up是问的是低于下属中位数应该怎么做。
解法: 数据流的中位数

127. Given a list of elements, each element with an Id and 3 (guaranteed 3, valid input) string properties.If any of the 2 elements have an overlap of the properties, they are considered duplicates, group the duplicated element ids together and show in the output.If no duplicates for a particular element, output its own id.
Example:
    Input:
    Element1, id1, properties: P1, P2, P3
Element2, id2, properties: P1, P4, P5
Element3, id3, properties: P6, P7, P8
Expected
output: {{id1, id2}, {id3}}
面试官提示转化成graph试试。

128.
string
replacement
比如说
string: "%X%_%Y%"
map:
{
    X = > "123"
Y = > "456"
}
需要output “123_456
"
两个followup：
1.
如果variable
名字
不只是1个char怎么办？
2.
如果variable
可以reference
另一个variable
怎么做
map = {USER = > admin, HOME = > / %USER % / home}
string = "I am %USER% My home is %HOME%"
output = "I am admin My home is /admin/home"

方法:
第一步: 拓步排序判断是否有环
第二部: 如果没有环, 就执行替换
[str
replacement](https: // leetcode.com/discuss/post/ 857876 /google-interview-question-onsite-by-anon-wc2e/)
```java


class Solution{
/ *
inputMap =
{
"V1": "Hello",
"V2": "$V1"

,
"V3": "Hola $V2 $V1"
      // "V4": "$V5"
}

dependency
map:
{
    "V1": "V2", "V3"
                "V2": "V3"
}

* /

int
stringToInt(String
s){
return stringMap.get(s);
}

String
intToString(int
i){
return intMap.get(i);
}

Map < String, Integer > stringMap = new
HashMap <> ();
Map < Integer, String > intMap = new
HashMap <> ();
String
stringReplacement(Map < String, String > input, String
s){
Set < String > nodes = input.keySet();
n = nodes.size();
int
i = 0;
for (String node: nodes){
    stringMap.put(node, i);
intMap.put(i, node);
i++;
}

int[]
indegree = new
int[n];
Map < Integer, List < Integer >> map = new
HashMap <> ();
for (String key: input.keySet()){
String val = input.getKey(key);
// some regex to find matching pattern
Pattern pattern = Pattern.compile("\\$[A-Za-z0-9]+");
Matcher matcher = pattern.matcher(val);
List < String > parents = new ArrayList <> ();
while (matcher.find()) {
parents.add(matcher.group());
}
// current
key
depend
on
parrents, add
to
graph
for (String p: parents){
if (nodes.contains(p)){
int pIndex = StringToInt.get(p);
int keyIndex = StringToInt.get(key);
map.putIfAbsent(pIndex, new ArrayList <> ());
// have map as parent->key for easier topo sort
map.get(pIndex).add(keyIndex);
indegree[keyIndex]++;
} else {
// when we depend on a node that doesn't have replacement rules
return "";
}
}
}
Queue < Integer > q = new
LinkedList <> ();
for (int i = 0; i < n; i++)
{
if (indegree[i] == 0)
{
    q.offer(indegree[i]);
}
}
int
N = n;
while (!q.isEmpty()){
int curr = q.poll();
N--;
if (!map.containsKey(curr)){
for (int next: map.get(curr)){
    indegree[next] - -;
// we
can
update
all
reference
of
currString
to
replacedCurrString
since
curr
indegree is 0(no
dependencies)
String
currString = intToString(curr);
String
replacedCurrString = input.get(currString);
String
originNextString = intToString(next);
String
replacedNextString = input.get(originNextString);
replacedNextString.replace(currString, replacedCurrString);
input.put(originNextString, replacedNextString);
if (indegree[next] == 0)
{
    q.offer(next);
}
}
}
}
if (N != 0){
// When there are circle in the map
return "";
}
for (String key: input.keySet()){
// something
to
undo
the
regex
if (s.contains("$" + key)){
s.replace(key, input.get(key));
}
}
return s;
}
}
```

131.[课程表](https: // leetcode.cn / problems / course - schedule /)

132.
假设有string
"AABBCCDDEE"， 注意所有的char如果出现的话一定是连续出现的，假设有一个数k是他们的partition
num，如果k = 3, 刚刚string的partition效果是
AAB
BCC
DDE
E, 我们称一个char为valid
char如果他仅存在于他的partition里面，并且在partition里面是连续存在的。那么刚刚这个例子，返回的valid
char应该是A, C, D。现在告诉你input不是整个string直接给你，而是以stream的形式一个char一个char的让你读，请你设计你的数据结构能够有
void
getNextChar(char
c) 和
int
getNumberOfValidChars()
这两个函数。
```python
if (currentChar != lastChar)
{
// check if lastChar is valid
if (lastChar != lastCharInLastSeq) {
counter += 1;
} else {
invalid, do
nothing
}
}
// update
variable
at
the
end
of
each
partition
if (currentNumber == partitionCount)
{
    lastCharInLastSeq = currentChar
reset
currentNumber
to
0
}
```

133.truncate a list of messages down to size max_log_messages.For the sake of this problem, our "fair" truncation algorithm is as follows: Let X be the max log messages maintained per client.For each client: If the client has emitted > X messages, truncate the log messages for that client to X messages.If the client has emitted <= X messages, do not truncate the log messages for that client. The goal of this problem is to figure out the maximum value of x which causes the total number of messages retained across all clients to be <= max_log_messages. Write Findx, which takes the input list and max_log_messages and returns X. Example: Suppose there are 5 log clients, and their number of
messages is: (A, 50), (B, 20), (C, 1000), (D, 50).(E, 400).Suppose we want to have no more than 300 total messages after truncation.
使用二分法猜答案O(nlgn)

135. 单元测试unittest
```python
import unittest
from Google.my_classes.class_1 import Demo
    # from my_classes.class_1 import Demo


class TestClassDemo(unittest.TestCase):
    def test_add(self):
        cls = Demo()
        res = 0
        self.assertEqual(cls.add(1, -1), res, f"the result should be 0 rather than {res}")

    def test_sub(self):
        cls = Demo()
        res = 1
        self.assertEqual(cls.sub(0, 1), res, f"the result should be -1 rather than {res}")


```

135.[K个不同整数的子数组](https: // leetcode.cn/problems/subarrays-with-k-different-integers/description/)
```python
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(k):
            dis = Counter()
            ans = 0
            left = 0
            for i in range(len(nums)):
                dis[nums[i]] += 1
                while len(dis) > k:
                    dis[nums[left]] -= 1
                    if dis[nums[left]] == 0:
                        dis.pop(nums[left])
                    left += 1
                ans += i - left
            return ans

        return at_most(k) - at_most(k - 1)


```

136.
自然数数组，1
到n，作为唯一输入。要求数组重排，以达到重排后的数组中任意对子的均值不落在他们中间。
数组重排，以达到重排后的数组中任意对子的君值不落在他们中间。
1，2，3 ：fail
君值
2
1，2，4: ok， 君值2
.5
```python

def f(x):
    """递归排序函数"""
    # 基本情况：单个元素的序列是已经排好序的
    if len(x) <= 1:
        return x

    # 将输入序列分为奇数位置的和偶数位置的子序列
    odd_indexed = x[::2]  # 奇数索引：x1, x3, x5, ...
    even_indexed = x[1::2]  # 偶数索引：x2, x4, x6, ...

    # 递归地排序这两个子序列
    y1 = f(odd_indexed)
    y2 = f(even_indexed)

    # 合并两个排序后的子序列
    return y1 + y2


# 示例使用：
n = 10
input_sequence = list(range(1, n + 1))
sorted_sequence = f(input_sequence)
print("Sorted sequence:", sorted_sequence)
```

137. Ｇiven an array， return the largest sum from a [i] + a[i + 1]....a[j] while a[i] == a[j]。 这题用prefix sum。 Follow up 就用hashmap 优化。
```python
from collections import defaultdict
class Solution:
    def get_maxsum(self, nums):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        m = defaultdict(list)
        for i in range(0, len(nums)):
            if len(m[nums[i]]) == 0:
                m[nums[i]] = [float('inf'), -float('inf')]  # min, max
            m[nums[i]][0] = min(m[nums[i]][0], prefix_sum[i + 1])  # 只记录最小
            m[nums[i]][1] = max(m[nums[i]][1], prefix_sum[i + 1])  # 只记录最大

        ans = -float('inf')

        for k, v in m.items():
            if len(v) >= 2:
                ans = max(ans, v[-1] - v[0] + k)
        return ans


print(Solution().get_maxsum([1, 2, 1, 3, 1, 2, 1]))
```
时间O(N)
138. 找所有重复元素: [442](https: // leetcode.cn / problems / find - all - duplicates - in -an - array / description /) [
    287](https: // leetcode.cn / problems / find - the - duplicate - number / submissions / 543130502 /)
    
```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [num for i, num in enumerate(nums) if num - 1 != i]


```
139. Alien Dict
140. 找一个ARRAY里是否存在一个subarray, 其中subarray的sum modk == n
     https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
整除
解法:
step1: 使用perfix_sum存和
step2: 遍历prefix_sum数组, 并用哈希表保存
```python
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        exists = defaultdict(int)
        count = 0
        for i in range(len(prefix)):
            if prefix[i] % k + n in exists:
                count += exists[prefix[i] % k + n]

            exists[prefix[i] % k + n] += 1

        return count


```
141 订票系统，卖家输入票子信息，用户买票子，follow - up允许卖家撤回票子，要求实时输出最便宜的票子，额外讨论了OOD设计
```python
构建一个订票系统，其中包括以下几个关键功能：

卖家可以输入票务信息（例如票价、票数、座位等）。

用户可以购买票务。

卖家可以撤回票务。

系统能够实时输出最便宜的票子。

此外，我们还要讨论面向对象设计（OOD），以便设计出高内聚、低耦合且可扩展的系统。

系统需求分析
基本功能：

卖家输入票子信息：包括票价、座位等信息。票务可以有多个属性，例如票价、日期、座位、类型等。

用户购买票子：用户可以购买票务，票务购买成功后，票数减少。

卖家撤回票子：卖家可以撤回已发布的票务，系统应该处理已撤销的票务信息。

实时输出最便宜的票子：系统能够根据当前售出的票务，实时返回最低价格的票子。

设计思路
Ticket类：表示一个票务，包含票价、数量等属性。

TicketInventory类：管理所有票务，包括添加、撤回、查询最便宜票务等。

User类：用户类，包含用户信息及已购买的票务。

TicketSystem类：系统的主要类，提供接口供用户和卖家进行操作。

类的设计
1.
Ticket
类
python
Copy


class Ticket:
    def __init__(self, ticket_id, price, quantity, event_name):
        self.ticket_id = ticket_id  # 票的唯一ID
        self.price = price  # 票价
        self.quantity = quantity  # 剩余票数
        self.event_name = event_name  # 事件名称

    def __repr__(self):
        return f"Ticket(ID: {self.ticket_id}, Event: {self.event_name}, Price: {self.price}, Quantity: {self.quantity})"


属性：

ticket_id：票务的唯一标识符。

price：票价。

quantity：剩余票数。

event_name：事件或活动名称。

2.
TicketInventory
类
该类用于管理所有的票务，能够添加、删除票务，以及查找最便宜的票务。

python
Copy
import heapq


class TicketInventory:
    def __init__(self):
        self.tickets = {}  # 使用字典存储票务信息，key为ticket_id
        self.min_heap = []  # 使用堆来实时查询最便宜的票务

    def add_ticket(self, ticket):
        """添加票务信息到系统"""
        self.tickets[ticket.ticket_id] = ticket
        heapq.heappush(self.min_heap, (ticket.price, ticket))  # 按票价维护堆

    def remove_ticket(self, ticket_id):
        """卖家撤回票务"""
        if ticket_id in self.tickets:
            del self.tickets[ticket_id]
            self._rebuild_heap()

    def _rebuild_heap(self):
        """重新构建堆"""
        self.min_heap = [(ticket.price, ticket) for ticket in self.tickets.values()]
        heapq.heapify(self.min_heap)

    def get_cheapest_ticket(self):
        """返回最便宜的票务"""
        while self.min_heap:
            _, ticket = self.min_heap[0]
            if ticket.ticket_id in self.tickets:  # 票务未被撤回
                return ticket
            else:
                heapq.heappop(self.min_heap)  # 弹出已撤销的票务
        return None


方法：

add_ticket(ticket)：添加票务。

remove_ticket(ticket_id)：卖家撤回票务，移除票务信息，并重建堆。

get_cheapest_ticket()：获取当前最便宜的票务，实时检查堆中的票务是否有效（是否已被撤回）。

3. User


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.purchased_tickets = []

    def buy_ticket(self, ticket, quantity):
        if ticket.quantity >= quantity:
            ticket.quantity -= quantity
            self.purchased_tickets.append((ticket, quantity))
            return True
        return False


方法：

buy_ticket(ticket, quantity)：用户购买票务，检查票数是否足够，成功购买后更新票务数量。

4. TicketSystem 类


class TicketSystem:
    def __init__(self):
        self.inventory = TicketInventory()

    def seller_add_ticket(self, ticket):
        """卖家添加票务"""
        self.inventory.add_ticket(ticket)

    def seller_remove_ticket(self, ticket_id):
        """卖家撤回票务"""
        self.inventory.remove_ticket(ticket_id)

    def user_buy_ticket(self, user, ticket_id, quantity):
        """用户购买票务"""
        ticket = self.inventory.tickets.get(ticket_id)
        if ticket:
            return user.buy_ticket(ticket, quantity)
        return False

    def get_cheapest_ticket(self):
        """获取当前最便宜的票务"""
        return self.inventory.get_cheapest_ticket()


方法：

seller_add_ticket(ticket)：卖家添加票务。

seller_remove_ticket(ticket_id)：卖家撤回票务。

user_buy_ticket(user, ticket_id, quantity)：用户购买票务。

get_cheapest_ticket()：获取最便宜的票务。

示例使用
python
Copy
# 创建系统
ticket_system = TicketSystem()

# 卖家添加票务
ticket1 = Ticket(ticket_id=1, price=100, quantity=50, event_name="Concert A")
ticket_system.seller_add_ticket(ticket1)
ticket2 = Ticket(ticket_id=2, price=80, quantity=30, event_name="Concert B")
ticket_system.seller_add_ticket(ticket2)

# 获取最便宜的票务
cheapest_ticket = ticket_system.get_cheapest_ticket()
print(f"最便宜的票务是: {cheapest_ticket}")

# 用户购买票务
user = User(user_id=101)
ticket_system.user_buy_ticket(user, ticket_id=2, quantity=2)

# 卖家撤回票务
ticket_system.seller_remove_ticket(2)

# 获取最便宜的票务
cheapest_ticket = ticket_system.get_cheapest_ticket()
print(f"撤回票务后，最便宜的票务是: {cheapest_ticket}")
```
142. coding 1: design a class that supports insertRange and queryPoint, which returns true if the given point is covered by the given ranges

一些followup包括optimize queryPoint to be O(1), 
points can be negatives, ranges can be continuous instead of discrete
解法: 空间换时间 arr[i] 记录是否在range内部 bitmap

143.[绝对差不超过限制的最长连续子数组] 1438 单调队列

144. https://leetcode.com/problems/permutation-sequence
生成一个车牌号。00000 -> 00001 -> 00002 -> ... -> 99999 -> A0000 -> A0001 -> ... -> A9999 -> ... -> Z9999 -> AA000 -> ... -> ZZ999 -> ... -> AAA00 -> ... -> ZZZ99 -> ... -> AAAA0 -> ... -> ZZZZ9 -> ... -> AAAAA -> ... -> ZZZZZ。输入是一个数字，表示要生成第几个车牌号，输出是一个字符串，对应该数字对应的车牌号。
```python


class Solution:
    """
        以 1 为 a1(首字母) 的排列一共有 (n−1)! 个；
        以 2 为 a1(首字母)的排列一共有 (n−1)! 个；

        以 n 为 a1的排列一共有 (n−1)! 个。

        由于我们需要求出从小到大的第 k 个排列，因此：

        如果 k≤(n−1)! ，我们就可以确定排列的首个元素为 1；
        如果 (n−1)!< k ≤2⋅(n−1)! 我们就可以确定排列的首个元素为 2；
    """

    def get_fac(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

    def getPermutation(self, n: int, k: int) -> str:
        res = []

        num = list(range(1, n + 1))

        k -= 1
        res = ""
        for i in range(n):
            fac = self.get_fac(len(num) - 1)
            d = k // fac
            res += str(num[d])
            num.pop(d)
            k = k % fac

        return res


```
145.[大西洋 太平洋 洋流问题]()
```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
            逆向dfs
            O(mn)
        """
        m = len(heights)
        n = len(heights[0])

        self.heights = heights
        self.P = [[False for _ in range(n)] for _ in range(m)]
        self.A = [[False for _ in range(n)] for _ in range(m)]
        self.dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # self.ans = []

        for i in range(n):
            self.P[0][i] = True
            self.A[m - 1][i] = True

        for i in range(m):
            self.P[i][0] = True
            self.A[i][n - 1] = True

        for i in range(m):
            self.dfs(i, 0, m, n, self.P)
            self.dfs(i, n - 1, m, n, self.A)
        for i in range(n):
            self.dfs(0, i, m, n, self.P)
            self.dfs(m - 1, i, m, n, self.A)

        ans = []
        for i in range(m):
            for j in range(n):
                if self.P[i][j] and self.A[i][j]:
                    ans.append([i, j])

        return ans

    def dfs(self, i, j, m, n, ocean):
        for _dir in self.dirs:
            new_i, new_j = i + _dir[0], j + _dir[1]
            if 0 <= new_i < m and 0 <= new_j < n and self.heights[new_i][new_j] >= self.heights[i][j] and ocean[new_i][
                new_j] == False:
                ocean[new_i][new_j] = True
                self.dfs(new_i, new_j, m, n, ocean)


```

146. leaderboard: 实现lgn求topk的和: MKAverage

147.[花期内花的数目](https: // leetcode.cn / problems / number - of - flowers - in -full - bloom / description /)
```python


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        """
            差分数组: nlg(N)
        """
        cnt = defaultdict(int)
        for s, e in flowers:
            cnt[s] += 1
            cnt[e + 1] -= 1

        arr = sorted(cnt.items())
        m = len(people)
        people = [(i, people[i]) for i in range(m)]

        ans = [0 for _ in range(m)]

        people = sorted(people, key=lambda x: (x[1], x[0]))
        cur = 0
        j = 0
        # print(arr)
        for i, p in people:
            while j < len(arr) and arr[j][0] <= p:
                cur += arr[j][1]
                j += 1
            ans[i] = cur
        return ans

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # 二分: O(nlgN)
        start = []
        end = []
        for s, e in flowers:
            start.append(s)
            end.append(e)
        start = sorted(start)
        end = sorted(end)
        m = len(people)
        ans = [0 for _ in range(m)]

        for i in range(m):
            s1 = bisect.bisect_right(start, people[i])
            e1 = bisect.bisect_right(end, people[i] - 1)

            ans[i] = max(0, s1 - e1)
        return ans


```
148. given a datastream and a distance，每次来一个新value，判断一下能否和已经存下来的组成triplet，triplet之间两两abs小于distance。lz用了sortedlist

     
150. number of islands Tree.树上的岛屿数量
```python
"""
         1
       /   \
      0     1
     / \   / \
    1   0  1  0

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_islands(root):
    if root is None:
        return 0, []

    islands = []
    visited = {}

    # Helper function to perform DFS and calculate the size of an island.
    def dfs(node):
        # 返回包含当前节点node的岛屿的size
        if node is None or node.val == 0 or node in visited:
            return 0  # node是水, 返回0
        visited[node] = True
        size = 1  # Count the current node
        size += dfs(node.left)
        size += dfs(node.right)
        return size

    # Traverse all nodes in the tree
    def traverse(node):
        if node is None:
            return
        if node.val == 1 and node not in visited:  # 当前节点没有被访问过, 必不可少
            # Start a new island and calculate its size
            island_size = dfs(node)  # 包含当前节点的岛屿的size
            islands.append(island_size)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return len(islands), islands


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(0)
root.left.left = TreeNode(1)
root.left.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(1)

print(find_islands(root))
```
还可以使用并查集, 但是需要做两遍遍历


150.[树的直径](https: // leetcode.com / problems / diameter - of - binary - tree /)
```python


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans

    @cache
    def dfs(self, node) -> List[int]:
        if node is None:
            return 0

        left_max = self.dfs(node.left)
        right_max = self.dfs(node.right)

        self.ans = max(self.ans, left_max + right_max)

        return 1 + max(left_max, right_max)


```
151.
loop
iteration实现树的先序, 中序, 后序遍历
preorder
```python


def preorderTraversal_iter(self, root: Optional[TreeNode]) -> List[int]:
    """

    """
    cur = root
    stack = []
    ans = []
    while cur or stack:
        while cur:
            ans.append(cur.val)
            stack.append(cur)
            cur = cur.left

        top = stack.pop()
        cur = top.right
    return ans


```
inorder
```python


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        ans = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            top = stack.pop()
            ans.append(top.val)
            cur = top.right
        return ans


```
3.
postorder
```python


class Solution:
    def postorderTraversal(self, root):
        def bfs(root):
            if root is None:
                return

            bfs(root.left)
            bfs(root.right)
            res.append(root.val)

        res = []
        bfs(root)
        return res

    def postorderTraversal_1(self, root: Optional[TreeNode]) -> List[int]:
        res = deque()
        stack = []
        if root is None:
            return []

        stack.append(root)
        while len(stack) > 0:
            cur = stack.pop()
            res.appendleft(cur.val)

            if cur.left is not None:
                stack.append(cur.left)
            if cur.right is not None:
                stack.append(cur.right)

        return list(res)


```
4.
删除一棵树的每个
```python


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delete_tree(root):
    if root is None:
        return

    # Recursively delete the left and right subtrees
    delete_tree(root.left)
    delete_tree(root.right)

    # "Delete" the current node (by setting it to None)
    root.left = None
    root.right = None
    root.val = None  # Setting value to None, simulating deletion

    print(f"Node with value {root.val} deleted.")  # Simulating the deletion action


# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Delete the tree
delete_tree(root)
```
循环实现
```python


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delete_tree_iteratively(root):
    if root is None:
        return

    stack = [root]  # Start with the root node in the stack
    nodes_to_process = []  # This will be used to process nodes in post-order

    while stack:
        node = stack.pop()
        nodes_to_process.append(node)  # Add node to the nodes_to_process stack for post-order

        # Push the left and right children to the stack
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # Now we process the nodes in reverse order (post-order)
    while nodes_to_process:
        node = nodes_to_process.pop()
        # "Delete" the current node by setting its left, right, and val to None
        node.left = None
        node.right = None
        node.val = None  # Optionally clear the value to simulate deletion
        print(f"Node with value None deleted.")  # Simulate the deletion


# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Delete the tree iteratively
delete_tree_iteratively(root)

```
6.
只用1和2组合出N，打印print出所有可能的组合
举例：
4:
1
1
1
1
1
1
2
1
2
1
2
1
1
2
2
```python


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
                dfs(cur + i)
                path.pop()

        dfs(0)
        return ans


print(Solution().get_n(4))
```
用栈实现
```python


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
```

7.
给莫斯代码
.-.xxx -..xxxxx.. -
xxx代表char分割
xxxxx代表word分割
要decode
```python
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9'
}


def decode_morse_code(morse_code):
    # 摩斯码分隔符
    char_split = 'xxx'  # 表示字符分隔
    word_split = 'xxxxx'  # 表示单词分隔

    # 将摩斯码根据单词分隔符拆分成单词
    words = morse_code.split(word_split)

    decoded_message = []

    for word in words:
        # 将每个单词根据字符分隔符拆分成字符
        characters = word.split(char_split)

        decoded_word = ''.join(MORSE_CODE_DICT.get(char, '') for char in characters)
        decoded_message.append(decoded_word)

    # 返回解码后的消息，单词之间用空格分隔
    return ' '.join(decoded_message)


# 示例摩斯码
morse_code = '.-.xxx-..xxxxx..-'

# 解码
decoded_message = decode_morse_code(morse_code)
print(decoded_message)

```
如果单词也是xxx分割, 并且给了word
set.则:
step1: 先收集所有字符
step2: 做word
break, 用dfs

8.[小偷, 最安全路径](
    https: // leetcode.cn / problems / find - the - safest - path - in -a - grid / solutions / 2375133 / bfs - ping - jing - lu - by - tsreaper - nrrp /)
step
1: 做1次bfs, 记录每个格子的安全距离
step
2: (0, max(dp[i][j]))
做二分, 每次判断安全距离x能否到达
9.
给你一个string里面有startip，endip，cityname，具体string里面什么格式你可以自己定义，然后给你一个ip
adress
输出对应的城市名字。
string
里面都是ipv4并且valid没有overlap的ip
address
Input
string
startIP
endIP
cityName
1.0
.1
.10
1.0
.1
.20
NYC
1.0
.1
.30
1.0
.1
.40
SF
Input
1.0
.1
.12
return NYC
和面试官聊大概就是要建一个class来代表这个startip，endip和cityname。然后按照startip或者endip排个序，最后用2分法来找
```python
import bisect


class IPRange:
    def __init__(self, start_ip, end_ip, city_name):
        self.start_ip = start_ip
        self.end_ip = end_ip
        self.city_name = city_name

        # 将 start_ip 和 end_ip 转换为整数
        self.start_ip_int = self.ip_to_int(start_ip)
        self.end_ip_int = self.ip_to_int(end_ip)

    def ip_to_int(self, ip):
        # 将 IP 地址字符串转换为整数
        octets = ip.split('.')
        return (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])


class IPCityFinder:
    def __init__(self):
        self.ranges = []

    def add_range(self, start_ip, end_ip, city_name):
        # 创建一个新的 IP 区间并加入到 ranges 中
        self.ranges.append(IPRange(start_ip, end_ip, city_name))

    def build(self):
        # 根据 start_ip_int 排序 IP 区间
        self.ranges.sort(key=lambda x: x.start_ip_int)

    def find_city(self, ip):
        # 查找给定 IP 对应的城市名
        ip_int = self.ip_to_int(ip)

        # 二分查找
        # 我们从 IP 区间的 start_ip_int 中获取所有起始地址的值
        start_ips = [r.start_ip_int for r in self.ranges]

        # 使用 bisect 查找该 IP 应该插入的位置
        idx = bisect.bisect_right(start_ips, ip_int) - 1

        # 检查是否找到对应的城市
        if idx >= 0 and self.ranges[idx].start_ip_int <= ip_int <= self.ranges[idx].end_ip_int:
            return self.ranges[idx].city_name
        else:
            return "Not found"  # 如果没有找到对应的城市

    def ip_to_int(self, ip):
        # 将 IP 地址字符串转换为整数
        octets = ip.split('.')
        return (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])


# 示例：测试
ip_finder = IPCityFinder()
ip_finder.add_range("1.0.1.10", "1.0.1.20", "NYC")
ip_finder.add_range("1.0.1.30", "1.0.1.40", "SF")
ip_finder.build()

# 查找给定 IP 对应的城市
print(ip_finder.find_city("1.0.1.12"))  # 返回 "NYC"
print(ip_finder.find_city("1.0.1.35"))  # 返回 "SF"
print(ip_finder.find_city("1.0.1.50"))  # 返回 "Not found"

```
10. 两辆车Two cars can move(up, down, left, right or not move) and return whether they can reach their destination .is road # is wall a is starting point of car a b is starting point of car b A is car a’s destination B is car b’s destination
例如
aBAb: false
因为a或者b总会挡住对方的出路 面试官的思路是遍历判断是否能达到最终状态即a和b都到各自的终点。我的做法是遍历时把grid转换成string来代表当前状态，遍历的时候就可以判断当前状态是否被访问过。

```python
from collections import deque

# 车的移动方向：上、下、左、右、不动
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]


def is_valid_move(x, y, grid, rows, cols):
    """检查是否可以移动到 (x, y) 位置"""
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] != '#'


def bfs(grid, start_a, start_b, dest_a, dest_b):
    """广度优先搜索来检查是否能到达目标"""
    rows, cols = len(grid), len(grid[0])
    visited = set()  # 用于记录已经访问过的状态
    queue = deque([(start_a, start_b)])  # 队列存储每一步的状态

    while queue:
        car_a, car_b = queue.popleft()
        ax, ay = car_a
        bx, by = car_b

        # 如果两辆车分别到达目的地
        if car_a == dest_a and car_b == dest_b:
            return True

        # 当前状态转换为字符串，检查是否已经访问过
        current_state = (ax, ay, bx, by)
        if current_state in visited:
            continue

        # 记录已经访问过的状态
        visited.add(current_state)

        # 尝试两辆车的所有移动
        for dx1, dy1 in directions:
            new_ax, new_ay = ax + dx1, ay + dy1
            if not is_valid_move(new_ax, new_ay, grid, rows, cols):
                continue

            for dx2, dy2 in directions:
                new_bx, new_by = bx + dx2, by + dy2
                if not is_valid_move(new_bx, new_by, grid, rows, cols):
                    continue

                # 如果两辆车不重叠，且每辆车都在有效的位置
                if (new_ax == new_bx and new_ay == new_by):
                    continue  # 两辆车不能重叠

                queue.append(((new_ax, new_ay), (new_bx, new_by)))

    return False


def can_reach_destinations(grid):
    """检查两个车是否可以分别到达各自的目的地"""
    rows, cols = len(grid), len(grid[0])

    # 找到车a、车b、车A、车B的起始位置
    start_a = None
    start_b = None
    dest_a = None
    dest_b = None

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'a':
                start_a = (i, j)
            elif grid[i][j] == 'b':
                start_b = (i, j)
            elif grid[i][j] == 'A':
                dest_a = (i, j)
            elif grid[i][j] == 'B':
                dest_b = (i, j)

    # 调用BFS来检查是否可以到达目标
    if not start_a or not start_b or not dest_a or not dest_b:
        return False  # 如果找不到起始点或者目标点

    return bfs(grid, start_a, start_b, dest_a, dest_b)


# 测试用例
grid = [
    ['a', '.', '.', '#', '.', '.', 'B'],
    ['.', '#', '#', '#', '.', '#', '#'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['#', '.', '#', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '#', '#', 'A'],
    ['#', '.', '.', '.', '#', '#', '.'],
    ['b', '.', '.', '#', '.', '.', '.']
]

# 调用函数
result = can_reach_destinations(grid)
print("Can both cars reach their destinations?", result)

```
11.有效的括号字符串 'https://leetcode.cn/problems/valid-parenthesis-string/solutions/992347/you-xiao-de-gua-hao-zi-fu-chuan-by-leetc-osi3
    
13. tree path sum leaf to leaf
```python
class Solution:
    def path_sum_leaf2leaf(self, root):
        def dfs(node):
            if node is None: return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            return max(left_sum, right_sum) + node.val

        return dfs(root)


```
non leaf to leaf
```python
class Solution:
    def path_sum(self, root):
        ans = -float('inf')

        def dfs(node):
            nonlocal ans
            if node is None: return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            ans = max(ans, node.val + max(left_sum, 0) + max(right_sum, 0))

            return node.val + max(max(left_sum, 0), max(right_sum, 0))

        dfs(root)
        return ans


```
