#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#

# @lc code=start
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(index: int, letters: set) -> int:
            word_letters = set()
            for c in arr[index]:
                if c in letters or c in word_letters:
                    return 0
                word_letters.add(c)

            letters = letters | word_letters
            res = len(letters)
            for i in range(index + 1, len(arr)):
                res = max(res, backtrack(i, letters))
            return res
        
        res = 0
        for i in range(0, len(arr)):
            res = max(res, backtrack(i, set()))
        return res

# @lc code=end
solution = Solution()
print(solution.maxLength(["un","iq","ue"]))
print(solution.maxLength(["cha","r","act","ers"]))
print(solution.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
