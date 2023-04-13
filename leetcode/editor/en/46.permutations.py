#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur: List[int], remaining: set) -> None:
            if len(cur) == len(nums):
                res.append(cur)
                return
            for num in remaining:
                new_perm = cur.copy()
                new_set = remaining.copy()
                new_set.remove(num)

                new_perm.append(num)
                dfs(new_perm, new_set)
        
        dfs([], set(nums))
        return res

# @lc code=end
solution = Solution()
print(solution.permute([1,2,3]))
