#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#

# @lc code=start
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(row, col, open):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col]:
                return open
            
            if not open and (row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1):
                open = True
                
            grid[row][col] = 1
            for dx, dy in directions:
                open = dfs(row + dx, col + dy, open) or open
            
            return open

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    continue
                if not dfs(row, col, False):
                    res += 1
        
        return res

# @lc code=end
solution = Solution()
grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
print(solution.closedIsland(grid))

grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
print(solution.closedIsland(grid))

grid = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]]
print(solution.closedIsland(grid))

grid = [[0,0,1,1,0,1,0,0,1,0],
        [1,1,0,1,1,0,1,1,1,0],
        [1,0,1,1,1,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,0,1],
        [0,0,0,0,0,0,1,1,1,0],
        [0,1,0,1,0,1,0,1,1,1],
        [1,0,1,0,1,1,0,0,0,1],
        [1,1,1,1,1,1,0,0,0,0],
        [1,1,1,0,0,1,0,1,0,1],
        [1,1,1,0,1,1,0,1,1,0]]
print(solution.closedIsland(grid))
