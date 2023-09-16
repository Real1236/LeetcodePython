#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Build adjacency list --> key: city 1, value: sets of (city 2, distance)
        adjList = defaultdict(set)
        for a, b, distance in roads:
            adjList[a].add((b, distance))
            adjList[b].add((a, distance))

        # Keep track of paths already taken (a, b, distance)
        visited = set()

        # DFS
        def dfs(current, res):
            for next, distance in adjList[current]:
                res = min(res, distance)
                if next in visited:
                    continue
                visited.add(next)
                res = dfs(next, res)

            return res
        
        return dfs(1, float('inf'))

# @lc code=end
solution = Solution()
print(solution.minScore(4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]))
print(solution.minScore(4, [[1,2,2],[1,3,4],[3,4,7]]))
print(solution.minScore(3, [[3,2,1],[1,3,3]]))
