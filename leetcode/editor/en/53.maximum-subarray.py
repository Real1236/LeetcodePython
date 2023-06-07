#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        index = cur = 0
        res = float("-inf")
        while index < len(nums):
            cur += nums[index]
            res = max(res, cur)
            if cur < 0:
                cur = 0
            index += 1
        return res

# @lc code=end
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(solution.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]))
