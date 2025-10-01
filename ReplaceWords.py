#Time complexity: O(N * L) for inserting into the Trie data structure where n is the number of words and L in the length of each word
#Space Complexity: O(n) for using the array data structure for children
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Using the trie data structure we can efficiently search prefixes and then replace words accordingly

class TrieNode:

    def __init__(self):
        self.isWord = False
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            if curr.isWord: break
            curr = curr.children[c]
        curr.isWord = True

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        result = []
        for word in dictionary:
            self.insert(word)
        splitStr = sentence.split(" ")
        for i in range(len(splitStr)):
            curr = self.root
            replacement = []
            if i > 0: result.append(" ")
            for c in splitStr[i]:
                if c not in curr.children or curr.isWord:
                    break
                replacement.append(c)
                curr = curr.children[c]
            if curr.isWord:
                result.append("".join(replacement))
            else:
                result.append(splitStr[i])

        return "".join(result)