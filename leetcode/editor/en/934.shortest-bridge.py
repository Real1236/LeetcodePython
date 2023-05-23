#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        def isValid(row,col):
            return row < 0 or col < 0 or row == len(grid) or col == len(grid[0])

        def findIsland(row, col):
            if isValid(row,col) or not grid[row][col] or (row,col) in visited:
                return False
            visited.add((row,col))
            grid[row][col] = 2
            for dir in directions:
                findIsland(row + dir[0], col + dir[1])
            return True
        
        island_found = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if findIsland(row, col):
                    island_found = True
                    break
            if island_found:
                break

        distance = -1
        cells = deque(visited)
        while cells:
            size = len(cells)
            for _ in range(size):
                row, col = cells.popleft()
                if grid[row][col] == 1:
                    return distance
                visited.add((row,col))
                for dir in directions:
                    new_row, new_col = row + dir[0], col + dir[1]
                    if isValid(new_row, new_col) or (new_row, new_col) in visited:
                        continue
                    cells.append((new_row, new_col))
                    visited.add((new_row, new_col))
            distance += 1
        
# @lc code=end
solution = Solution()
grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(grid)
print(solution.shortestBridge(grid))
print("")
print(grid)