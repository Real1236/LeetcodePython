#
# @lc app=leetcode id=1762 lang=python3
#
# [1762] Buildings With an Ocean View
#

# @lc code=start
from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []

        # Monotonic Stack
        for i, height in enumerate(heights):
            while res and height >= heights[res[-1]]:
                res.pop()
            res.append(i)

        # Scan from back
        # for i in range(len(heights) - 1, -1, -1):
        #     if not res or heights[i] > heights[res[-1]]:
        #         res.append(i)
        # res.reverse()

        return res
        
# @lc code=end
solution = Solution()
print(solution.findBuildings([4,2,3,1]))
print(solution.findBuildings([4,3,2,1]))
print(solution.findBuildings([1,3,2,4]))
print(solution.findBuildings([1,3,2,5,4,1,3]))
