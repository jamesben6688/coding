"""
Jessica wants to get auto insurance. When arriving at the insurance company, there are N agents (number 1 to N)
serving nobody, and M people have already arrived with the same demand.
The company follows the rule of first arrived first served, and if more than 2 agents can serve a customer at the same time,
the customer will always choose the one with the smallest number.
For agents, each of them has a constant serving time that the ith agent will take T[i] minutes to serve a customer.
 Assume Jessica arrived at time 0, and all the agents are idle and start to serve the customers.
The question is how many minutes will Jessica needs to wait before meeting with an agent?
"""
import heapq
from math import gcd, lcm

# lcm(*[3, 5])
# lcm(a, b) = a * b // gcd(a, b)

def jessica_wait_time(T, M):
    """
        以下根据周期优化。
        求LCM: N(log(K)), 其中K为最小的数

        LCM(a, b, c) = LCM(a, LCM(b, c)), LCM(b, c) = log(K)

    :param T:
    :param M:
    :return:
    """
    _lcm = lcm(*T)
    period = sum([_lcm // T[i] for i in range(len(T))])
    ans = (M // period) * _lcm
    # ans = 0

    M = M % period
    # ans = 0

    N = len(T)
    # Min-heap: (available_time, agent_index)
    heap = [(0, i) for i in range(N)]
    heapq.heapify(heap)

    for customer in range(M):  # Simulate the M people before Jessica
        available_time, agent_idx = heapq.heappop(heap)
        # Agent becomes busy again after T[agent_idx]
        heapq.heappush(heap, (available_time + T[agent_idx], agent_idx))

    # Jessica is the next customer
    wait_time, agent_idx = heapq.heappop(heap)
    ans += wait_time
    return ans, agent_idx

# period=599 people
# period_time = 420
print(jessica_wait_time(T = [2, 5, 3, 7, 4],
M = 401+599+599))