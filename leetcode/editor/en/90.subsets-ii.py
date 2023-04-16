#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def dfs(subset: List[int], counts: dict) -> None:
            numbers = list(counts.keys())
            for num in numbers:
                new_subset = subset.copy()
                new_subset.append(num)
                res.append(new_subset)

                if counts[num] > 1:
                    counts[num] -= 1
                else:
                    counts.pop(num)
                new_counts = counts.copy()
                dfs(new_subset, new_counts)
                if counts[num]:
                    counts.pop(num)

        dfs([], Counter(nums))
        return res
        
# @lc code=end

