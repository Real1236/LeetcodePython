#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#

# @lc code=start

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


from typing import List


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        def checkSubgrid(startRow: int, startCol: int, size: int) -> List[int]:
            node = Node(grid[startRow][startCol], 1, None, None, None, None)
            breakLoop = False
            for row in range(startRow, startRow + size):
                for col in range(startCol, startCol + size):
                    val = grid[row][col]
                    if val != node.val:
                        halfSize = size // 2
                        node.isLeaf = 0
                        node.topLeft = checkSubgrid(startRow, startCol, halfSize)
                        node.topRight = checkSubgrid(startRow, startCol + halfSize, halfSize)
                        node.bottomLeft = checkSubgrid(startRow + halfSize, startCol, halfSize)
                        node.bottomRight = checkSubgrid(startRow + halfSize, startCol + halfSize, halfSize)
                        breakLoop = True
                        break
                if breakLoop:
                    break
            return node

        return checkSubgrid(0, 0, len(grid))
        
# @lc code=end

