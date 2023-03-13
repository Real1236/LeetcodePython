#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class Node:
    
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = Node()
            cur = cur.children[letter]
        cur.is_word = True

    def search(self, word: str) -> bool:
        def dfs(j: int, cur: Node) -> bool:
            for i in range(j, len(word)):
                letter = word[i]
                if letter == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if letter not in cur.children:
                        return False
                    cur = cur.children[letter]
            return cur.is_word
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
wordDictionary = WordDictionary()

# # Test 1
# wordDictionary.addWord("bad")
# wordDictionary.addWord("dad")
# wordDictionary.addWord("mad")
# print(wordDictionary.search("pad"))  # return False
# print(wordDictionary.search("bad"))  # return True
# print(wordDictionary.search(".ad"))  # return True
# print(wordDictionary.search("b.."))  # return True

# Test 2
wordDictionary.addWord("a")
wordDictionary.addWord("a")
print(wordDictionary.search("."))  # return True
print(wordDictionary.search("a"))  # return True
print(wordDictionary.search("aa"))  # return False
print(wordDictionary.search("a"))  # return True
print(wordDictionary.search(".a"))  # return False
print(wordDictionary.search("a."))  # return False
