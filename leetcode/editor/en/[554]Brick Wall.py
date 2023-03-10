# There is a rectangular brick wall in front of you with n rows of bricks. The 
# iᵗʰ row has some number of bricks each of the same height (i.e., one unit) but 
# they can be of different widths. The total width of each row is the same. 
# 
#  Draw a vertical line from the top to the bottom and cross the least bricks. 
# If your line goes through the edge of a brick, then the brick is not considered 
# as crossed. You cannot draw a line just along one of the two vertical edges of 
# the wall, in which case the line will obviously cross no bricks. 
# 
#  Given the 2D array wall that contains the information about the wall, return 
# the minimum number of crossed bricks after drawing such a vertical line. 
# 
#  
#  Example 1: 
#  
#  
# Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: wall = [[1],[1],[1]]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  n == wall.length 
#  1 <= n <= 10⁴ 
#  1 <= wall[i].length <= 10⁴ 
#  1 <= sum(wall[i].length) <= 2 * 10⁴ 
#  sum(wall[i]) is the same for each row i. 
#  1 <= wall[i][j] <= 2³¹ - 1 
#  
# 
#  Related Topics Array Hash Table 👍 2023 👎 112
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = {0: 0}
        for row in range(len(wall)):
            index = 0
            for col in range(len(wall[row]) - 1):
                index += wall[row][col]
                edges[index] = edges.get(index, 0) + 1

        return len(wall) - max(edges.values())


# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
# solution.leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]])
solution.leastBricks([[1, 1], [2], [1, 1]])
# print(solution.leastBricks([[100000000],[100000000],[100000000]]))
