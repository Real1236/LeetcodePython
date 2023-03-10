#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")":"(", "}":"{", "]":"["}
        stack = []
        for c in s:
            if c in bracket_map:
                if not stack:
                    return False
                if stack[-1] == bracket_map[c]:
                    stack.pop()
            else:
                stack.append(c)
        return not stack

        
# @lc code=end
solution = Solution()
print(solution.isValid("()"))
