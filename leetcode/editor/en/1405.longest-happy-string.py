#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#

# @lc code=start
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        letters = [[-a, "a"], [-b, "b"], [-c, "c"]]
        heapq.heapify(letters)
        res = "  "
        prev = None
        while letters:
            cur = heapq.heappop(letters)
            if cur[0] < 0:
                res += cur[1]
                cur[0] += 1
                heapq.heappush(letters, cur)
            if prev:
                heapq.heappush(letters, prev)
                prev = None
            if letters and letters[0][1] == res[-1] == res[-2]:
                prev = heapq.heappop(letters)
        return res[2:]
        
# @lc code=end
solution = Solution()
print(solution.longestDiverseString(7,1,0))
