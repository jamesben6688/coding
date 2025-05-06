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

# Example usage:
tasks = [(0, 5), (1, 3), (2, 1), (4, 2)]  # (start_time, duration)
num_cpus = 2  # 6
print(Solution().min_time(tasks, num_cpus))  # Output will be the minimum time to complete all tasks

