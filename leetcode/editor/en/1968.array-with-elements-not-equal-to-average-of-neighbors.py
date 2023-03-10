#
# @lc app=leetcode id=1968 lang=python3
#
# [1968] Array With Elements Not Equal to Average of Neighbors
#

# @lc code=start
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        left, right = 0, len(nums) - 1
        while len(nums) != len(res):
            res.append(nums[left])
            left += 1

            if right > left:
                res.append(nums[right])
                right -= 1

        return res
        
# @lc code=end
solution = Solution()
solution.rearrangeArray([0,4,1,5,3])
