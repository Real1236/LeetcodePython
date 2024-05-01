'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''
import heapq
from typing import List

# # Approach 1: Priority Queue
# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         # Sort meeting rooms by start time
#         intervals.sort()

#         # Initialize variables
#         minHeap = []
#         res = 0

#         # Iterate through each meeting room
#         for start, end in intervals:
#             # Check minHeap for the earliest end time
#             while minHeap and minHeap[0] <= start:
#                 heapq.heappop(minHeap)

#             # Add room to minHeap
#             heapq.heappush(minHeap, end)

#             # Check number of rooms
#             res = max(res, len(minHeap))

#         return res
    
# Approach 2: 2 Arrays
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        0---------------------------30
            5-----10
                        15---20
        '''
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])

        s = e = res = count = 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        
        return res


solution = Solution()

intervals = [[0,30],[5,10],[15,20]]
res = solution.minMeetingRooms(intervals)
assert res == 2
print(res)

intervals = [[7,10],[2,4]]
res = solution.minMeetingRooms(intervals)
assert res == 1
print(res)