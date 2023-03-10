#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if index >= 0 and index < len(nums) and nums[index] > 0:
                nums[index] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1
        
# @lc code=end
solution = Solution()
solution.firstMissingPositive([1,2,0])
