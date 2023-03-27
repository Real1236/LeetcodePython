#
# @lc app=leetcode id=1845 lang=python3
#
# [1845] Seat Reservation Manager
#

# @lc code=start
import heapq


class SeatManager:

    def __init__(self, n: int):
        self.unreserved = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        return heapq.heappop(self.unreserved)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved, seatNumber)
        

# @lc code=end

