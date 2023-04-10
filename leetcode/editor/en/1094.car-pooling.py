#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = [(trip[1], trip[2], trip[0]) for trip in trips] # [from, to, numPassengers]
        heapq.heapify(trips)
        p = 0
        while trips:
            trip = heapq.heappop(trips)
            if trip[1] == -1:
                p -= trip[2]
            else:
                p += trip[2]
                if p > capacity:
                    return False
                heapq.heappush(trips, (trip[1], -1, trip[2]))
        return True
            

# @lc code=end

