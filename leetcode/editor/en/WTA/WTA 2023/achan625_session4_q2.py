# Question 2
# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example:
# Input: grid = [[2,1,1], [1,1,0], [0,1,1]]
# Output: 4
# Explanation: 
# Minute 0: Rotten orange at [0,0]
# Minute 1: Rotten oranges at [0,0], [0,1], [1,0]
# Minute 2: Rotten oranges at [0,0], [0,1], [1,0], [0,2], [1,1]
# Minute 3: Rotten oranges at [0,0], [0,1], [1,0], [0,2], [1,1], [2,1]
# Minute 4: Rotten oranges at [0,0], [0,1], [1,0], [0,2], [1,1], [2,1], [2,2]
# Example:
# Input: grid = [[2,1,1], [0,1,1], [1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.


from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    fresh.add((row, col))
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        res = 0
        while rotten and fresh:
            size = len(rotten)
            for _ in range(size):
                row, col = rotten.popleft()
                for dir in directions:
                    new_row, new_col = row + dir[0], col + dir[1]
                    if (new_row < 0 or new_col < 0 
                        or new_row == len(grid) or new_col == len(grid[0])
                        or grid[new_row][new_col] != 1):
                        continue
                    grid[new_row][new_col] = 2
                    fresh.remove((new_row, new_col))
                    rotten.append((new_row, new_col))
            res += 1
        return res if not fresh else -1

solution = Solution()

# Example 1
print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]] ))

# Example 2
print(solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))

# Test Case 1
print(solution.orangesRotting([[0,2]]))

# Test Case 2
print(solution.orangesRotting([[1,0,1,2], [2,0,1,1], [2,1,1,1]]))

