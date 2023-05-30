#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import defaultdict
import heapq
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = defaultdict(list)
        for a, b in tickets:
            flights[a].append(b)

        res = []
        def dfs(prev, city):
            res.append(city)
            if not flights:
                return res
            numCities = len(flights[city])
            heapq.heapify(flights[city])
            for _ in range(numCities):
                destination = heapq.heappop(flights[city])
                if not flights[city]:
                    flights.pop(city)
                if dfs(city, destination):
                    return res
            if not flights[city]:
                flights.pop(city)
            res.pop()
            flights[prev].append(city)
        
        return dfs("", "JFK")
        
# @lc code=end
solution = Solution()
print(solution.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(solution.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
