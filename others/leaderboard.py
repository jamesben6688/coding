from collections import OrderedDict
from sortedcontainers import SortedList


class Leaderboard:

    def __init__(self):
        self.id_score = OrderedDict()
        self.scores = SortedList()

    def addScore(self, playerId: int, score: int) -> None:
        self.id_score[playerId] = score
        self.scores.add(score)

    def top(self, K: int) -> int:
        # print(self.scores.values())
        print(self.scores)
        return sum(self.scores[-K:])

    def reset(self, playerId: int) -> None:
        # del self.scores[playerId]
        self.scores.remove(self.id_score[playerId])
        del self.id_score[playerId]



s = Leaderboard()
ops = ["Leaderboard","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","addScore","top","reset","reset","addScore","reset"]
op = [[],[1,13],[2,93],[3,84],[4,6],[5,89],[6,31],[7,7],[8,1],[9,98],[10,42],[5],[1],[2],[3,76],[4,68],[1],[3],[4],[2,70],[2]]

for i in range(1, len(ops)):
    if ops[i] == "addScore":
        s.addScore(*op[i])
        print(s.scores)
    elif ops[i] == 'top':
        print(s.top(*op[i]))
    elif ops[i] == 'reset':
        s.reset(*op[i])
        print(s.scores)