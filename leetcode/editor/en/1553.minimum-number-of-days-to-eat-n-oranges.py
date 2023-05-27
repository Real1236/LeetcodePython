#
# @lc app=leetcode id=1553 lang=python3
#
# [1553] Minimum Number of Days to Eat N Oranges
#

# @lc code=start
from collections import deque


class Solution:
    def minDays(self, n: int) -> int:
        dp = {0:0, 1:1}
        def dfs(n):
            if n in dp:
                return dp[n]
            one = n % 2 + dfs(n // 2) + 1
            two = n % 3 + dfs(n // 3) + 1
            dp[n] = min(one, two)
            return dp[n]
        return dfs(n)
        
# @lc code=end
solution = Solution()
print(solution.minDays(10))
print(solution.minDays(6))
