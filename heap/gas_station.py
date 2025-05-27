import heapq

import heapq


from typing import List, Tuple


def min_cost_with_dp(target: int, tank_size: int, stations: list[tuple[int, int]]) -> int:
    stations = [(0, 0)] + stations + [(target, float('inf'))]
    n = len(stations)

    INF = float('inf')
    dp = [[INF] * (tank_size + 1) for _ in range(n)]
    dp[0][tank_size] = 0  # 起点满油

    for i in range(1, n):  # 当前站 i
        for j in range(i):  # 从哪个前一站 j 来
            dist = stations[i][0] - stations[j][0]
            if dist > tank_size:
                continue  # 无法从 j 到 i，无论加多少油

            for m in range(tank_size + 1):  # j站时剩余油量为 m
                if dp[j][m] == INF:
                    continue
                if m < dist:
                    need = dist - m  # 从 j 到 i 还差多少油
                else:
                    need = 0

                for extra in range(tank_size - m - need + 1):  # 可选的额外加油（不是必须的）
                    total_fuel = m + need + extra
                    if total_fuel > tank_size:
                        continue
                    final_fuel = total_fuel - dist  # 到达 i 后剩余的油
                    cost = dp[j][m] + (need + extra) * stations[j][1]
                    dp[i][final_fuel] = min(dp[i][final_fuel], cost)

    return min(dp[-1])


# def min_total_cost(target: int, tank_size: int, stations: List[Tuple[int, int]]) -> tuple[float, int]:
#     """
#         DP:
#             if f-m+dis[i]-dis[j] >= 0:
#                 dp[i][f] = min(dp[i][f], dp[j][m] + stations[j][0] * max(0, f+dis[i]-dis[j]-m))
#
#         target = 100
#         tank_size = 30
#         stations = [
#             (10, 5),
#             (20, 2),
#             (30, 4),
#             (60, 3),
#             (80, 1)
#         ]
#
#     :param target:
#     :param tank_size:
#     :param stations:
#     :return:
#     """
#     stations = [(0, 0)] + stations + [(target, float('inf'))]
#     n = len(stations)
#     dp = [[float('inf')] * (tank_size+1) for _ in range(n+2)]
#     for i in range(tank_size):
#         dp[0][i] = 0
#
#     for i in range(1, n):
#         for f in range(tank_size+1):
#             for j in range(i):
#                 if j == 0:
#                     m = tank_size
#
#                     dp[i][f] = min(dp[i][f], dp[j][m] + stations[j][1] * (f - m + stations[i][0] - stations[j][0]))
#                 else:
#                     for m in range(tank_size+1):
#                         if f-m+stations[i][0]-stations[j][0] >= 0:
#                             dp[i][f] = min(dp[i][f], dp[j][m]+stations[j][1] * (f-m+stations[i][0]-stations[j][0]))
#
#
#     return min(dp[-1])


from typing import List, Tuple

def min_cost_dp(target: int, tank_size: int, stations: List[Tuple[int, int]]) -> int:
    # 在原来的加油站列表中加入起点和终点
    stations = [(0, 0)] + stations + [(target, 0)]
    n = len(stations)

    # dp[i][f] = 从起点到达第i个站，剩余f油量的最小花费
    INF = float('inf')
    dp = [[INF] * (tank_size + 1) for _ in range(n)]
    dp[0][tank_size] = 0  # 起点：满油，0花费

    for i in range(n):
        for fuel in range(tank_size + 1):
            if dp[i][fuel] == INF:
                continue

            pos_i, price_i = stations[i]

            # 1. 尝试加油 k 单位（从0到tank_size - fuel）
            for k in range(tank_size - fuel + 1):
                new_fuel = fuel + k
                cost = dp[i][fuel] + k * price_i

                # 2. 从当前站尝试开到后续站 j
                for j in range(i + 1, n):
                    pos_j, _ = stations[j]
                    distance = pos_j - pos_i
                    if distance > new_fuel:
                        break
                    remain = new_fuel - distance
                    dp[j][remain] = min(dp[j][remain], cost)

    # 答案是：到达终点（第n-1站）任意剩余油量的最小花费
    return min(dp[n - 1]) if min(dp[n - 1]) < INF else -1




import heapq


def min_cost_to_target(stations, tank_size, target):
    stations.append((target, 0))  # 把终点也当成一个加油站
    stations.sort()

    n = len(stations)
    heap = [(0, 0, tank_size)]  # (total_cost, station_index, fuel_left)

    visited = dict()  # (index, fuel) -> cost

    while heap:  # n*tank_size
        cost, i, fuel = heapq.heappop(heap)
        pos_i, price_i = stations[i]

        if pos_i + fuel >= target:
            return cost

        for j in range(i + 1, n):  # n
            pos_j, price_j = stations[j]
            dist = pos_j - pos_i
            if dist > fuel:
                break  # 不能到达
            for added in range(tank_size - (fuel - dist) + 1):  # 能加的油量  # tank_size
                new_fuel = fuel - dist + added
                new_cost = cost + added * price_j
                key = (j, new_fuel)
                if key not in visited or visited[key] > new_cost:
                    visited[key] = new_cost
                    heapq.heappush(heap, (new_cost, j, new_fuel))  # log(n*tank_size)

    return -1  # 无法到达


target = 100
tank_size = 30
stations = [
    (10, 5),
    (20, 2),
    (30, 4),
    (60, 3),
    (80, 1)
]
# print(min_cost_to_target(stations, tank_size, target))
print(min_cost_with_dp(target, tank_size, stations))
