# Given a pattern and a string s, find if s follows the same pattern. 
# 
#  Here follow means a full match, such that there is a bijection between a 
# letter in pattern and a non-empty word in s. 
# 
#  
#  Example 1: 
# 
#  
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= pattern.length <= 300 
#  pattern contains only lower-case English letters. 
#  1 <= s.length <= 3000 
#  s contains only lowercase English letters and spaces ' '. 
#  s does not contain any leading or trailing spaces. 
#  All the words in s are separated by a single space. 
#  
# 
#  Related Topics Hash Table String 👍 4302 👎 486


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        letter_to_word = {}
        word_to_letter = {}
        for letter, word in zip(pattern, words):
            if letter in letter_to_word and word != letter_to_word[letter]:
                return False
            if word in word_to_letter and letter != word_to_letter[word]:
                return False
            letter_to_word[letter] = word
            word_to_letter[word] = letter

        return True

        
# leetcode submit region end(Prohibit modification and deletion)
