def is_merge(word1, word2, merged):
    # 递归检查是否能将 word1 和 word2 归并成 merged
    # i: word1 的索引， j: word2 的索引， k: merged 的索引
    def dfs(i, j, k):
        # 如果 merged 已经完全匹配
        if k == len(merged):
            return i == len(word1) and j == len(word2)

        # 如果从 word1 取一个字符
        if i < len(word1) and word1[i] == merged[k]:
            if dfs(i + 1, j, k + 1):
                return True

        # 如果从 word2 取一个字符
        if j < len(word2) and word2[j] == merged[k]:
            if dfs(i, j + 1, k + 1):
                return True

        return False

    return dfs(0, 0, 0)


def find_merge_pair(dictionary, merged):
    # 遍历字典中的每一对单词
    for i in range(len(dictionary)):
        for j in range(len(dictionary)):
            if i == j:
                continue  # 不要自己和自己配对
            w1, w2 = dictionary[i], dictionary[j]

            # 如果 word1 和 word2 的长度和 merged 长度不匹配，跳过
            if len(w1) + len(w2) != len(merged):
                continue

            # 使用 DFS 检查 w1 和 w2 是否能合并成 merged
            if is_merge(w1, w2, merged):
                return w1, w2  # 找到一对有效的单词

    return None  # 没有找到匹配的单词对


# 示例输入
dictionary = ["alpha", "apple", "aalph", "alaph", "beta", "banana"]
merged = "abelphata"

# 调用函数并输出结果
result = find_merge_pair(dictionary, merged)
print(result)  # 输出: ('alpha', 'beta')

# O(N^2L)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False  # 标记是否为一个完整的单词

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 构建 Trie 树
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    # 查找是否能通过与给定单词合并形成目标字符串
    def can_merge(self, word1, merged):
        memo = {}

        def dfs(i, node, k):
            # 用于记忆化搜索，避免重复计算
            if (i, id(node), k) in memo:
                return False
            if i == len(word1) and k == len(merged):
                return node.is_word  # 当 w1 和 w2 都用完时，返回 Trie 中是否存在完整的单词
            if k >= len(merged):
                return False

            res = False
            # 选项 1: 从 w1 取字符
            if i < len(word1) and merged[k] == word1[i]:
                res |= dfs(i + 1, node, k + 1)
            # 选项 2: 从 Trie（即 w2）取字符
            if merged[k] in node.children:
                res |= dfs(i, node.children[merged[k]], k + 1)

            memo[(i, id(node), k)] = not res
            return res

        return dfs(0, self.root, 0)

# 用来查找两个单词合并后的匹配情况
def find_merge_pair(dictionary, merged):
    trie = Trie()
    for word in dictionary:
        trie.insert(word)

    for word in dictionary:
        if len(word) > len(merged):
            continue
        # 通过 Trie 判断 word 是否可以合并到 merged 中
        if trie.can_merge(word, merged):
            # 提取剩下的部分作为另一个单词 w2
            i = j = 0
            w2 = []
            for c in merged:
                if i < len(word) and c == word[i]:
                    i += 1
                else:
                    w2.append(c)
            w2 = ''.join(w2)
            if w2 in set(dictionary):  # w2 必须是字典中的一个有效单词
                return word, w2
    return None
# O(NL)
# 示例输入
dictionary = ["alpha", "apple", "aalph", "alaph", "beta", "banana"]
merged = "abelphata"

# 调用函数并输出结果
result = find_merge_pair(dictionary, merged)
print(result)  # 输出: ('alpha', 'beta')

"""
Tire 解释
    当然可以，我们就用你的例子 merged = "abelphata"，字典是：

python
Copy
Edit
dictionary = ["alpha", "apple", "aalph", "alaph", "beta", "banana"]
目标：找出两个字典中的单词 w1 和 w2，使得 merge(w1, w2) == "abelphata"，字符顺序保持。

🔧 整体逻辑
你的算法是这样做的：

总体流程：
把所有单词插入 Trie，Trie 用来查找第二个单词 w2。

枚举每一个单词作为 w1。

尝试将 merged 拆解成 w1 和某个词 w2（Trie 中存在）。

用 DFS 判断 merged 是否可以通过两个词按字符顺序 merge 得到。

我们现在 详细一步步跟踪 第一次匹配的过程：

🧪 示例跟踪：merged = "abelphata"，尝试 w1 = "alpha"
我们想判断是否存在一个字典单词 w2，使得 merge("alpha", w2) == "abelphata"

🧠 函数调用：can_merge("alpha", "abelphata")
我们现在使用 DFS，来同时在 "alpha" 上用下标 i，在 Trie 上用节点 node，在 merged 上用下标 k 遍历，逐字符匹配。

🪜 步骤一：状态初始化
i = 0：alpha 的开头

k = 0：merged 的开头

node = root（Trie 根）

我们希望从 merged 的第一个字符开始，按照 merge 规则，从 w1 或 w2 取字符。

🌀 递归过程：
Step	merged[k]	操作说明	i	k	Trie path (w2)
1	'a'	word1[i] == 'a'，从 w1 拿字符，i → 1	1	1	
2	'b'	word1[i] != 'b'，Trie 中有 'b' 分支 → 走 w2	1	2	'b'
3	'e'	word1[i] != 'e'，Trie 中有 'e' → 继续	1	3	'be'
4	'l'	word1[i] != 'l'，Trie 中有 'l' → 继续	1	4	'bel'
5	'p'	word1[i] == 'p' → 走 word1，i → 2	2	5	'bel'
6	'h'	word1[i] == 'h' → i → 3	3	6	'bel'
7	'a'	word1[i] == 'a' → i → 4	4	7	'bel'
8	't'	word1[i] == 't' → i → 5	5	8	'bel'
9	'a'	word1 结束了 → 尝试 Trie 走 'a'	5	9	'beta' ✅

此时：

i = len("alpha") = 5，表示 w1 完成

Trie 正好走到了 "beta" 的结尾，并且是一个单词

所以说明："alpha" + "beta" → merge 成 "abelphata"

🎯 结果
返回成功！

于是你在 find_merge_pair 中，进一步提取另一个词 w2（从 merged 中去掉 w1 的字符）：

python
Copy
Edit
merged = "abelphata"
w1 = "alpha"
# 去掉 merged 中按顺序出现的 alpha 的字符，剩下的是 w2
处理后得到：

merged = abelphata

去掉 a l p h a → 剩下的是 'b', 'e', 't' → beta

于是：

python
Copy
Edit
return ("alpha", "beta")
🧠 总结你这个算法的好处
用 Trie + DFS 有效剪枝，不需要遍历所有单词对。

利用了 merge 顺序不打乱的特性。

可以高效地从一个 w1 找到可能的 w2（只要能通过 Trie 匹配出来）。
"""
