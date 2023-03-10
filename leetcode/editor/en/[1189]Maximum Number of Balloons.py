# Given a string text, you want to use the characters of text to form as many 
# instances of the word "balloon" as possible. 
# 
#  You can use each character in text at most once. Return the maximum number 
# of instances that can be formed. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: text = "nlaebolko"
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: text = "loonbalxballpoon"
# Output: 2
#  
# 
#  Example 3: 
# 
#  
# Input: text = "leetcode"
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= text.length <= 10⁴ 
#  text consists of lower case English letters only. 
#  
# 
#  Related Topics Hash Table String Counting 👍 1248 👎 76
from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = Counter(text)
        balloon = Counter("balloon")

        print(letters["b"])
        res = 10000
        for letter in balloon:
            res = min(res, letters[letter] // balloon[letter])
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
solution.maxNumberOfBalloons("cde")
