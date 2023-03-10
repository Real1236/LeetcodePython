#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = min(nums[left], nums[right])
        while nums[left] > nums[right]:
            middle = (left + right) // 2
            if res > nums[middle]:
                right = middle
            elif res < nums[middle]:
                left = middle + 1
            res = min(nums[left], nums[right])
        return res
        
# @lc code=end
solution = Solution()
print(solution.findMin([3,4,5,1,2]))
print(solution.findMin([4,5,6,7,0,1,2]))
print(solution.findMin([11,13,15,17]))
print(solution.findMin([3,1,2]))
