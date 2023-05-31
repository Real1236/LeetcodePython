#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
from collections import defaultdict, deque
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0

        nList = defaultdict(list)
        for a in points:
            for b in points:
                nList[(a[0], a[1])].append((abs(a[0] - b[0]) + abs(a[1] - b[1]), (b[0], b[1])))

        res = 0
        q = deque([(points[0][0], points[0][1])])
        visited = set([(points[0][0], points[0][1])])
        frontier = []
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                neighbours = nList[cur]
                for n in neighbours:
                    if n[1] not in visited:
                        heapq.heappush(frontier, n)
                distance, next = heapq.heappop(frontier)
                while next in visited:
                    distance, next = heapq.heappop(frontier)
                if next not in visited:
                    res += distance
                    visited.add(next)
                    q.append(next)
                    if len(visited) == len(points):
                        return res


# @lc code=end
solution = Solution()
print(solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
