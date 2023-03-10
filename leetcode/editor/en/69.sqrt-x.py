#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            middle = int(left + (right - left) / 2)
            square = middle * middle
            if square == x:
                return middle
            if square < x:
                left = middle + 1
            else:
                right = middle - 1
        
        return right
        
# @lc code=end

