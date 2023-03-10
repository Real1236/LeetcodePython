#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        
        i, j = 0, 0
        res = ""
        while j < len(stack):
            if i != stack[j]:
                res += s[i]
            else:
                j += 1
            i += 1
        return res + s[i:]

        
# @lc code=end
solution = Solution()
print(solution.minRemoveToMakeValid("lee(t(c)o)de)"))
print(solution.minRemoveToMakeValid("a)b(c)d"))
print(solution.minRemoveToMakeValid("))(("))
