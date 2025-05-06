from copy import deepcopy


class Solution:
    def get_min_time(self, tasks, n_cpus):
        mn_time = float('inf')
        n_tasks = len(tasks)
        cpu_time = [0] * n_cpus
        finished = [False] * n_tasks
        n_finish = 0
        cpu_schedule = [[] for _ in range(n_cpus)]
        ans = []
        def dfs():
            nonlocal mn_time, n_finish, ans
            if n_finish == n_tasks:
                if max(cpu_time) < mn_time:
                    mn_time = max(cpu_time)
                    ans = deepcopy(cpu_schedule)
                mn_time = min(mn_time, max(cpu_time))
                return

            for i in range(n_tasks):
                if finished[i]:
                    continue
                for cpu_idx in range(n_cpus):
                    finished[i] = True
                    cpu_schedule[cpu_idx].append(i)
                    n_finish += 1
                    old_time = cpu_time[cpu_idx]
                    if cpu_time[cpu_idx] <= tasks[i][0]:
                        cpu_time[cpu_idx] = tasks[i][0] + tasks[i][1]
                    else:
                        cpu_time[cpu_idx] += tasks[i][1]
                    dfs()
                    cpu_schedule[cpu_idx].pop()
                    n_finish -= 1
                    finished[i] = False
                    cpu_time[cpu_idx] = old_time
        dfs()
        return mn_time, ans


tasks = [(0, 5), (1, 3), (2, 1), (4, 2)]  # (start_time, duration)
num_cpus = 2  # 6
print(Solution().get_min_time(tasks, num_cpus))  # Output will be the minimum time to complete all tasks
