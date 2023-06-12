#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        curSize = maxSize = 1
        prev = arr[0]
        sign = "="
        for i in range(1, len(arr)):
            if prev == arr[i]:
                curSize = 1
            elif prev > arr[i]:
                if sign == ">":
                    curSize = 2
                else:
                    curSize += 1
                    maxSize = max(maxSize, curSize)
                    sign = ">"
            else:
                if sign == "<":
                    curSize = 2
                else:
                    curSize += 1
                    maxSize = max(maxSize, curSize)
                    sign = "<"
            prev = arr[i]
        return maxSize

# @lc code=end
solution = Solution()
print(solution.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
print(solution.maxTurbulenceSize([4,8,12,16]))
print(solution.maxTurbulenceSize([100]))
