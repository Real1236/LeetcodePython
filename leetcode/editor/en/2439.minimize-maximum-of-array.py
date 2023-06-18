#
# @lc app=leetcode id=2439 lang=python3
#
# [2439] Minimize Maximum of Array
#

# @lc code=start
import math
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = res = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            res = max(res, math.ceil(total / (i + 1)))
        return res
        
# @lc code=end
solution = Solution()
print(solution.minimizeArrayValue([6,9,3,8,14]))
