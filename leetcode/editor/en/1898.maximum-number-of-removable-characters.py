#
# @lc app=leetcode id=1898 lang=python3
#
# [1898] Maximum Number of Removable Characters
#

# @lc code=start
from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubsequence(removed: set):
            p_index = 0
            for i, c in enumerate(s):
                if i not in removed and c == p[p_index]:
                    if p_index == len(p) - 1:
                        return True
                    p_index += 1
            return False
        
        left, right = 0, len(removable) - 1
        res = 0
        while left <= right:
            middle = (left + right) // 2
            removed = set(removable[:middle + 1])
            if isSubsequence(removed):
                left = middle + 1
                res = middle + 1
            else:
                right = middle - 1

        return res
        
# @lc code=end
solution = Solution()
print(solution.maximumRemovals("abcacb", "ab", [3,1,0]))
