#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
from collections import Counter, deque
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        chars = Counter(s)
        chars = [[-count, char] for char, count in chars.items()]
        heapq.heapify(chars)
        
        res = " "
        popped = deque()
        while chars:
            while chars and res[-1] == chars[0][1]:
                popped.append(heapq.heappop(chars))
            if chars and res[-1] != chars[0][1]:
                c = heapq.heappop(chars)
                res += c[1]
                c[0] += 1
                if c[0] != 0:
                    heapq.heappush(chars, c)
            while popped and res[-1] != popped[0][1]:
                c = popped.popleft()
                res += c[1]
                c[0] += 1
                if c[0] != 0:
                    heapq.heappush(chars, c)
        
        return res[1:] if not popped else ""
        
# @lc code=end
solution = Solution()
# print(solution.reorganizeString("aab"))
# print(solution.reorganizeString("aaab"))
print(solution.reorganizeString("vvvlo"))
