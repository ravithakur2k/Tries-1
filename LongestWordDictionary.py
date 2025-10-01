#Time complexity: O(N * L) for insert, search and startsWith where n is the number of words and L in the length of each word
#Space Complexity: O(n) for using the array data structure for children
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Using the trie data structure we store all the words and then either using a DFS or BFS approach we can get the longest word. In BFS to use the lexicographical nature
# we can iterate the loop from the back as shown.

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = [None] * 26

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = TrieNode()
            curr = curr.children[ord(c) - ord('a')]
        curr.isWord = True

    def longestWordBFS(self, words: List[str]) -> str:
        curr = self.root
        self.result = ""
        for word in words:
            self.insert(word)
        self.bfs(curr)
        return self.result

    def bfs(self, root):
        currStr = ""
        q = deque()
        strQ = deque()
        q.append(root)
        strQ.append(currStr)

        while q:
            curr = q.popleft()
            currStr = strQ.popleft()
            for i in range(25, -1, -1):
                if curr.children[i] != None and curr.children[i].isWord:
                    q.append(curr.children[i])
                    strQ.append(currStr + chr(i + ord('a')))
        self.result = currStr

    def longestWordDFS(self, words: List[str]) -> str:
        curr = self.root
        self.result = ""
        for word in words:
            self.insert(word)
        self.dfs(curr, [])
        return self.result

    def dfs(self, curr, path):
        if len(self.result) < len(path):
            self.result = "".join(path)
        for i in range(26):
            if (curr.children[i] != None and curr.children[i].isWord):
                path.append(chr(i + ord('a')))
                self.dfs(curr.children[i], path)
                path.pop()




