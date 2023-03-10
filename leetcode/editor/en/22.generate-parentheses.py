#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def helper(open: int, closed: int):
            if open == closed == n:
                res.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                helper(open + 1, closed)
                stack.pop()
            if closed < open:
                stack.append(")")
                helper(open, closed + 1)
                stack.pop()
                
        helper(0, 0)
        return res

# @lc code=end
solution = Solution()
print(solution.generateParenthesis(3))
