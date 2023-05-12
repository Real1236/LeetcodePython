#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()

        def dfs(row: int, col: int, prevHeight: int, ocean: set):
            if (row < 0 or col < 0
                or row >= len(heights) or col >= len(heights[0]) or 
                prevHeight > heights[row][col] or (row, col) in ocean):
                return
            ocean.add((row, col))
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            for dir in directions:
                dfs(row + dir[0], col + dir[1], heights[row][col], ocean)

        for i in range(len(heights[0])):
            dfs(0, i, heights[0][i], pacific)
            dfs(len(heights) - 1, i, heights[len(heights) - 1][i], atlantic)
        for i in range(len(heights)):
            dfs(i, 0, heights[i][0], pacific)
            dfs(i, len(heights[0]) - 1, heights[i][len(heights[0]) - 1], atlantic)

        res = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in atlantic and (row,col) in pacific:
                    res.append([row, col])

        return res
        
# @lc code=end
solution = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(solution.pacificAtlantic(heights))