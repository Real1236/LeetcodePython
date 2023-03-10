# Given a list of non-negative integers nums, arrange them such that they form 
# the largest number and return it. 
# 
#  Since the result may be very large, so you need to return a string instead 
# of an integer. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,2]
# Output: "210"
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics String Greedy Sorting 👍 6149 👎 511
from collections import deque
from functools import cmp_to_key
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string_nums = [str(num) for num in nums]

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        string_nums.sort(key=cmp_to_key(compare))
        res = "".join(string_nums).lstrip("0")

        if res:
            return res
        return "0"

        
# leetcode submit region end(Prohibit modification and deletion)
a = "1"
b = "9"
print(a < b)
print(a == b)
print(a > b)
