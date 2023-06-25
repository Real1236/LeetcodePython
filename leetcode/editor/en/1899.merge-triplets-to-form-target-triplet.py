#
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#

# @lc code=start
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        cur = [float("-inf") for _ in range(3)]
        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                cur = [max(a, cur[0]), max(b, cur[1]), max(c, cur[2])]
        return cur == target
        
# @lc code=end
solution = Solution()
print(solution.mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))
print(solution.mergeTriplets([[1,3,1]], [1,3,2]))
