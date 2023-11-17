#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visited = set()
        def dfs(node: int) -> List[int]:
            visited.add(node)
            totalTime = foundApple = 0

            neighbours = adjList[node]
            for n in neighbours:
                if n in visited:
                    continue
                time, tempFoundApple = dfs(n)
                if tempFoundApple:
                    foundApple = 1
                    totalTime += time
            
            return [totalTime + 2, 1] if foundApple or hasApple[node] else [0, 0]

        return max(0, dfs(0)[0] - 2)
        
# @lc code=end
solution = Solution()
# print(solution.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]))
# print(solution.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False]))
# print(solution.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False]))
print(solution.minTime(5, [[0,1],[0,2],[1,3],[0,4]], [False,False,False,True,False]))
