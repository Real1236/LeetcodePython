#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        window = {}

        have, need = 0, len(t_count)
        res = s
        left = 0
        found = False
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in t_count and window[s[right]] == t_count[s[right]]:
                have += 1
            
            while have == need:
                found = True
                if right - left + 1 < len(res):
                    res = s[left : right + 1]
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        
        return res if found else ""

        
# @lc code=end
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))
