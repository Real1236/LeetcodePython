#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
from collections import Counter


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        deleted = False
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if s[left:right] == s[left:right][::-1] or s[left + 1: right + 1] == s[left + 1: right + 1][::-1]:
                    return True
                return False
        return True
        
# @lc code=end
solution = Solution()
#                         0         1         2         3         4         5         6         7         8         9         10
#                         01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
solution.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")
