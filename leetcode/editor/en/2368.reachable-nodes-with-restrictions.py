#
# @lc app=leetcode id=2368 lang=python3
#
# [2368] Reachable Nodes With Restrictions
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        q = deque([0])
        visited = set()
        restrictedSet = set(restricted)
        while q:
            levelSize = len(q)
            for _ in range(levelSize):
                node = q.popleft()
                if node in restrictedSet or node in visited:
                    continue
                visited.add(node)

                neighbours = adjList[node]
                for n in neighbours:
                    q.append(n)

        return len(visited)

# @lc code=end
solution = Solution()

n = 7
edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
restricted = [4,5]
print(solution.reachableNodes(n, edges, restricted))