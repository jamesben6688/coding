"""


"""
from collections import deque


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def can_transmit(router_dict, start, end, R):
    routers = list(router_dict.keys())
    coords = router_dict

    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current == end:
            return True
        visited.add(current)

        for other in routers:
            if other in visited:
                continue
            if manhattan(coords[current], coords[other]) <= R:
                queue.append(other)

    return False


router_dict = {
    "A": (0, 0),
    "B": (0, 8),
    "C": (10, 8),
    "D": (0, 28)
}

print(can_transmit(router_dict, "A", "C", R=10))  # True
print(can_transmit(router_dict, "A", "D", R=10))  # False

