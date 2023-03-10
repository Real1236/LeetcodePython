# Given two strings s and t, return true if t is an anagram of s, and false othe
# rwise. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a differe
# nt word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: s = "anagram", t = "nagaram"
# Output: true
#  Example 2: 
#  Input: s = "rat", t = "car"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 5 * 104 
#  s and t consist of lowercase English letters. 
#  
# 
#  
#  Follow up: What if the inputs contain Unicode characters? How would you adapt
#  your solution to such a case? 
#  Related Topics Hash Table String Sorting 
#  👍 7637 👎 249


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetters = {}
        for letter in s:
            sLetters[letter] = sLetters.get(letter, 0) + 1

        for letter in t:
            if letter not in sLetters:
                return False
            if sLetters[letter] == 1:
                sLetters.pop(letter)
            else:
                sLetters[letter] = sLetters[letter] - 1

        if len(sLetters) > 0:
            return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
