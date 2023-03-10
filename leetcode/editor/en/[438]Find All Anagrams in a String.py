# Given two strings s and p, return an array of all the start indices of p's 
# anagrams in s. You may return the answer in any order. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length, p.length <= 3 * 10⁴ 
#  s and p consist of lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Sliding Window 👍 9270 👎 287
from collections import Counter
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram = Counter(p)
        check = Counter(s[:len(p)])
        res = []
        for i in range(len(p), len(s)):
            if check == anagram:
                res.append(i - len(p))
            check[s[i]] = check.get(s[i], 0) + 1
            check[s[i - len(p)]] -= 1
            if check[s[i - len(p)]] == 0:
                check.pop(s[i - len(p)])

        if check == anagram:
            res.append(len(s) - len(p))
        return res


# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
print(solution.findAnagrams("baa", "aa"))
