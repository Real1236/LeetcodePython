#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minimums = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] < minimums[-1]:
                minimums.append(nums[i])
            else:
                minimums.append(minimums[-1])
        
        j = []
        for i in range(len(nums) - 1, -1, -1):
            while j and nums[i] > j[-1]:
                if j[-1] > minimums[i]:
                    return True
                j.pop()
            j.append(nums[i])

        return False
        
# @lc code=end
solution = Solution()
print(solution.find132pattern([3,1,4,2]))
