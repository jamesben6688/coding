from collections import defaultdict


# 统计 bigram 频率
def build_bigram_freq(sentences):
    # 可以把查找的时候里面设计成最大堆, 节省查找的时间
    # 但是建模的时间更长
    bigram_freq = defaultdict(lambda: defaultdict(int))

    # 遍历每个句子
    for sentence in sentences:
        for i in range(len(sentence) - 1):
            word1 = sentence[i]
            word2 = sentence[i + 1]
            bigram_freq[word1][word2] += 1

    return bigram_freq


# 给定一个词，预测下一个最可能的词
def predict_next_word(word, bigram_freq):
    if word in bigram_freq:
        next_word_freq = bigram_freq[word]
        # 获取频率最高的下一个词
        predicted_word = max(next_word_freq, key=next_word_freq.get)
        return predicted_word
    else:
        return None  # 如果该词后面没有记录，则返回 None


# 示例句子列表
sentences = [
    ["I", "am", "learning", "Python"],
    ["I", "am", "learning", "data", "science"],
    ["I", "like", "Python"],
    ["I", "like", "ML"],
    ["I", "like", "DL"],
    ["Python", "is", "great"]
]

# 构建 bigram 频率字典
bigram_freq = build_bigram_freq(sentences)

# 给定词语，预测下一个词
word = "I"
predicted_word = predict_next_word(word, bigram_freq)
print(f"The next word after '{word}' is: {predicted_word}")
