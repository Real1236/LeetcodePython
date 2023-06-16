#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        netChange = 0
        runningChange = 0
        for i in range(len(gas)):
            change = gas[i] - cost[i]
            netChange += change
            if runningChange == 0 and runningChange + change >= 0:
                start = i
            runningChange = max(runningChange + change, 0)
        return start if netChange >= 0 else -1

# @lc code=end
solution = Solution()
print(solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print(solution.canCompleteCircuit([2,3,4], [3,4,3]))
print(solution.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))
print(solution.canCompleteCircuit([5,8,2,8], [6,5,6,6]))
print(solution.canCompleteCircuit([5,5,1,3,4], [8,1,7,1,1]))
print(solution.canCompleteCircuit([4,5,5,1,3], [1,8,1,7,1]))
