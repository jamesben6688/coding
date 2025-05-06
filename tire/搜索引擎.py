from collections import defaultdict
from typing import List
from heapq import *


class TireNode:
    def __init__(self):
        self.children = defaultdict()

        # 记录当前字符后面的单词的批次
        # self.freq_sen = defaultdict(int)
        self.freq_sen = []  # 使用优先级队列


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        """
            初始化时间复杂度O(nl)，input时间复杂度O(l)，
            n是字符串数量，l是最长字符串长度，空间O(nl)
            题解: https://www.bilibili.com/video/BV1VT41137Cc/?spm_id_from=333.337.search-card.all.click&vd_source=515dedd17a7416a93307429c1b2dfa6b
        """
        self.root = TireNode()
        self.input_str = ""
        self.cur_node = self.root
        self.found = True

        n = len(times)
        for i in range(n):
            self.add(self.root, sentences[i], times[i])

    def add(self, node, sen, freq):
        for ch in sen:
            if ch not in node.children:
                node.children[ch] = TireNode()

            node = node.children[ch]

            found = False
            for i in range(len(node.freq_sen)):
                if node.freq_sen[i][1] == sen:
                    new_freq, new_sen = node.freq_sen.pop(i)
                    heappush(node.freq_sen, [new_freq - freq, new_sen])

                    found = True

                    break

            # 注意这个地方一定要heapify, 否则heapq会出现错误
            # 因为前面调用了list.pop操作,会破坏heapq的结构
            heapify(node.freq_sen)

            if not found:
                heappush(node.freq_sen, [-freq, sen])

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.add(self.root, self.input_str, 1)
            self.input_str = ""
            self.cur_node = self.root
            self.found = True
            return []
        else:
            self.input_str += c

            res = []
            i = 0
            # for child in self.cur_node.children[c]:

            if c not in self.cur_node.children or not self.found:
                self.found = False
                return []
            else:
                tmp_res = []
                while self.cur_node.children[c].freq_sen and i < 3:
                    freq, sen = heappop(self.cur_node.children[c].freq_sen)
                    res.append(sen)
                    tmp_res.append([freq, sen])

                    i += 1

                for tmp in tmp_res:
                    heappush(self.cur_node.children[c].freq_sen, tmp)

                self.cur_node = self.cur_node.children[c]
                return res

# Your AutocompleteSystem object will be instantiated and called as such:
obj = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
ins = [["i"], [" "], ["a"], ["#"]]
for ch in ins:
    param_1 = obj.input(ch[0])
    print(param_1)
