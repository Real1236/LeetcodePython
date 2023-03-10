
#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = Counter(s1)
        window = Counter(s2[:len(s1)])
        
        for i in range(len(s1), len(s2)):
            if letters == window:
                return True
            window[s2[i]] = window.get(s2[i], 0) + 1
            window[s2[i - len(s1)]] -= 1

        return letters == window
        
# @lc code=end

