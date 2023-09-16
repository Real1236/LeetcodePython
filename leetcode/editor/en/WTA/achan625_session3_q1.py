# Question 1
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of conference rooms required.

# Example:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example:

# Input: intervals = [[7,10],[2,4]]
# Output: 1  


import heapq
from typing import List


class Solution:
    def roomsNeeded(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        endTimes = []

        res = 0
        for start, end in intervals:
            while endTimes and endTimes[0] <= start:
                heapq.heappop(endTimes)
            heapq.heappush(endTimes, end)
            res = max(res, len(endTimes))

        return res

solution = Solution()

# Example 1
print(solution.roomsNeeded([[0,30],[5,10],[15,20]]))

# Example 2
print(solution.roomsNeeded([[7,10],[2,4]]))

# # Test Case 1
print(solution.roomsNeeded([[0,30],[5,10],[15,20],[9,16],[20,50]]))

# Test Case 2
print(solution.roomsNeeded([[6,10],[1,3],[8,12],[4,7]]))

