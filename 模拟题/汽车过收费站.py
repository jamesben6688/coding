from collections import defaultdict


class Car:
    def getCost(self, logs, mult, dist):
        cost = 0
        map = defaultdict(list)
        for log in logs:
            chpt, car, time = log
            map[car].append((time, chpt))

        ans = defaultdict(int)
        for k in map:
            cost = 0
            value = map[k]  # value in map.values():
            value.sort()
            prev = 0
            for i in value:
                t, chpt = i
                if prev:  # 跳过第一个收费站, 从第二个收费站开始算钱
                    cost += dist[(chpt, prev)]
                prev = chpt

            ans[k] = cost * mult

        return ans


"""
    1:
        1, 0
        2, 1
        3, 3
    2:
        1, 2
        2, 6
"""
val = Car()
logs = [[1,1,0],[2,1,1],[3,1,3],[1,2,2],[2,2,6]]

mult = 5

dist = {(2, 1): 3, (3, 2): 5}

ans = val.getCost(logs, mult, dist)
print(ans)