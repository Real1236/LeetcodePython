# You have a long flowerbed in which some of the plots are planted, and some 
# are not. However, flowers cannot be planted in adjacent plots. 
# 
#  Given an integer array flowerbed containing 0's and 1's, where 0 means empty 
# and 1 means not empty, and an integer n, return if n new flowers can be planted 
# in the flowerbed without violating the no-adjacent-flowers rule. 
# 
#  
#  Example 1: 
#  Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
#  
#  Example 2: 
#  Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= flowerbed.length <= 2 * 10⁴ 
#  flowerbed[i] is 0 or 1. 
#  There are no two adjacent flowers in flowerbed. 
#  0 <= n <= flowerbed.length 
#  
# 
#  Related Topics Array Greedy 👍 3365 👎 701
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i == 0:
                if len(flowerbed) > 1 and flowerbed[1] == 1:
                    continue
                else:
                    flowerbed[0] = 1
                    count += 1
            elif i == len(flowerbed) - 1:
                if len(flowerbed) > 1 and flowerbed[i - 1] == 1:
                    continue
                else:
                    flowerbed[i - 1] = 1
                    count += 1
            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
            if count >= n:
                return True

        return count >= n


# leetcode submit region end(Prohibit modification and deletion)
hashmap = {0: 1}
print(hashmap.get(1, 0))
