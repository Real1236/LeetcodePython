#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#

# @lc code=start
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        int_nums = set()
        for num in nums:
            int_nums.add(int(num, 2))
        for i in range(2 ** len(nums[0])):
            if i not in int_nums:
                res = bin(i)[2:]
                return "0" * (len(nums[0]) - len(res)) + res

# @lc code=end
solution = Solution()
print(solution.findDifferentBinaryString(["01","10"]))
