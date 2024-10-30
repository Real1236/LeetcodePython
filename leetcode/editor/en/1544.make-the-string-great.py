#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        stack = [s[0]]
        for i in range(1, len(s)):
            if not stack or abs(ord(stack[-1]) - ord(s[i])) != 32:
                stack.append(s[i])
            else:
                stack.pop()
        return "".join(stack)

# @lc code=end
solution = Solution()

s = "leEeetcode"    # -> "leetcode"
print(solution.makeGood(s))

s = "abBAcC"    # -> ""
print(solution.makeGood(s))

s = "NAanorRoOrROwnTNW" # -> "wnTNW"
print(solution.makeGood(s))
