#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, index, visisted):
            if (row < 0 or col < 0 or row >= len(board) or col >= len(board[0])
                or board[row][col] != word[index]
                or visited[row][col]):
                return False
            if index == len(word) - 1:
                return True
            
            visited[row][col] = True
            index += 1
            if (backtrack(row + 1, col, index, visited)
                or backtrack(row, col + 1, index, visited)
                or backtrack(row - 1, col, index, visited)
                or backtrack(row, col - 1, index, visited)):
                return True
            visisted[row][col] = False
            return False

            
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, 0, visited):
                    return True
        
        return False

# @lc code=end
solution = Solution()

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(solution.exist(board, word))
