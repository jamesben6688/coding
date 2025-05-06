# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

from typing import List
import random
from copy import deepcopy


class Solution:
    def findSecretWord(self,secret, words: List[str]) -> List:
        def get_sim(a, b):
            ans = 0
            for i in range(len(a)):
                if a[i] == b[i]:
                    ans += 1
            return ans

        for g in range(30):
            tmp = []
            r = random.randint(0, len(words)) % len(words)

            w = words[r]
            sim = get_sim(secret, w)
            if sim == 6:
                return [g, w]

            for j in range(len(words)):
                if j != r and get_sim(words[j], w) == sim:
                    tmp.append(words[j])

            words = deepcopy(tmp)


for i in range(20):
    print(Solution().findSecretWord(
    secret =
    "aaaata",
    words =
    ["aaaaga","aaaaka","aaauaa","aaaaoa","aafaaa","aaaaza","aaaava","agaaaa","aaagaa","aaaaqa","aaaaca","aaaaua","apaaaa","aawaaa","aaaaba","aaaqaa","aayaaa","aaaaja","aaacaa","aaayaa","aaaeaa","aavaaa","aasaaa","aaaapa","aaaaxa","aeaaaa","aaxaaa","akaaaa","aaaoaa","aazaaa","anaaaa","aaaala","aaraaa","aaaata","aaaaia","ajaaaa","aaaaaa","ahaaaa","aaaraa","aaaiaa","aanaaa","alaaaa","aakaaa","aiaaaa","aajaaa","aaakaa","axaaaa","aaqaaa","aaamaa","aapaaa","aaafaa","aaasaa","aadaaa","amaaaa","aaaaea","aabaaa","aaaama","asaaaa","acaaaa","aaiaaa","avaaaa","afaaaa","aoaaaa","aamaaa","aaaasa","aaawaa","azaaaa","aataaa","aaeaaa","aaaafa","aaahaa","aaalaa","aaaana","aaanaa","aaabaa","aaaada","auaaaa","aaapaa","awaaaa","ayaaaa","adaaaa","aaavaa","aagaaa","aauaaa","abaaaa","aaadaa","aqaaaa","aaaxaa","aaaawa","aaajaa","araaaa","aahaaa","aaaaha","aacaaa","aaaara","aaoaaa","ataaaa","aaaaya","aalaaa","aaazaa"]
    ))
