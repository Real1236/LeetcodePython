#
# @lc app=leetcode id=1984 lang=python3
#
# [1984] Minimum Difference Between Highest and Lowest of K Scores
#

# @lc code=start
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')
        for left in range(len(nums) + 1 - k):
            right = left + k - 1
            res = min(res, nums[right] - nums[left])
        return res

# @lc code=end

