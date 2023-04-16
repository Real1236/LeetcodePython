#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(combo: List[int], index: int, total: int) -> None:
            if total >= target:
                if total == target:
                    res.append(combo)
                return
            i = index + 1
            while i < len(candidates):
                cand = candidates[i]
                new_combo = combo.copy()
                new_combo.append(cand)
                dfs(new_combo, i, total + cand)
                i += 1
                while candidates[i] == cand:
                    i += 1
        
        dfs([], -1, 0)
        return res

# @lc code=end
solution = Solution()
print(solution.combinationSum2([2,5,2,1,2], 5))
