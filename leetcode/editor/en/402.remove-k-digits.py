#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        deleted = 0
        for cur in num:
            while deleted < k and stack and stack[-1] > cur:
                deleted += 1
                stack.pop()
            stack.append(cur)
        
        stack = stack[:len(stack) - (k - deleted)]
        res = "".join(stack)
        res = res.lstrip("0")
        return res if res != "" else "0"

# @lc code=end
solution = Solution()

# print(solution.removeKdigits("1234567890", 9))
# print("-----------------------")
# print(solution.removeKdigits("111222", 3))
# print("-----------------------")
print(solution.removeKdigits("11143219", 3))
# print("-----------------------")
# print(solution.removeKdigits("1432219", 3))
# print("-----------------------")
# print(solution.removeKdigits("41939221", 3))
# print("-----------------------")
# print(solution.removeKdigits("10200", 1))
# print("-----------------------")
# print(solution.removeKdigits("10", 2))
# print("-----------------------")
# print(solution.removeKdigits("123111", 2))
