#
# @lc app=leetcode id=1871 lang=python3
#
# [1871] Jump Game VII
#

# @lc code=start
from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
        
        q = deque([0])
        furthest = 0
        while q:
            size = len(q)
            for _ in range(size):
                index = q.popleft()
                start = max(index + minJump, furthest + 1)
                for nextIndex in range(start, index + maxJump + 1):
                    if nextIndex >= len(s) or s[nextIndex] == "1":
                        continue
                    if nextIndex == len(s) - 1:
                        return True
                    q.append(nextIndex)
                furthest = index + maxJump
        return False
        
# @lc code=end
solution = Solution()
print(solution.canReach("011010", 2, 3))
print(solution.canReach("01101110", 2, 3))