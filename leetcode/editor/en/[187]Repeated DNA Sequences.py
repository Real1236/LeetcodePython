# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 
# 'C', 'G', and 'T'. 
# 
#  
#  For example, "ACGAATTCCG" is a DNA sequence. 
#  
# 
#  When studying DNA, it is useful to identify repeated sequences within the 
# DNA. 
# 
#  Given a string s that represents a DNA sequence, return all the 10-letter-
# long sequences (substrings) that occur more than once in a DNA molecule. You may 
# return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
#  
#  Example 2: 
#  Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] is either 'A', 'C', 'G', or 'T'. 
#  
# 
#  Related Topics Hash Table String Bit Manipulation Sliding Window Rolling 
# Hash Hash Function 👍 2564 👎 459
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        substrings, res = set(), set()
        for i in range(9, len(s)):
            substring = s[i - 9: i + 1]
            if substring in substrings:
                res.add(substring)
            else:
                substrings.add(substring)
        return list(res)


# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
