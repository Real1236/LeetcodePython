#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finishedBananas(k: int) -> bool:
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / k)
                if hours > h:
                    return False
            if hours <= h:
                return True

        left, right = 0, max(piles)
        res = right
        while left <= right:
            k = (left + right) // 2
            if k == 0:
                break
            finished = finishedBananas(k)
            if finished:
                right = k - 1
                res = min(res, k)
            else:
                left = k + 1
        return res

# @lc code=end
solution = Solution()
print(solution.minEatingSpeed([3,6,7,11], 8))
print(solution.minEatingSpeed([30,11,23,4,20], 5))
print(solution.minEatingSpeed([30,11,23,4,20], 6))
print(solution.minEatingSpeed([312884470], 968709470))
