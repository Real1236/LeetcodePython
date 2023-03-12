#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            number_need = target - num
            if number_need in hashmap:
                return [hashmap[number_need], i]
            hashmap[num] = i
        
# @lc code=end
#       0 1 2  3
nums = [2,7,11,15]

solution = Solution()
print(solution.twoSum(nums, 9))
