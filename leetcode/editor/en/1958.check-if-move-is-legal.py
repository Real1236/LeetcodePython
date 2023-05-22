#
# @lc app=leetcode id=1958 lang=python3
#
# [1958] Check if Move is Legal
#

# @lc code=start
from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        def findEnd(dir: List[int]) -> tuple:
            row, col = rMove + dir[0], cMove + dir[1]
            opp_color = "B"
            if color == "B":
                opp_color = "W"
            length = 2
            while board[row][col] == opp_color:
                row, col = row + dir[0], col + dir[1]
                if row < 0 or col < 0 or row == len(board) or col == len(board[0]):
                    return (-1,-1)
                length += 1
            return (row,col) if length >= 3 else (-1,-1)

        directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
        for dir in directions:
            end = findEnd(dir)
            if end == (-1,-1):
                continue
            if board[end[0]][end[1]] == color:
                return True
        return False
        
# @lc code=end
solution = Solution()
board = [[".",".",".",".","W","B","B","B"],[".",".",".",".",".",".",".","B"],["W",".",".","W",".",".","W","."],["B",".","B","B","B",".",".","W"],["W",".",".","B","W","B","B","."],["W","B",".",".","W","B","B","."],[".","W","B","B","W","B",".","W"],["B",".","W","B","W",".","W","."]]
print(solution.checkMove(board, 0, 0, "B"))
