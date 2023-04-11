#
# @lc app=leetcode id=1383 lang=python3
#
# [1383] Maximum Performance of a Team
#

# @lc code=start
import heapq
import math
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = [(e, s) for e, s in zip(efficiency, speed)]
        engineers.sort(reverse=True)
        top_speeds = []
        speed = 0
        res = 0
        for eng in engineers:
            speed += eng[1]
            heapq.heappush(top_speeds, eng[1])
            if len(top_speeds) > k:
                speed -= heapq.heappop(top_speeds)
            res = max(speed * eng[0], res)
        return res % (10**9 + 7)

# @lc code=end
solution = Solution()
print(solution.maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2))
