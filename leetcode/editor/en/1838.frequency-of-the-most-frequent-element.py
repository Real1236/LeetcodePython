#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, operations, res = 0, 0, 0

        largest = nums[0]
        for right in range(len(nums)):
            operations += (nums[right] - largest) * (right - left)
            largest = max(largest, nums[right])

            if operations > k:
                operations -= largest - nums[left]
                left += 1
            else:
                res = max(res, right - left + 1)

        return res
        
# @lc code=end
solution = Solution()
print(solution.maxFrequency([1,2,4], 5))
print(solution.maxFrequency([1,4,8,13], 5))
print(solution.maxFrequency([3,9,6], 2))
print(solution.maxFrequency([3,9,6,1], 2))
