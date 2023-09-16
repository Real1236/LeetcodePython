#
# @lc app=leetcode id=2359 lang=python3
#
# [2359] Find Closest Node to Given Two Nodes
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start, distances):
            visited = set()
            q = deque()
            q.append(start)
            level = 0
            while q:
                levelSize = len(q)
                for _ in range(levelSize):
                    current = q.popleft()
                    distances[current] = level
                    visited.add(current)

                    if not edges[current] in visited and edges[current] != -1:
                        q.append(edges[current])
                level += 1

        n1Distances, n2Distances = {}, {}
        bfs(node1, n1Distances)
        bfs(node2, n2Distances)
        
        res, minDistance = -1, float('inf')
        for node in range(len(edges)):
            if node in n1Distances and node in n2Distances:
                distance = max(n1Distances[node], n2Distances[node])
                if distance < minDistance:
                    res = node
                    minDistance = distance
        return res

# @lc code=end
solution = Solution()
print(solution.closestMeetingNode([2,2,3,-1], 0, 1))
print(solution.closestMeetingNode([1,2,-1], 0, 2))
