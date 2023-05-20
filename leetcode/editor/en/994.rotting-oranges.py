#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
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

# @lc code=end
solution = Solution()
print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
