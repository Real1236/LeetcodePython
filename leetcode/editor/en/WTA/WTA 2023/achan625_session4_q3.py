# There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), 
# some houses that have been painted last summer should not be painted again.

# A neighborhood is a maximal group of continuous houses that are painted with the same color. 
# For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].

# Given an array houses, an m x n matrix cost and an integer target where:
# houses[i]: is the color of the house i, and 0 if the house is not painted yet.
# cost[i][j]: is the cost of paint the house i with the color j + 1.
# Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. 
# If it is not possible, return -1.

# Example:
# Input: houses = [0,0,0,0,0], cost = [[1,10], [10,1], [10,1], [1,10], [5,1]], m = 5, n = 2, target = 3
# Output: 9
# Explanation: Paint houses this way [1,2,2,1,1]. This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}]. 
# Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

# Example: 
# Input: houses = [0,2,1,2,0], cost = [[1,10], [10,1], [10,1], [1,10], [5,1]], m = 5, n = 2, target = 3
# Output: 11
# Explanation: Some houses are already painted, so paint the houses this way [2,2,1,2,2]
# This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
# Cost of paint the first and last house (10 + 1) = 11.


from collections import deque
from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = {}

        def dfs(i: int, hoods: int, colour: int) -> int:
            if i >= len(houses) or hoods < 0 or m - i < hoods:
                return float('inf') if hoods != 0 or i < len(houses) else 0

            key = (i, hoods, colour)
            if key not in dp:
                if houses[i] == 0:
                    price = float('inf')
                    for paint in range(1, n + 1):
                        price = min(price, dfs(i + 1, hoods - (paint != colour), paint) + cost[i][paint - 1])
                    dp[key] = price
                else:
                    dp[key] = dfs(i + 1, hoods - (houses[i] != colour), houses[i])

            return dp[key]
        
        res = dfs(0, target, -1)
        return res if res < float('inf') else -1

solution = Solution()

# Example 1
print(solution.minCost([0,0,0,0,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3))

# Example 2
print(solution.minCost([0,2,1,2,0], [[1,10], [10,1], [10,1], [1,10], [5,1]], 5, 2, 3))

# Test Case 1
print(solution.minCost([3,1,2,3], [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], 4, 3, 3))

# Test Case 2
print(solution.minCost([1,0,1,2], [[2,0,1,1], [2,1,1,1], [2,0,1,1], [2,1,1,1]], 4, 4, 2))

