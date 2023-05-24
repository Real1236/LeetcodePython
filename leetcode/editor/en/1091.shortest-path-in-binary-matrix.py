#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def isValid(row, col):
            return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])

        directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
        q = deque([(0,0)])
        visited = set((0,0))
        length = 1
        while q:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                if row == len(grid) - 1 and col == len(grid[0]) - 1 and not grid[row][col]:
                    return length
                for dir in directions:
                    new_row, new_col = row + dir[0], col + dir[1]
                    if isValid(new_row, new_col) and (new_row, new_col) not in visited and not grid[new_row][new_col]:
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
            length += 1
        return -1
        
# @lc code=end
solution = Solution()
grid = [[0,0,0],[1,1,0],[1,1,0]]
print(solution.shortestPathBinaryMatrix(grid))
