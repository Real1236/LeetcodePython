#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
from collections import defaultdict
import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adjList = defaultdict(list)
        for i, edge in enumerate(edges):
            a, b, prob = edge[0], edge[1], succProb[i]
            adjList[a].append((prob, b))
            adjList[b].append((prob, a))
        
        visit = set()
        frontier = [(-1, start)]
        while frontier:
            curProb, cur = heapq.heappop(frontier)
            curProb *= -1
            visit.add(cur)
            if cur == end:
                return curProb
            neighbours = adjList[cur]
            for prob, n in neighbours:
                if n in visit:
                    continue
                heapq.heappush(frontier, (-prob * curProb, n))
        return 0


# @lc code=end
solution = Solution()
print(solution.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))
print(solution.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2))
print(solution.maxProbability(3, [[0,1]], [0.5], 0, 2))
