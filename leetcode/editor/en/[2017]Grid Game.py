# You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] 
# represents the number of points at position (r, c) on the matrix. Two robots are 
# playing a game on this matrix. 
# 
#  Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot 
# may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c))
# . 
# 
#  At the start of the game, the first robot moves from (0, 0) to (1, n-1), 
# collecting all the points from the cells on its path. For all cells (r, c) 
# traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) 
# to (1, n-1), collecting the points on its path. Note that their paths may 
# intersect with one another. 
# 
#  The first robot wants to minimize the number of points collected by the 
# second robot. In contrast, the second robot wants to maximize the number of points 
# it collects. If both robots play optimally, return the number of points collected 
# by the second robot. 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [[2,5,4],[1,5,1]]
# Output: 4
# Explanation: The optimal path taken by the first robot is shown in red, and 
# the optimal path taken by the second robot is shown in blue.
# The cells visited by the first robot are set to 0.
# The second robot will collect 0 + 0 + 4 + 0 = 4 points.
#  
# 
#  Example 2: 
#  
#  
# Input: grid = [[3,3,1],[8,5,2]]
# Output: 4
# Explanation: The optimal path taken by the first robot is shown in red, and 
# the optimal path taken by the second robot is shown in blue.
# The cells visited by the first robot are set to 0.
# The second robot will collect 0 + 3 + 1 + 0 = 4 points.
#  
# 
#  Example 3: 
#  
#  
# Input: grid = [[1,3,1,15],[1,3,3,1]]
# Output: 7
# Explanation: The optimal path taken by the first robot is shown in red, and 
# the optimal path taken by the second robot is shown in blue.
# The cells visited by the first robot are set to 0.
# The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.
#  
# 
#  
#  Constraints: 
# 
#  
#  grid.length == 2 
#  n == grid[r].length 
#  1 <= n <= 5 * 10⁴ 
#  1 <= grid[r][c] <= 10⁵ 
#  
# 
#  Related Topics Array Matrix Prefix Sum 👍 566 👎 16
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix1, prefix2 = grid[0].copy(), grid[1].copy()

        for i in range(1, n):
            prefix1[i] += prefix1[i - 1]
            prefix2[i] += prefix2[i - 1]

        lowest = float("inf")
        for i in range(n):
            top = prefix1[-1] - prefix1[i]
            bottom = prefix2[i - 1] if i > 0 else 0
            second_robot = max(top, bottom)
            lowest = min(lowest, second_robot)

        return lowest


# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
# solution.gridGame([[2,5,4],[1,5,1]])
solution.gridGame([[20, 3, 20, 17, 2, 12, 15, 17, 4, 15], [20, 10, 13, 14, 15, 5, 2, 3, 14, 3]])