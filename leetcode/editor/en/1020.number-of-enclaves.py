#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or not grid[row][col]:
                return 0
            
            count = 1
            grid[row][col] = 0
            if row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1:
                count = -1
            
            for dx, dy in directions:
                res = dfs(row + dx, col + dy)
                if count == -1 or res == -1:
                    count = -1
                else:
                    count += res

            return count
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                res = dfs(row, col)
                if res > 0:
                    count += res
        
        return count

# @lc code=end
solution = Solution()

grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(solution.numEnclaves(grid))

grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(solution.numEnclaves(grid))