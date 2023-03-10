#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        inc_stack = []  # -> [original index, updated index, number]
        res = 0
        for i, n in enumerate(arr):
            updated = i
            while inc_stack and n < inc_stack[-1][2]:
                original, updated, num = inc_stack.pop()
                res += (i - original) * (original + 1 - updated) * num
            inc_stack.append([i, updated, n])

        while inc_stack:
            original, updated, num = inc_stack.pop()
            res += (len(arr) - original) * (original + 1 - updated) * num

        return res % (10 ** 9 + 7)
        
# @lc code=end
solution = Solution()
print(solution.sumSubarrayMins([3,1,2,4]))
print(solution.sumSubarrayMins([11,81,94,43,3]))
