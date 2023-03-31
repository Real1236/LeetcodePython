#
# @lc app=leetcode id=1985 lang=python3
#
# [1985] Find the Kth Largest Integer in the Array
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return heapq.heappop(nums)
        
# @lc code=end

