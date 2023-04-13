#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(cur: List[int], index: int) -> None:
            if len(cur) == k:
                res.append(cur)
                return
            for i in range(index + 1, n + 1):
                new = cur.copy()
                new.append(i)
                dfs(new, i)
        
        dfs([], 0)
        return res

# @lc code=end
solution = Solution()
print(solution.combine(4, 2))
