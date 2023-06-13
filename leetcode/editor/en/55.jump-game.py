#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        endIndex = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= endIndex:
                endIndex = i
        return endIndex == 0

# @lc code=end
solution = Solution()
print(solution.canJump([2,3,1,1,4]))
print(solution.canJump([3,2,1,0,4]))
