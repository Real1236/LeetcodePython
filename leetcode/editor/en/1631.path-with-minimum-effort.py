#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        
        minHeap = [[0, 0, 0]]   # [diff, row, col]
        visited = set()

        while minHeap:
            diff, row, col = heapq.heappop(minHeap)

            if (row, col) in visited:
                continue
            visited.add((row, col))

            if (row, col) == (ROWS - 1, COLS - 1):
                return diff

            for dr, dc in dirs:
                newRow, newCol = row + dr, col + dc

                if newRow >= ROWS or newCol >= COLS or newRow < 0 or newCol < 0 or (newRow, newCol) in visited:
                    continue

                heapq.heappush(minHeap, [max(diff, abs(heights[newRow][newCol] - heights[row][col])), newRow, newCol])

# @lc code=end
solution = Solution()
heights = [[4,3,4,10,5,5,9,2],
           [10,8,2,10,9,7,5,6],
           [5,8,10,10,10,7,4,2],
           [5,1,3,1,1,3,1,9],
           [6,4,10,6,10,9,4,6]]
print(solution.minimumEffortPath(heights))
