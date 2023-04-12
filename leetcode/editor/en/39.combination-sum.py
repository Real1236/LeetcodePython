#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(comb: List[int], index: int, remaining: int) -> None:
            if remaining < 0:
                return
            if remaining == 0:
                res.append(comb)
            for i in range(index, len(candidates)):
                new_list = comb.copy()
                new_list.append(candidates[i])
                dfs(new_list, i, remaining - candidates[i])
        dfs([], 0, target)
        return res

# @lc code=end
solution = Solution()
print(solution.combinationSum([2,3,6,7], 7))
