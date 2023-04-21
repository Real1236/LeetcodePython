#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        side_length = perimeter / 4

        matchsticks.sort(reverse=True)
        sides = [0 for _ in range(4)]
        def backtrack(index: int) -> bool:
            if index == len(matchsticks):
                return True

            m_length = matchsticks[index]
            for i in range(4):
                if sides[i] + m_length <= side_length:
                    sides[i] += m_length
                    if backtrack(index + 1):
                        return True
                    sides[i] -= m_length
            return False
              
        return backtrack(0)

# @lc code=end
solution = Solution()
print(solution.makesquare([1,1,2,2,2]))
print(solution.makesquare([3,3,3,3,4]))
print(solution.makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))
print(solution.makesquare([4,13,1,1,14,15,1,3,13,1,3,5,2,8,12]))
