#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#

# @lc code=start
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res, left, right = 0, 0, len(nums) - 1
        
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += (1 << (right - left))
                left += 1
        
        return res % (10 ** 9 + 7)
        
# @lc code=end
solution = Solution()
print(solution.numSubseq([3,5,6,7], 9))
print(solution.numSubseq([3,3,6,8], 10))
