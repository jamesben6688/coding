class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word


def find_non_match_unigrams_without_spaces(unigrams, bigrams):
    trie = Trie()

    # Insert bigrams into Trie
    for bigram in bigrams:
        trie.insert(bigram)

    result = []

    # Check unigrams against the Trie
    for unigram in unigrams:
        if not trie.search(unigram):
            result.append(unigram)

    return result


# Test the function
unigrams = ["new", "york", "hampshire", "french"]
bigrams = ["newyork", "newhampshire"]

print(find_non_match_unigrams_without_spaces(unigrams, bigrams))  # Output: ['french']
