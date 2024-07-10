# Question 2
# Given a string s, determine if it is cool.

# A string s is cool if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:
# Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
# Return true if s is a cool string, otherwise, return false.

# Example: 
# Input: s = "aabcbc" 
# Output: true 
# Explanation: "" -> "abc" -> "aabcbc" Thus, "aabcbc" is valid.

# Example: 
# Input: s = "abccba" 
# Output: false 
# Explanation: It is impossible to get "abccba" using the operation.


class Solution:
    def isCool(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "c":
                if len(stack) < 2 or stack[-1] != "b" or stack[-2] != "a":
                    return False
                stack.pop()
                stack.pop()
            elif c == "a" or c == "b":
                stack.append(c)
            else:
                return False
        
        return not stack

solution = Solution()

# Example 1
print(solution.isCool("aabcbc"))

# Example 2
print(solution.isCool("abccba"))

# Test case 1 - adjacent 'c's
print(solution.isCool("aabcbabcc"))

# Test case 2 - letter that's not 'a' or 'b'
print(solution.isCool("aabcbabccf"))
