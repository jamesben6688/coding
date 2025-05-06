"""

 解法设计（使用差分 + 有序容器）
我们需要维护当前已有的所有 (time, cpu_diff) 的事件，可以用一个 SortedDict 来维护（或者用 heap + line sweep 但不适合动态添加）。

数据结构选择：
SortedDict (来自 sortedcontainers 库) 存储所有时刻的增减 CPU 数量（key: time, value: cpu_diff）

每次 check 都做一遍线性扫描（由于事件较少，通常 acceptable）

✅ 代码示例
python
Copy
Edit

🧪 测试示例
python
Copy
Edit
scheduler = JobScheduler(4)
print(scheduler.add_job(0, 5, 2))  # True
print(scheduler.add_job(2, 4, 2))  # True
print(scheduler.add_job(3, 2, 1))  # False, would need 5 CPU at time 3
print(scheduler.can_schedule(6, 2, 3))  # True, future slot is ok
✅ 时间复杂度分析
add_job / can_schedule 时间复杂度：O(k)，k 是当前 timeline 中的不同时间点数量（最多 2 * job 数量）

空间复杂度：O(k)


"""
from sortedcontainers import SortedDict


class JobScheduler:
    def __init__(self, total_cpus):
        self.total_cpus = total_cpus
        self.timeline = SortedDict()  # key: timestamp, value: cpu_diff

    def _update_timeline(self, time, delta):
        if time in self.timeline:
            self.timeline[time] += delta
        else:
            self.timeline[time] = delta

        # Clean up 0s to keep it minimal
        if self.timeline[time] == 0:
            del self.timeline[time]

    def can_schedule(self, start, duration, cpu_needed):
        end = start + duration
        # simulate: insert into a copy of timeline
        temp = SortedDict(self.timeline)

        temp[start] = temp.get(start, 0) + cpu_needed
        temp[end] = temp.get(end, 0) - cpu_needed

        # sweep through and check CPU usage
        current_cpu = 0
        for time in temp:
            current_cpu += temp[time]
            if current_cpu > self.total_cpus:
                return False
        return True

    def add_job(self, start, duration, cpu_needed):
        if self.can_schedule(start, duration, cpu_needed):
            self._update_timeline(start, cpu_needed)
            self._update_timeline(start + duration, -cpu_needed)
            return True
        return False

