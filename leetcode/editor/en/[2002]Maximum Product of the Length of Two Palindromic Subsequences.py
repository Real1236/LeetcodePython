# Given a string s, find two disjoint palindromic subsequences of s such that 
# the product of their lengths is maximized. The two subsequences are disjoint if 
# they do not both pick a character at the same index. 
# 
#  Return the maximum possible product of the lengths of the two palindromic 
# subsequences. 
# 
#  A subsequence is a string that can be derived from another string by 
# deleting some or no characters without changing the order of the remaining characters. 
# A string is palindromic if it reads the same forward and backward. 
# 
#  
#  Example 1: 
#  
#  
# Input: s = "leetcodecom"
# Output: 9
# Explanation: An optimal solution is to choose "ete" for the 1ˢᵗ subsequence 
# and "cdc" for the 2ⁿᵈ subsequence.
# The product of their lengths is: 3 * 3 = 9.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bb"
# Output: 1
# Explanation: An optimal solution is to choose "b" (the first character) for 
# the 1ˢᵗ subsequence and "b" (the second character) for the 2ⁿᵈ subsequence.
# The product of their lengths is: 1 * 1 = 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "accbcaxxcxx"
# Output: 25
# Explanation: An optimal solution is to choose "accca" for the 1ˢᵗ subsequence 
# and "xxcxx" for the 2ⁿᵈ subsequence.
# The product of their lengths is: 5 * 5 = 25.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= s.length <= 12 
#  s consists of lowercase English letters only. 
#  
# 
#  Related Topics String Dynamic Programming Backtracking Bit Manipulation 
# Bitmask 👍 612 👎 40


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, s: str) -> int:
        palindromes = {}
        for bitmask in range(1, 1 << len(s)):
            subsequence = ""
            for i in range(len(s)):
                if bitmask & (1 << i):
                    subsequence += s[i]
            if subsequence == subsequence[::-1]:
                palindromes[bitmask] = len(subsequence)

        res = 0
        for first in palindromes:
            for second in palindromes:
                if first & second == 0:
                    res = max(res, palindromes[first] * palindromes[second])
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
