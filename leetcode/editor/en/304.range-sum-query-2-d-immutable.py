#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for row in range(len(matrix)):
            for col in range(1, len(matrix[row])):
                matrix[row][col] += matrix[row][col - 1]
        for col in range(len(matrix[0])):
            for row in range(1, len(matrix)):
                matrix[row][col] += matrix[row - 1][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.matrix[row2][col2]
        if col1 > 0:
            res -= self.matrix[row2][col1 - 1]
        if row1 > 0:
            res -= self.matrix[row1 - 1][col2]
        if col1 > 0 and row1 > 0:
            res += self.matrix[row1 - 1][col1 - 1]
        return res
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
obj = NumMatrix([[3, 0, 1, 4, 2], 
                 [5, 6, 3, 2, 1], 
                 [1, 2, 0, 1, 5], 
                 [4, 1, 0, 1, 7], 
                 [1, 0, 3, 0, 5]])
