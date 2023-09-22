#
# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = set()
        for f, t in edges:
            incoming.add(t)

        res = []
        for vertex in range(n):
            if vertex not in incoming:
                res.append(vertex)
        return res

# @lc code=end
solution = Solution()
print(solution.findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]]))
print(solution.findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]]))
