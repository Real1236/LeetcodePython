# Question 1 - Arrays
# Given a 2D array, print the elements of the array in a clockwise spiral from starting from top left.

# Example 1:
# Input:
# matrix = [[1,    2,   3,   4],
#                 [5,    6,   7,   8],
#                 [9,   10,  11,  12],
#                 [13,  14,  15,  16]]
# Output:
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
# Explanation: 
# The output is matrix in spiral format. 

# Example 2: 
# Input:
# matrix =  [[1,   2,   3,   4,  5,   6],
#                  [7,   8,   9,  10,  11,  12],
#                  [13,  14,  15, 16,  17,  18]]
# Output:
# 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
# Explanation: 
# The output is matrix in spiral format.

from typing import List


def printSpiral(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    res = []

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    print(" ".join(map(str, res)))

matrix = [[1,    2,   3,   4],
                [5,    6,   7,   8],
                [9,   10,  11,  12],
                [13,  14,  15,  16]]
printSpiral(matrix)

matrix =  [[1,   2,   3,   4,  5,   6],
                 [7,   8,   9,  10,  11,  12],
                 [13,  14,  15, 16,  17,  18]]
printSpiral(matrix)

# Test Case 3:
matrix3 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
printSpiral(matrix)

# Test Case 4:
matrix4 = [[]]
printSpiral(matrix)

# It iteratively reduces the boundaries of the array (top, bottom, left, right) to traverse and print the outer layers before moving inward, until all elements are printed.