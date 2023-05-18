#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()
        
        def dfs(row, col):
            if row < 0 or col < 0 or row == ROWS or col == COLS or board[row][col] == "X" or (row, col) in visited:
                return
            visited.add((row, col))
            for dir in directions:
                dfs(row + dir[0], col + dir[1])

        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        for col in range(1, COLS - 1):
            dfs(0, col)
            dfs(ROWS - 1, col)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row, col) not in visited:
                    board[row][col] = "X"
        
# @lc code=end
board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
solution = Solution()
solution.solve(board)
for row in board:
    print(row)