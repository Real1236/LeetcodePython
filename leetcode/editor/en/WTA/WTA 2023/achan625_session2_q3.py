# Question 3
# Given two strings s and t, return an array of all the start indices of t's anagrams in s. You may return the answer in any order. 
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 

# Example:
# Input: 
# s = "cbaebabacd"
# t = "abc"
# Output:
# [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc". 
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example:
# Input: 
# s = "abab"
# t = "ab"
# Output:
# [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab". 
# The substring with start index = 1 is "ba", which is an anagram of "ab". 
# The substring with start index = 2 is "ab", which is an anagram of "ab".


from typing import List


class Solution:
        def anagramIndices(self, s: str, t: str) -> List[int]:
            def getLetterIndex(c: str) -> int:
                return ord(c) - ord('a')

            if len(t) > len(s):
                return []
            
            tLetters = [0 for _ in range(26)]
            for c in t:
                tLetters[getLetterIndex(c)] += 1
                
            res = []
            sLetters = [0 for _ in range(26)]
            for i in range(len(t) - 1):
                sLetters[getLetterIndex(s[i])] += 1

            for i in range(len(s) - len(t) + 1):
                sLetters[getLetterIndex(s[i + len(t) - 1])] += 1
                if sLetters == tLetters:
                    res.append(i)
                sLetters[getLetterIndex(s[i])] -= 1

            return res

solution = Solution()

# Example 1
print(solution.anagramIndices("cbaebabacd", "abc"))

# Example 2
print(solution.anagramIndices("abab", "ab"))

# Test case 1 - adjacent length of 't' is greater than length of 's'
print(solution.anagramIndices("aa", "aaa"))

# Test case 2
print(solution.anagramIndices("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"))