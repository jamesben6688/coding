"""

Assuming that each task has {id, priority}, you will receive three types of requests as a stream:
1. New task, meaning that task {id, priority} is newly generated.
2. Pick task, meaning that the task handler can handle the next task, so you have to return the highest priority task and remove it.
3. Change priority of task, meaning that specific task’s priority is changed, so you have to update the priority of the task.
For example,
New task {3, 2}// id = 3, priority = 2
New task {5, 4}
New task {2, 3}
Pick → you should return task {3, 2} // if a task has a lower number for the priority, it is a higher priority.
Update priority {5, 1} // We changed the priority of task whose id is 5 from 4 to 1
Pick → you should return task {5, 1}
New task {1, 0}
New task {4, 6}
Update priority {2, 7}
New task {6, 5}
Pick → you should return task {1, 0}
Pick → you should return task {6, 5}
Pick → you should return task {4, 6}

我们需要设计一个任务调度器，支持以下操作（流式地处理）：

三种操作：
新增任务：NewTask(id, priority)

选择任务：Pick() → 返回当前最高优先级任务（priority 最小），并将其移除

更新任务优先级：UpdatePriority(id, new_priority)

数据结构需求：
高效插入任务

高效更新任务优先级

高效取出当前最小 priority 的任务

使用 Min Heap + Hash Map + Lazy Removal（惰性删除）
O(lgN)
"""
import heapq

class TaskScheduler:
    def __init__(self):
        self.heap = []  # min-heap: (priority, id)
        self.task_map = {}  # id -> current priority

    def new_task(self, id, priority):
        heapq.heappush(self.heap, (priority, id))
        self.task_map[id] = priority

    def update_priority(self, id, new_priority):
        if id in self.task_map:
            self.task_map[id] = new_priority
            heapq.heappush(self.heap, (new_priority, id))

    def pick(self):
        while self.heap:
            priority, id = heapq.heappop(self.heap)
            # Lazy deletion: skip outdated heap entry
            if id in self.task_map and self.task_map[id] == priority:
                del self.task_map[id]
                return (id, priority)
        return None
