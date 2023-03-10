#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#

# @lc code=start
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        for i in range(k, len(s) + 1):
            codes.add(s[i - k: i])
        return len(codes) == 2 ** k
        
# @lc code=end
solution = Solution()
print(solution.hasAllCodes("00000000010011101", 4))
