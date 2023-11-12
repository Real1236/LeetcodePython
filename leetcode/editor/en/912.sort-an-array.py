#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
from collections import deque
from typing import List

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        middleIndex = len(nums) // 2
        a = deque(self.sortArray(nums[:middleIndex]))
        b = deque(self.sortArray(nums[middleIndex:]))

        res = []
        while a and b:
            if a[0] <= b[0]:
                res.append(a.popleft())
            else:
                res.append(b.popleft())
        
        if a:
            res += list(a)
        if b:
            res += list(b)

        return res
        
# @lc code=end
solution = Solution()
print(solution.sortArray([5,2,3,1]))
