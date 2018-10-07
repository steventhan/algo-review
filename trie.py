class TrieNode:
    def __init__(self):
        self.chars = {}
        self.end_of_word = False

    def __repr__(self):
        return "Node: {}, {}".format(self.chars, self.end_of_word)

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for char in word:
            cur.chars.setdefault(char, TrieNode())
            cur = cur.chars[char]
        cur.end_of_word = True

    def _search_node(self, word):
        cur = self.root
        for char in word:
            if char in cur.chars:
                cur = cur.chars[char]
            else: raise ValueError
        return cur


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        try:
            return self._search_node(word).end_of_word
        except ValueError:
            return False



    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        try:
            return isinstance(self._search_node(prefix), TrieNode)
        except ValueError:
            return False




# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
assert trie.search("apple") == True
assert trie.startsWith("apple") == True
print(trie.root)
