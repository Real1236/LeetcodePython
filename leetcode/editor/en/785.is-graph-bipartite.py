#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        blue, green = set(), set()

        def bfs(node):
            if node in blue or node in green:
                return True

            q = deque([node])
            isBlue = True
            while q:
                levelSize = len(q)
                for i in range(levelSize):
                    cur = q.popleft()
                    for nei in graph[cur]:
                        if isBlue and nei in blue:
                            return False
                        if not isBlue and nei in green:
                            return False

                        if nei not in blue and nei not in green:
                            if isBlue:
                                green.add(nei)
                            else:
                                blue.add(nei)
                            q.append(nei)
                
                isBlue = not isBlue

            return True
        
        for node in range(len(graph)):
            if not bfs(node):
                return False

        return True
        
# @lc code=end
solution = Solution()
print(solution.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])) # False
print(solution.isBipartite([[3,4,6],[3,6],[3,6],[0,1,2,5],[0,7,8],[3],[0,1,2,7],[4,6],[4],[]])) # True
