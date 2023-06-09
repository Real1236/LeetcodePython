#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cMin = cMax = 0
        gMin, gMax = float('inf'), float('-inf')
        for n in nums:
            cMin = min(n, cMin + n)
            cMax = max(n, cMax + n)
            gMin = min(gMin, cMin)
            gMax = max(gMax, cMax)
        return max(gMax, sum(nums) - gMin) if gMax > 0 else gMax
        
# @lc code=end
solution = Solution()
print(solution.maxSubarraySumCircular([5,-3,5]))
print(solution.maxSubarraySumCircular([-3,-2,-3]))
