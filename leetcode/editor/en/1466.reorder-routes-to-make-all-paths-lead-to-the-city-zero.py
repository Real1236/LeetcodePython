#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = { (a,b) for a, b in connections }
        neighbours = { city:set() for city in range(n) }
        for a, b in edges:
            neighbours[a].add(b)
            neighbours[b].add(a)

        def dfs(city):
            res = 0
            for neighbour in neighbours[city]:
                if (city, neighbour) in edges:
                    res += 1
                neighbours[neighbour].remove(city)
                res += dfs(neighbour)
            return res
                  
        return dfs(0)
        
# @lc code=end
solution = Solution()
print(solution.minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]]))
