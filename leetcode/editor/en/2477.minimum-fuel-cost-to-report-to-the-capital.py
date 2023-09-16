#
# @lc app=leetcode id=2477 lang=python3
#
# [2477] Minimum Fuel Cost to Report to the Capital
#

# @lc code=start
from collections import defaultdict
import math
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adjList = defaultdict(set)
        for a, b in roads:
            adjList[a].add(b)
            adjList[b].add(a)

        fuel = 0
        def dfs(current, prev):
            people = 1
            for n in adjList[current]:
                if n == prev:
                    continue
                people += dfs(n, current)
            nonlocal fuel
            fuel += int(math.ceil(people / seats)) if current else 0
            return people

        dfs(0, None)
        return fuel

# @lc code=end
solution = Solution()
print(solution.minimumFuelCost([[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], 2))
