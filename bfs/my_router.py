"""
比如router是 Router A [0,0] , Router B[0,8], Router C[10,8], Router D [0,28] R = 10,
输入start router和end router，返回是否能从start传递到end，每次传递只能在range内，这里这个distance大叔说manhattan distance就可以。
follow up是 比如router会优先传递给最近的
"""
def man_dis(pt1, pt2):
    return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])


from collections import deque


def can_transmit(start, end, routers, r):
    que = deque([start])
    n = len(routers)
    visited = set()
    visited.add(start)
    parents = {start: None}

    while que:
        q_size = len(que)
        neighbors = []
        for i in range(q_size):
            cur = que.popleft()
            if cur == end:
                path = []

                # followup: 打印path
                while end in parents:
                    path.append(end)
                    end = parents[end]

                return True, path[::-1]

            for j in routers:
                if j not in visited and man_dis(routers[cur], routers[j]) <= r:
                    # que.append(j)
                    neighbors.append(j)
                    visited.add(j)

            # followup-1: 优先传给最近的
            sorted(neighbors, key=lambda x: man_dis(routers[x], routers[cur]))
            que.extend(neighbors)

            for node in neighbors:
                if node not in parents:
                    parents[node] = cur

    return False, []


router_dict = {
    "A": (0, 0),
    "B": (0, 8),
    "C": (10, 8),
    "D": (0, 28)
}
print(can_transmit("A", "D", router_dict, r=10))
