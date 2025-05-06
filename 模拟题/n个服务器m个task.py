import heapq


def most_tasks_server(n, m, tasks):
    # 任务按开始时间排序，若开始时间相同按结束时间排序
    tasks.sort(key=lambda x: (x[0], x[1]))

    # 服务器的空闲时间，初始化为0
    free_time = [0] * n
    # 服务器的任务计数，初始化为0
    task_count = [0] * n

    # 遍历任务
    for start, end in tasks:
        # 找到最早空闲的服务器
        available_server = None
        for i in range(n):
            if free_time[i] <= start:
                available_server = i
                break

        if available_server is not None:
            # 任务分配给该服务器
            free_time[available_server] = end
            task_count[available_server] += 1
        else:
            # 所有服务器都在忙碌，等待最早空闲的服务器
            earliest_free_time = min(free_time)
            # 等待任务，直到有服务器空闲
            earliest_free_server = free_time.index(earliest_free_time)
            free_time[earliest_free_server] = earliest_free_time + (end - start)
            task_count[earliest_free_server] += 1

    # 找到处理任务最多的服务器
    max_tasks = max(task_count)
    server_index = task_count.index(max_tasks)

    return server_index, max_tasks


# 示例输入
tasks = [(1, 3), (2, 4), (3, 5), (1, 2), (4, 6)]
n = 3  # 服务器数量
m = 5  # 任务数量
result = most_tasks_server(n, m, tasks)
print(f"服务器 {result[0]} 处理的任务最多，共 {result[1]} 个任务")
