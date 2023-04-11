#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def backtrack(cur: List[int], index: int):
            cur.append(nums[index])
            res.append(cur.copy())
            for i in range(index + 1, len(nums)):
                backtrack(cur.copy(), i)
        
        for i in range(len(nums)):
            backtrack([], i)
        return res

# @lc code=end
solution = Solution()
print(solution.subsets([1,2,3]))
