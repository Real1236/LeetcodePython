#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = right = 0
        prev, count = None, 0
        while right < len(nums):
            if nums[right] != prev:
                prev = nums[right]
                count = 1
                nums[left] = nums[right]
                right += 1
                left += 1
            else:
                count += 1
                if count == 2:
                    nums[left] = nums[right]
                    right += 1
                    left += 1
                else:
                    while right < len(nums) and nums[right] == prev:
                        right += 1
        return left
        
# @lc code=end

