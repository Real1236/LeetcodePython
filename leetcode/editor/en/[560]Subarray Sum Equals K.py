# Given an array of integers nums and an integer k, return the total number of 
# subarrays whose sum equals to k. 
# 
#  A subarray is a contiguous non-empty sequence of elements within an array. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,1], k = 2
# Output: 2
#  
#  Example 2: 
#  Input: nums = [1,2,3], k = 3
# Output: 2
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -1000 <= nums[i] <= 1000 
#  -10⁷ <= k <= 10⁷ 
#  
# 
#  Related Topics Array Hash Table Prefix Sum 👍 16423 👎 483
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        total = 0
        res = 0
        for num in nums:
            total += num
            res += prefix_sums.get(total - k, 0)
            prefix_sums[total] = prefix_sums.get(total, 0) + 1
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
