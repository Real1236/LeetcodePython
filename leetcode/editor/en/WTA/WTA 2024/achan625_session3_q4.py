# Question 4 - Prefix Sum
# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Implement the NumMatrix class:

# NumMatrix(int[][] matrix): Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2): Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# You must design an algorithm where sumRegion works in O(1) time complexity.

# Example 1:

# Input:
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [
# [[3, 0, 1, 4, 2], 
# [5, 6, 3, 2, 1], 
# [1, 2, 0, 1, 5], 
# [4, 1, 0, 1, 7], 
# [1, 0, 3, 0, 5]], 
# [2, 1, 4, 3], 
# [1, 1, 2, 2], 
# [1, 2, 2, 4]
# ]
# Output:
# [null, 8, 11, 12]
# Explanation:
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // returns 8 (sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // returns 11 (sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // returns 12 (sum of the blue rectangle)

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.prefix_sums = []
        for r in range(len(matrix)):
            prefix_sum = 0
            row = []
            for c in range(len(matrix[0])):
                prefix_sum += matrix[r][c]
                row.append(prefix_sum)
            self.prefix_sums.append(row)
        
        for c in range(len(self.prefix_sums[0])):
            for r in range(1, len(self.prefix_sums)):
                self.prefix_sums[r][c] += self.prefix_sums[r - 1][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        big_rectangle = self.prefix_sums[row2][col2]
        left_rectangle = self.prefix_sums[row2][col1 - 1] if col1 else 0
        top_rectangle = self.prefix_sums[row1 - 1][col2] if row1 else 0
        top_left_rectangle = self.prefix_sums[row1 - 1][col1 - 1] if row1 and col1 else 0
        return big_rectangle - left_rectangle - top_rectangle + top_left_rectangle

matrix = [
    [3, 0, 1, 4, 2], 
    [5, 6, 3, 2, 1], 
    [1, 2, 0, 1, 5], 
    [4, 1, 0, 1, 7], 
    [1, 0, 3, 0, 5]
]
numMatrix = NumMatrix(matrix)
print(numMatrix.sumRegion(2, 1, 4, 3))
print(numMatrix.sumRegion(1, 1, 2, 2))
print(numMatrix.sumRegion(1, 2, 2, 4))

matrix1 = [
    [2, 5, 4], 
    [6, 3, 9], 
    [4, 7, 2]
]
numMatrix1 = NumMatrix(matrix1)
print(numMatrix1.sumRegion(0, 0, 1, 1))  # Expected output: 16
print(numMatrix1.sumRegion(1, 1, 2, 2))  # Expected output: 21

matrix2 = [
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12]
]
numMatrix2 = NumMatrix(matrix2)
print(numMatrix2.sumRegion(0, 1, 2, 3))  # Expected output: 63
print(numMatrix2.sumRegion(1, 0, 2, 2))  # Expected output: 48

# During initialization, the constructor creates a 2d prefix sum array. The sumRegion takes the sum of the lower right corner of the rectangle and subtracting the areas that are not part of the subregion. Therefore initialization is O(n*m) but sumRegion is O(1).