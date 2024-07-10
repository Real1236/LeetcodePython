# Question 2 - Binary Search
# Given the positions of houses and heaters on a horizontal line, return the minimum radius required for the heaters to cover all the houses. The warm radius will be the same for all heaters.

# Example 1:

# Input:
# houses = [1, 2, 3]
# heaters = [2]
# Output:
# 1
# Explanation:
# The only heater was placed in position 2, and with a radius of 1, all the houses can be warmed.

# Example 2:

# Input:
# houses = [1, 2, 3, 4]
# heaters = [1, 4]
# Output:
# 1
# Explanation:
# The two heaters were placed at positions 1 and 4. With a radius of 1, all the houses can be warmed.

# Example 3:

# Input:
# houses = [1, 5]
# heaters = [2]
# Output:
# 3
# Explanation:
# To cover the house at position 5, which is 3 units away from the heater at position 2, the minimum radius required is 3 to ensure all houses are within the heater's warm range.

from bisect import bisect_left
from typing import List


def min_radius(houses: List[int], heaters: List[int]) -> int:
    def all_houses_covered(radius: int) -> bool:
        for house in houses:
            pos = bisect_left(heaters, house - radius)
            if pos == len(heaters):
                return False
            if heaters[pos] > house + radius:
                return False
        return True
    
    houses.sort()
    heaters.sort()

    res = float('inf')
    low, high = 0, max(houses[-1], heaters[-1]) - min(houses[0], heaters[0])
    while low <= high:
        radius = (low + high) // 2
        if all_houses_covered(radius):
            res = min(res, radius)
            high = radius - 1
        else:
            low = radius + 1
    return res

houses = [1, 2, 3]
heaters = [2]
print(min_radius(houses, heaters))

houses = [1, 2, 3, 4]
heaters = [1, 4]
print(min_radius(houses, heaters))

houses = [1, 5]
heaters = [2]
print(min_radius(houses, heaters))

houses = [1, 5]
heaters = [10]
print(min_radius(houses, heaters))

houses = [1]
heaters = [1, 2, 3, 4]
print(min_radius(houses, heaters))

# Did a binary search on the radius. If there is a valid radius, we'll lower the upper bound, otherwise we'll increase the lower bound. Binary search is O(logn) and checking for a valid radius is O(n) so TC is O(nlogn)
