#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(target):
            cur_sum = 0
            subarray = 1
            for num in nums:
                cur_sum += num
                if cur_sum > target:
                    subarray += 1
                    cur_sum = num
            return subarray <= k
        
        left, right = max(nums), sum(nums)
        res = right
        while left <= right:
            middle = left + ((right - left) // 2)
            if canSplit(middle):
                res = middle
                right = middle - 1
            else:
                left = middle + 1
        return res
        
# @lc code=end

