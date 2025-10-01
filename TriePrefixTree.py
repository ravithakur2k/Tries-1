#Time complexity: O(N * L) for insert, search and startsWith where n is the number of words and L in the length of each word
#Space Complexity: O(n) for using the array data structure for children
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Using the trie data structure we can efficiently search prefixes


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = TrieNode()
            curr = curr.children[ord(c) - ord('a')]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                return False
            curr = curr.children[ord(c) - ord('a')]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if curr.children[ord(c) - ord('a')] == None:
                return False
            curr = curr.children[ord(c) - ord('a')]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)