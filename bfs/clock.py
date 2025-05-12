from collections import deque

def get_min_click(time1, time2):
    que = deque()
    step = 0

    que.append(time1)
    visited = set()
    visited.add(tuple(time1))

    while que:
        q_size = len(que)
        for i in range(q_size):
            cur_h, cur_m = que.popleft()

            if cur_h == time2[0] and cur_m == time2[1]:
                return step

            nx_h_1 = (cur_h + 1) % 24
            nx_h_2 = (cur_h+24-1) % 24

            que.append((nx_h_1, cur_m))
            que.append((nx_h_2, cur_m))

            nx_m_1 = (cur_m + 1) % 60
            nx_m_2 = (cur_m + 60 - 1) % 60
            que.append((cur_h, nx_m_1))
            que.append((cur_h, nx_m_2))

        step += 1
    return -1


print(get_min_click([23, 59], [0, 2]))
