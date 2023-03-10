#
# @lc app=leetcode id=1888 lang=python3
#
# [1888] Minimum Number of Flips to Make the Binary String Alternating
#

# @lc code=start
class Solution:
    def minFlips(self, s: str) -> int:
        length = len(s)
        s = s + s
        zero, one = "", ""
        for i in range(len(s)):
            zero += "0" if i % 2 == 0 else "1"
            one += "1" if i % 2 == 0 else "0"

        zero_count, one_count = 0, 0
        for i in range(length):
            zero_count += 1 if s[i] != zero[i] else 0
            one_count += 1 if s[i] != one[i] else 0
        
        res = min(zero_count, one_count)
        for i in range(length, len(s)):
            zero_count += 1 if s[i] != zero[i] else 0
            one_count += 1 if s[i] != one[i] else 0
            zero_count -= 1 if s[i - length] != zero[i - length] else 0
            one_count -= 1 if s[i - length] != one[i - length] else 0
            res = min(zero_count, one_count, res)

        return res

        
# @lc code=end
solution = Solution()
print(solution.minFlips("01001001101"))
