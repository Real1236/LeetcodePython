#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#

# @lc code=start
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        decreased = False
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                if decreased:
                    return False
                if i == len(nums) - 2:
                    return True
                if i == 0:
                    decreased = True
                    continue
                if nums[i - 1] > nums[i + 1] and nums[i] > nums[i + 2]:
                    return False
                decreased = True
        return True
        
# @lc code=end
solution = Solution()
print(solution.checkPossibility([4,5,2,3]))
