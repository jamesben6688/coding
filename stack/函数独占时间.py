from typing import List


class Solution:
    def exclusiveTime_1(self, n: int, logs: List[str]) -> List[int]:
        """
            如果是O(1) space, 可以用O(N^2)扫描, 每次统计1~n的时间
        """
        ans = [0 for _ in range(n)]

        stack = []
        last_start = 0

        for log in logs:
            pid, tag, t = log.split(":")
            pid = int(pid)
            t = int(t)

            if tag == "start":
                if stack:
                    ans[stack[-1]] += t - last_start
                stack.append(pid)
                last_start = t  # 记录上一次的开始时间
            elif tag == 'end':
                last_pid = stack.pop()
                ans[last_pid] += t + 1 - last_start  # 记录上一次的开始时间
                last_start = t + 1

        return ans

    def exclusiveTime(self, n, logs):
        """

            O(1)空间
        :param n:
        :param logs:
        :return:
        """
        res = [0] * n

        i = 0
        while i < len(logs):
            if logs[i] == "-":
                i += 1
                continue

            fid_i, type_i, time_i = logs[i].split(':')
            fid_i = int(fid_i)
            time_i = int(time_i)

            if type_i == 'start':
                count = 1
                j = i + 1
                while j < len(logs):
                    if logs[j] == "-":
                        j += 1
                        continue
                    fid_j, type_j, time_j = logs[j].split(':')
                    fid_j = int(fid_j)
                    time_j = int(time_j)
                    if fid_j == fid_i:
                        if type_j == 'start':
                            count += 1
                        else:
                            count -= 1
                            if count == 0:
                                break
                    j += 1

                # logs[i] 与 logs[j] 是匹配的 start/end
                duration = int(logs[j].split(':')[2]) - time_i + 1

                # 扣除内部嵌套函数时间（再次遍历中间区间）
                k = i + 1
                inner_time = 0
                while k < j:
                    if logs[k] == "-":
                        k += 1
                        continue
                    _, t, t_start = logs[k].split(':')
                    if t == 'start':
                        count2 = 1
                        m = k + 1
                        while m < j:
                            if logs[m] == "-":
                                m += 1
                                continue
                            _, t2, _ = logs[m].split(':')
                            if t2 == 'start':
                                count2 += 1
                            else:
                                count2 -= 1
                                if count2 == 0:
                                    break
                            m += 1
                        inner_time += int(logs[m].split(':')[2]) - int(t_start) + 1
                        k = m + 1
                    else:
                        k += 1

                res[fid_i] += duration - inner_time
                logs[i] = "-"
                logs[j] = "-"
            i += 1

        return res


print(Solution().exclusiveTime(
2, ["0:start:0","1:start:2","1:end:5","0:end:6"]
))