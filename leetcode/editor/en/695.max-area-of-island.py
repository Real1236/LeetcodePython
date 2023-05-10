#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(row: int, col: int) -> int:
            if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) 
                or visited[row][col] or grid[row][col] == 0):
                return 0
            
            visited[row][col] = 1
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            area = 1
            for dir in directions:
                area += dfs(row + dir[0], col + dir[1])
            return area

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visited[row][col] or grid[row][col] == 0:
                    visited[row][col] = 1
                    continue
                res = max(res, dfs(row, col))
        
        return res
        
# @lc code=end
solution = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(solution.maxAreaOfIsland(grid))
