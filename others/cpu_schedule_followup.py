"""
followup:
    在给定任务和完成时间的情况下，找出最少需要多少个CPU才能让所有任务尽快搞定。
"""

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
            mid = left + (right-left) // 2
            cur_time, _ = self.min_time(tasks, mid)

            if cur_time <= time:
                right = mid
            else:
                left = mid + 1

        return left


tasks = [(0, 5), (1, 3), (2, 1), (4, 2)]
time = 12
print(Solution().min_cpus(tasks, time))

