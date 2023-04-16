#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(perm: List[int], counts: dict) -> None:
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            keys = list(counts.keys())
            for key in keys:
                perm.append(key)
                if counts[key] == 1:
                    counts.pop(key)
                else:
                    counts[key] -= 1

                dfs(perm, counts)

                if counts[key]:
                    counts[key] += 1
                else:
                    counts[key] = 1
                perm.pop()
        
        dfs([], Counter(nums))
        return res

# @lc code=end
solution = Solution()
print(solution.permuteUnique([1,1,2]))
