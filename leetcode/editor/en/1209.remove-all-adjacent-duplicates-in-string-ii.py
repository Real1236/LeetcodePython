#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        res = ""
        for c, count in stack:
            res += c * count
        return res
        
        
# @lc code=end
solution = Solution()
print(solution.removeDuplicates("deeedbbcccbdaa", 3))
print(solution.removeDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4))
