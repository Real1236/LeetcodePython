#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        rows, cols = [set() for _ in range(n)], [set() for _ in range(n)]
        diag1, diag2 = [set() for _ in range(n * 2 - 1)], [set() for _ in range(n * 2 - 1)]

        def backtrack(row: int, col: int, board: List[str], numOfQs: int) -> int:
            if numOfQs == n:
                return 1
            res = 0
            while col < n:
                oldRow, oldCol = row, col
                row += 1
                if row == n:
                    row = 0
                    col += 1
                if self.isValidSquare(oldRow, oldCol, board, rows, cols, diag1, diag2):
                    board[oldRow] = board[oldRow][:oldCol] + "Q" + board[oldRow][oldCol + 1:]
                    rows.append(oldRow)
                    cols.append(oldCol)
                    diag1.append(oldRow + oldCol)
                    diag2.append(oldRow - oldCol)
                    res += backtrack(row, col, board, numOfQs + 1)
                    rows.remove(oldRow)
                    cols.remove(oldCol)
                    diag1.remove(oldRow + oldCol)
                    diag2.remove(oldRow - oldCol)
                    board[oldRow] = board[oldRow][:oldCol] + "." + board[oldRow][oldCol + 1:]
            return res
            
        return backtrack(0, 0, ["." * n for _ in range(n)], 0)
    
    def isValidSquare(self, row: int, col: int, board: List[str], rows: set, cols: set, diag1: set, diag2: set) -> bool:
        if row in rows or col in cols or row + col in diag1 or row - col in diag2:
            return False
        return True
        
# @lc code=end

