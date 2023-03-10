# You are given n rectangles represented by a 0-indexed 2D integer array 
# rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of 
# the iᵗʰ rectangle. 
# 
#  Two rectangles i and j (i < j) are considered interchangeable if they have 
# the same width-to-height ratio. More formally, two rectangles are interchangeable 
# if widthi/heighti == widthj/heightj (using decimal division, not integer 
# division). 
# 
#  Return the number of pairs of interchangeable rectangles in rectangles. 
# 
#  
#  Example 1: 
# 
#  
# Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
# Output: 6
# Explanation: The following are the interchangeable pairs of rectangles by 
# index (0-indexed):
# - Rectangle 0 with rectangle 1: 4/8 == 3/6.
# - Rectangle 0 with rectangle 2: 4/8 == 10/20.
# - Rectangle 0 with rectangle 3: 4/8 == 15/30.
# - Rectangle 1 with rectangle 2: 3/6 == 10/20.
# - Rectangle 1 with rectangle 3: 3/6 == 15/30.
# - Rectangle 2 with rectangle 3: 10/20 == 15/30.
#  
# 
#  Example 2: 
# 
#  
# Input: rectangles = [[4,5],[7,8]]
# Output: 0
# Explanation: There are no interchangeable pairs of rectangles.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == rectangles.length 
#  1 <= n <= 10⁵ 
#  rectangles[i].length == 2 
#  1 <= widthi, heighti <= 10⁵ 
#  
# 
#  Related Topics Array Hash Table Math Counting Number Theory 👍 309 👎 26
from math import factorial
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = {}
        max_count = 0
        for rectangle in rectangles:
            ratios[rectangle[0]/rectangle[1]] = ratios.get(rectangle[0]/rectangle[1], 0) + 1
            max_count = max(max_count, ratios[rectangle[0]/rectangle[1]])

        triangle_sequence = [1]
        for i in range(1, max_count - 1):
            triangle_sequence.append(i + 1 + triangle_sequence[i - 1])

        res = 0
        for count in ratios.values():
            if count > 1:
                res += triangle_sequence[count - 2]
        return res


# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
solution.interchangeableRectangles([[4,8],[3,6],[10,20],[15,30]])
# solution.interchangeableRectangles([[16,1],[13,7],[20,18],[21,15],[20,3],[18,12],[23,14],[16,14],[5,25],[3,8],[6,17],[22,10],[25,17],[8,13],[8,11],[4,14],[2,17],[9,22],[3,15],[18,1],[19,13],[26,6],[26,14],[9,10],[12,6],[24,3],[21,8],[17,6],[16,7],[8,9],[20,24],[25,26],[22,23],[4,25],[23,23],[24,8],[14,4],[10,18],[13,6],[7,6],[24,15],[16,22],[17,19],[2,16],[23,21],[15,26],[7,17],[14,7],[10,26],[9,8],[7,10],[1,1],[11,17],[4,20],[19,24],[18,24],[9,21],[20,22],[21,12],[10,23],[5,9],[2,3],[6,17],[5,20],[11,15],[7,19],[5,9],[12,13],[15,19],[3,26],[19,25],[13,6],[22,13],[18,7],[4,9],[13,24],[22,21],[21,9],[25,26],[21,20],[9,13],[10,5],[11,18],[6,20],[16,8]])
