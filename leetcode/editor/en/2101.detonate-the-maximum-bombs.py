#
# @lc app=leetcode id=2101 lang=python3
#
# [2101] Detonate the Maximum Bombs
#

# @lc code=start
from math import sqrt
from collections import defaultdict
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

                if distance <= r1:
                    adjList[i].append(j)
                if distance <= r2:
                    adjList[j].append(i)

        def dfs(bomb: int, adjList: dict, visited: set) -> int:
            visited.add(bomb)
            neighbours = adjList[bomb]
            for n in neighbours:
                if n in visited:
                    continue
                dfs(n, adjList, visited)
            return len(visited)
        
        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i, adjList, set()))
        return res

# @lc code=end
solution = Solution()

bombs = [[2,1,3],[6,1,4]]
print(solution.maximumDetonation(bombs))