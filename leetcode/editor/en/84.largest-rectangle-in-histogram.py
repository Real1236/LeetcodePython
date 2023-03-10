#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            index = i
            while stack and h <= stack[-1][1]:
                index, height = stack.pop()
                res = max(res, (i - index) * height)
            stack.append([index, h])
        while stack:
            index, height = stack.pop()
            res = max(res, (len(heights) - index) * height)
        return res
        
# @lc code=end
solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,6,3]))
print(solution.largestRectangleArea([2,4]))
