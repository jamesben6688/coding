from itertools import permutations
import random

"""
给你n个球员，每个球员有编号和weight。然后组队比赛，
两支队伍组成一个比赛，每个队k人，要求公平竞争，即队里的球员weight要么相同，要么相近。最后要求返回n/（k*2）个比赛。
每个队员只需要存在一个队伍里就可以了
"""
class Solution:
    def get_match(self, players, k):
        players = sorted(players, key=lambda x: (-x[1], x[0]))
        print(players)
        n = len(players)
        n_groups = n // k
        groups = [[] for _ in range(n_groups)]

        for i in range(k):
            cur_players = players[i*n_groups:(i+1)*n_groups]
            permutation = random.sample(cur_players, len(cur_players))
            for j in range(len(groups)):
                groups[j].append(permutation[j])

        return groups


print(Solution().get_match(
    players = [(1, 50), (2, 60), (3, 55), (4, 65), (5, 70), (6, 75), (7, 70), (8, 75)], k = 2
))



