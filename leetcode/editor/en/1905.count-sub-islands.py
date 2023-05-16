#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#

# @lc code=start
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid2[0]))] for _ in range(len(grid2))]
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(row, col):
            if (row < 0 or col < 0 or row >= len(grid2) or col >= len(grid2[0]) 
                or not grid2[row][col] or visited[row][col]):
                return True

            visited[row][col] = True
            res = True
            if not grid1[row][col]:
                res = False
            for dir in directions:
                res = dfs(row + dir[0], col + dir[1]) and res
            return res
            
        
        res = 0
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] and not visited[row][col] and dfs(row, col):
                    res += 1

        return res
        
# @lc code=end
solution = Solution()
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
# grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
print(solution.countSubIslands(grid1, grid2))
