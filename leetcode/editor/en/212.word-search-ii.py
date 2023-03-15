#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
from typing import List


class Node:
    def __init__(self) -> None:
        self.children = {}
        self.word = False
    
    def addWord(self, word: str) -> None:
        cur = self
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = Node()
            cur = cur.children[letter]
        cur.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(row: int, col: int, cur: Node, visited: List[List[bool]], word: str, words_found: set) -> None:
            if visited[row][col]:
                return
            
            letter = board[row][col]
            if letter in cur.children:
                visited[row][col] = True
                word += letter
                if col + 1 < len(board[0]):
                    dfs(row, col + 1, cur.children[letter], visited, word, words_found)
                if col - 1 >= 0:
                    dfs(row, col - 1, cur.children[letter], visited, word, words_found)
                if row + 1 < len(board):
                    dfs(row + 1, col, cur.children[letter], visited, word, words_found)
                if row - 1 >= 0:
                    dfs(row - 1, col, cur.children[letter], visited, word, words_found)
                visited[row][col] = False
                if cur.children[letter].word and word not in words_found:
                    words_found.add(word)

        root = Node()
        for word in words:
            root.addWord(word)
        
        words_found = set()
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, root, visited, '', words_found)

        return list(words_found)

        
# @lc code=end
solution = Solution()

# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]
# print(solution.findWords(board, words))

# board = [["a","b"],["c","d"]]
# words = ["abcb", "abdc", "abdca"]
# print(solution.findWords(board, words))

board = [["a"]]
words = ["a"]
print(solution.findWords(board, words))

