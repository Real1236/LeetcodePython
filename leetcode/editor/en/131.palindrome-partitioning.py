#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(cur: List[str], remaining: str) -> None:
            if not remaining:
                res.append(cur.copy())
                return
            for size in range(1, len(remaining) + 1):
                part = remaining[:size]
                if self.isPalindrome(part):
                    cur.append(part)
                    backtrack(cur, remaining[size:])
                    cur.pop()
        
        backtrack([], s)
        return res
    
    def isPalindrome(self, word: str) -> bool:
        l, r = 0, len(word) - 1
        while l <= r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True

# @lc code=end
solution = Solution()
print(solution.partition("aab"))
