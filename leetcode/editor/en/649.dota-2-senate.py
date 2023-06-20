#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#

# @lc code=start
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQ, dQ = deque(), deque()
        for i, p in enumerate(senate):
            if p == "R":
                rQ.append(i)
            else:
                dQ.append(i)
        
        while rQ and dQ:
            if rQ[0] < dQ[0]:
                dQ.popleft()
                rQ.append(rQ.popleft() + len(senate))
            else:
                rQ.popleft()
                dQ.append(dQ.popleft() + len(senate))
        
        return "Radiant" if rQ else "Dire"
        
# @lc code=end
solution = Solution()
print(solution.predictPartyVictory("RD"))
print(solution.predictPartyVictory("RDD"))
print(solution.predictPartyVictory("RRDRD"))
