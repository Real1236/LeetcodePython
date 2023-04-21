#
# @lc app=leetcode id=1849 lang=python3
#
# [1849] Splitting a String Into Descending Consecutive Values
#

# @lc code=start
class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(prev: int, index: int) -> bool:
            if index == len(s) and prev != int(s):
                return True
            for i in range(index + 1, len(s) + 1):
                sub = int(s[index:i])
                if sub == prev - 1 or prev == float('inf'):
                    if backtrack(sub, i):
                        return True
            return False
        
        return backtrack(float('inf'), 0)
        
# @lc code=end
solution = Solution()
print(solution.splitString("1234"))
print(solution.splitString("050043"))
