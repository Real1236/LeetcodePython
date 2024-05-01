#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # Find longest sequence of zeroes
        longest = 0
        count = 0
        for num in nums:
            if not num:
                count += 1
                if count > longest:
                    longest = count
            else:
                count = 0

        # Create mapping num of zeroes to occurrences of subarrays
        # 1 -> 1
        # 2 -> 3 = 1 + 2 = map[1] + 2
        # 3 -> 6 = 1 + 2 + 3 = map[2] + 3
        # 4 -> 10 = 1 + 2 + 3 + 4 = map[3] + 4
        map = [0]
        for i in range(1, longest + 1):
            map.append(map[i - 1] + i)

        # Loop through nums and add occurrences
        res = 0
        count = 0
        for num in nums:
            if not num:
                count += 1
                continue
            
            res += map[count]
            count = 0
            
        res += map[count]
        count = 0
        
        return res

# @lc code=end

