#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start


class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        charSet = set()
        for c in s:
            if c in charSet:
                charSet.clear()
                res += 1
            charSet.add(c)
        return res + 1
        
# @lc code=end
solution = Solution()

s = "abacaba"
res = solution.partitionString(s)
print(res)
assert res == 4

s = "ssssss"
res = solution.partitionString(s)
print(res)
assert res == 6