#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        place = {}
        for i, c in enumerate(order):
            place[c] = i + 1
        
        for i in range(len(words) - 1):
            cur = words[i]
            next = words[i + 1]
            for j, c in enumerate(cur):
                if j >= len(next):
                    return False
                if c == next[j]:
                    continue
                if place[c] > place[next[j]]:
                    return False
                else:
                    break
        return True
        
# @lc code=end

