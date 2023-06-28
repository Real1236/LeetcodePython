#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
from collections import deque


class Solution:
    def checkValidString(self, s: str) -> bool:
        left, right = 0, 0
        for c in s:
            if c == "(":
                left += 1
                right += 1
            elif c == ")":
                left -= 1
                right -= 1
            else:
                left -= 1
                right += 1
            if right < 0:
                return False
            left = max(left, 0)
        return left == 0

        
# @lc code=end
solution = Solution()
print(solution.checkValidString("(((((*)))**"))
