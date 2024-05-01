#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res, count = 0, 0
        for num in nums:
            if num:
                count = 0
                continue

            count += 1
            res += count
        
        return res

# @lc code=end

