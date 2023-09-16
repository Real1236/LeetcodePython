#
# @lc app=leetcode id=1129 lang=python3
#
# [1129] Shortest Path with Alternating Colors
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redAdjList = {}
        for a, b in redEdges:
            if a not in redAdjList:
                redAdjList[a] = set()
            redAdjList[a].add(b)

        blueAdjList = {}
        for a, b in blueEdges:
            if a not in blueAdjList:
                blueAdjList[a] = set()
            blueAdjList[a].add(b)
            
        visited = set([(0,"blue"), (0,"red")])
        q = deque([(0,"blue"), (0,"red")])
        level = 0
        res = [float('inf') for _ in range(n)]
        while q:
            levelSize = len(q)
            for _ in range(levelSize):
                node, prevColour = q.popleft()
                res[node] = min(res[node], level)
                if prevColour == "red" and node in blueAdjList:
                    nextNodes = blueAdjList[node]
                    for next in nextNodes:
                        if (next, "blue") not in visited:
                            visited.add((next, "blue"))
                            q.append((next, "blue"))
                elif prevColour == "blue" and node in redAdjList:
                    nextNodes = redAdjList[node]
                    for next in nextNodes:
                        if (next, "red") not in visited:
                            visited.add((next, "red"))
                            q.append((next, "red"))
            level += 1
        
        for i, value in enumerate(res):
            if value == float('inf'):
                res[i] = -1

        return res

# @lc code=end
solution = Solution()
print(solution.shortestAlternatingPaths(3, [[0,1],[1,2]], []))
print(solution.shortestAlternatingPaths(3, [[0,1]], [[2,1]]))
