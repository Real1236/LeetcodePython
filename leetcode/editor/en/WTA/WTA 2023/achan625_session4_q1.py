# Question 1
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally 
# or move outside the boundary (i.e., wrap-around is not allowed).

# Example: 
# Input: matrix = [[9,9,4], [6,6,8], [2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9]. Start from matrix[2,1], move left to matrix[2,0], 
# move up to matrix[1,0], move up to matrix[0,0].

# Example:
# Input: [[3,4,5], [3,2,6], [2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed. Start from matrix[0,0], 
# move right to matrix[0,1], move right to matrix[0,2], move down to matrix[1,2].


from typing import List


class Solution:
    def longestPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(row: int, col: int, prev: int) -> int:
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or prev >= matrix[row][col]:
                return 0
            if (row, col) in dp:
                return dp[(row, col)]
            
            distance = 1
            for dir in directions:
                distance = max(distance, dfs(row + dir[0], col + dir[1], matrix[row][col]) + 1)

            dp[(row, col)] = distance
            return distance
        
        res = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                res = max(res, dfs(row, col, -1))
        
        return res

solution = Solution()

# Example 1
print(solution.longestPath([[9,9,4], [6,6,8], [2,1,1]]))

# Example 2
print(solution.longestPath([[3,4,5], [3,2,6], [2,2,1]]))

# Test Case 1
print(solution.longestPath([[1]]))

# Test Case 2
print(solution.longestPath([[6,10],[1,3],[8,12],[4,7]]))

