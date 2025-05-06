import re
from collections import defaultdict

"""
train一个list of sentences来预测一个string后面最有可能出现哪个单词。
用了两个map followup了时间复杂度 如何优化 我的solution本来是O(n) 问了如何优化我说那就应该有O1的solution咯 
小哥笑了问我怎么实现 改了一下map 又被问了如果一个单词有1/3可能性出现另外一个2/3可能性出现 如何保证出现概率

followup:
 如果你想让预测结果符合训练中学到的概率分布（比如某个单词后面有 1/3 的概率是 "apple"，2/3 的概率是 "banana"），那么我们就要在预测阶段用 随机采样（sampling），而不是总是取最大值（argmax）。

🧠 核心区别
argmax：总是返回概率最大的那个词 → 确定性（不保留概率信息）。

sampling：根据概率分布进行抽样 → 符合统计规律（可以还原训练分布）。
random.choices(words, weights=weights, k=1)
"""


class BigramPredictor:
    def __init__(self):
        self.model = defaultdict(Counter)

    def tokenize(self, sentence):
        return re.findall(r'\b\w+\b', sentence.lower())

    def train(self, sentences):
        for sentence in sentences:
            tokens = self.tokenize(sentence)
            for i in range(len(tokens) - 1):
                self.model[tokens[i]][tokens[i + 1]] += 1

    def predict_next(self, input_string, topk=1):
        tokens = self.tokenize(input_string)
        if not tokens:
            return None
        last_word = tokens[-1]
        next_words = self.model.get(last_word)
        if not next_words:
            return None
        return [word for word, _ in next_words.most_common(topk)]

    def sample_next(self, input_string):
        tokens = self.tokenize(input_string)
        if not tokens:
            return None
        last_word = tokens[-1]
        counter = self.model.get(last_word)
        if not counter:
            return None
        words, weights = zip(*counter.items())
        return random.choices(words, weights=weights, k=1)[0]
