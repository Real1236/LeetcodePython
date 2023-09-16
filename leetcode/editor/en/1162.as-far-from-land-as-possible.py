#
# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    q.append((row, col))
        
        if len(q) == len(grid) * len(grid[0]) or not q:
            return -1
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        level = 0
        while q:
            levelSize = len(q)
            for _ in range(levelSize):
                row, col = q.popleft()
                for dir in directions:
                    newRow, newCol = row + dir[0], col + dir[1]
                    if (0 <= newRow < len(grid) and 0 <= newCol < len(grid[0])
                        and not grid[newRow][newCol]):
                        grid[newRow][newCol] = 1
                        q.append((newRow, newCol))
            level += 1

        return level - 1



# @lc code=end
solution = Solution()
print(solution.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
print(solution.maxDistance([[1,0,0],[0,0,0],[0,0,0]]))
print(solution.maxDistance([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
print(solution.maxDistance([[1,0,0,0,0,1,0,0,0,1],
                            [1,1,0,1,1,1,0,1,1,0],
                            [0,1,1,0,1,0,0,1,0,0],
                            [1,0,1,0,1,0,0,0,0,0],
                            [0,1,0,0,0,1,1,0,1,1],
                            [0,0,1,0,0,1,0,1,0,1],
                            [0,0,0,1,1,1,1,0,0,1],
                            [0,1,0,0,1,0,0,1,0,0],
                            [0,0,0,0,0,1,1,1,0,0],
                            [1,1,0,1,1,1,1,1,0,0]]))
