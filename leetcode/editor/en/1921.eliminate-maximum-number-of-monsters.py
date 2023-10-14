#
# @lc app=leetcode id=1921 lang=python3
#
# [1921] Eliminate Maximum Number of Monsters
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = [dist[i]/speed[i] for i in range(len(dist))]
        times.sort()
        for i, time in enumerate(times):
            if time <= i:
                return i
        return len(times)
    

# @lc code=end
solution = Solution()
print(solution.eliminateMaximum([1,3,4], [1,1,1]))
print(solution.eliminateMaximum([1,1,2,3], [1,1,1,1]))
print(solution.eliminateMaximum([3,2,4], [5,3,2]))
print(solution.eliminateMaximum([4,2,3], [2,1,1]))
