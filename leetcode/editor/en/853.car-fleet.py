#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        
        res = 0
        longest_time = 0
        for p, s in cars:
            time = (target - p) / s
            if time > longest_time:
                longest_time = time
                res += 1
                
        return res

# @lc code=end
solution = Solution()
solution.carFleet(100, [0,2,4], [4,2,1])
