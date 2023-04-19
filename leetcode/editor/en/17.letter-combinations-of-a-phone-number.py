#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        tel = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        def backtrack(comb: str, index: int) -> None:
            if index == len(digits):
                res.append(comb)
                return
            for letter in tel[digits[index]]:
                backtrack(comb + letter, index + 1)
        
        if digits:
            backtrack("", 0)
        return res

# @lc code=end
solution = Solution()
print(solution.letterCombinations("23"))
