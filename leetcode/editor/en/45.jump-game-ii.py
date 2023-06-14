#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque([(0,0)])
        jumps = 0
        while q:
            for _ in range(len(q)):
                left, right = q.popleft()
                if right >= len(nums) - 1:
                    return jumps
                maxJump = 0
                for i in range(left, right + 1):
                    maxJump = max(maxJump, i + nums[i])
                q.append((right + 1, maxJump))
            jumps += 1

# @lc code=end
solution = Solution()
print(solution.jump([2,3,1,1,4]))
print(solution.jump([2,3,0,1,4]))
print(solution.jump([0]))
