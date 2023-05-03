#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
from collections import Counter
import heapq
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)

        if sum(nums) % k:
            return False
        target = sum(nums) / k
        visited = set()

        def backtrack(index: int, k: int, sum: int) -> bool:
            if k == 0:
                return True
            if sum == target:
                return backtrack(0, k - 1, 0)

            for i in range(index, len(nums)):
                if i > 0 and (i - 1) not in visited and nums[i] == nums[i - 1]:
                    continue
                if i in visited or sum + nums[i] > target:
                    continue
                visited.add(i)
                if backtrack(i + 1, k, sum + nums[i]):
                    return True
                visited.remove(i)

            return False
        
        return backtrack(0, k, 0)

# @lc code=end
solution = Solution()
print(solution.canPartitionKSubsets([4,3,2,3,5,2,1], 4))
