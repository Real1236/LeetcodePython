#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checkCapacity(capacity):
            counter = 1
            runTotal = 0
            for weight in weights:
                if runTotal + weight > capacity:
                    runTotal = weight
                    counter += 1
                    if counter > days or weight > capacity:
                        return "Increase Capacity"
                else:
                    runTotal += weight
            
            return "Decrease Capacity"

        low, high = max(weights), sum(weights)
        while low < high:
            capacity = (low + high) // 2
            if checkCapacity(capacity) == "Increase Capacity":
                low = capacity + 1
            else:
                high = capacity

        return (low + high) // 2

        
# @lc code=end
solution = Solution()

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(solution.shipWithinDays(weights, days)) # 15

weights = [3,2,2,4,1,4]
days = 3
print(solution.shipWithinDays(weights, days)) # 6

weights = [1,2,3,1,1]
days = 4
print(solution.shipWithinDays(weights, days)) # 3