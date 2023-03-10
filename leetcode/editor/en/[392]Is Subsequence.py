# Given two strings s and t, return true if s is a subsequence of t, or false 
# otherwise. 
# 
#  A subsequence of a string is a new string that is formed from the original 
# string by deleting some (can be none) of the characters without disturbing the 
# relative positions of the remaining characters. (i.e., "ace" is a subsequence of 
# "abcde" while "aec" is not). 
# 
#  
#  Example 1: 
#  Input: s = "abc", t = "ahbgdc"
# Output: true
#  
#  Example 2: 
#  Input: s = "axc", t = "ahbgdc"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 100 
#  0 <= t.length <= 10⁴ 
#  s and t consist only of lowercase English letters. 
#  
# 
#  
# Follow up: Suppose there are lots of incoming 
# s, say 
# s1, s2, ..., sk where 
# k >= 10⁹, and you want to check one by one to see if 
# t has its subsequence. In this scenario, how would you change your code?
# 
#  Related Topics Two Pointers String Dynamic Programming 👍 6385 👎 358


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        for t_index in range(len(t)):
            if s_index == len(s):
                return True
            if s[s_index] == t[t_index]:
                s_index += 1
        return s_index == len(s)
        
# leetcode submit region end(Prohibit modification and deletion)

