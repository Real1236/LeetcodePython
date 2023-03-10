#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        if not stack:
            return 0
        res = stack[0]
        for i in range(1, len(stack)):
            res = max(res, stack[i] - stack[i - 1])
        return max(len(s) - stack[-1], res)
        
# @lc code=end

