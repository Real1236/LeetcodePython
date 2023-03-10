#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(left: int, right: int, leftBias: bool) -> int:
            index = -1
            while left <= right:
                middle = (left + right) // 2
                if target > nums[middle]:
                    left = middle + 1
                elif target < nums[middle]:
                    right = middle - 1
                else:
                    index = middle
                    if leftBias:
                        right = middle - 1
                    else:
                        left = middle + 1
            return index

        l = binarySearch(0, len(nums) - 1, True)
        if l == -1:
            return [-1, -1]
        r = binarySearch(l, len(nums) - 1, False)
        return [l, r]
        
# @lc code=end
solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 8))
print(solution.searchRange([5,7,7,8,8,10], 6))
print(solution.searchRange([], 0))
