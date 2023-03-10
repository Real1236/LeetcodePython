#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for asteroid in asteroids:
            if asteroid > 0:
                res.append(asteroid)
            else:
                left_destroyed = False
                while res and res[-1] > 0:
                    if asteroid * -1 > res[-1]:
                        res.pop()
                    elif asteroid * -1 < res[-1]:
                        left_destroyed = True
                        break
                    else:
                        res.pop()
                        left_destroyed = True
                        break
                if not left_destroyed:
                    res.append(asteroid)
        return res
                

# @lc code=end

