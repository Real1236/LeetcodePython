#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from typing import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left = 0
        max_frequency = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(max_frequency, count[s[right]])

            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res

# @lc code=end
solution = Solution()
print(solution.characterReplacement("ABAB", 2))
print(solution.characterReplacement("AABABBA", 1))