#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        res = []
        left = 0
        for right in range(len(nums)):
            while window and nums[window[-1]] <= nums[right]:
                window.pop()
            window.append(right)

            if left > window[0]:
                window.popleft()

            if right >= k - 1:
                res.append(nums[window[0]])
                left += 1
        
        return res    

        
# @lc code=end

