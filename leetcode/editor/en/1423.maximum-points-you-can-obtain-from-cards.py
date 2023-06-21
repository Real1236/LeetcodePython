#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window = 0
        winSize = len(cardPoints) - k
        for i in range(winSize):
            window += cardPoints[i]
        
        total = minWin = window
        for i in range(winSize, len(cardPoints)):
            total += cardPoints[i]
            window += cardPoints[i]
            window -= cardPoints[i - winSize]
            minWin = min(minWin, window)
        
        return total - minWin

# @lc code=end

