#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if (mid > 0 and nums[mid - 1] > nums[mid]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                right = mid - 1
            elif (mid == 0 or nums[mid - 1] < nums[mid]) and (mid < len(nums) - 1 and nums[mid] < nums[mid + 1]):
                left = mid + 1
            elif (mid > 0 and nums[mid - 1] > nums[mid]) and (mid < len(nums) - 1 and nums[mid] < nums[mid + 1]):
                left = mid + 1
            else:
                return mid
        


# @lc code=end
solution = Solution()

nums = [1,2,3,1]
print(solution.findPeakElement(nums))

nums = [1,2,1,3,5,6,4]
print(solution.findPeakElement(nums))

nums = [1]
print(solution.findPeakElement(nums))

nums = [2,1]
print(solution.findPeakElement(nums))
