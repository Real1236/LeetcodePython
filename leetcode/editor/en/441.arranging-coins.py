#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 1
        while row <= n:
            n -= row
            row += 1
        return row - 1
        
# @lc code=end

