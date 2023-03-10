#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from TreeNode import *


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while root and (root.val > high or root.val < low):
            if root.val > high:
                root = root.left
            elif root.val < low:
                root = root.right
        
        if root:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root


# @lc code=end
solution = Solution()

# test = deserialize("[3,1,4,null,2]")
# printTree(test)
# printTree(solution.trimBST(test, 1, 2))

# test = deserialize("[3,0,4,null,2,null,null,1]")
# printTree(test)
# printTree(solution.trimBST(test, 1, 3))

# test = deserialize("[45,30,46,10,36,null,49,8,24,34,42,48,null,4,9,14,25,31,35,41,43,47,null,0,6,null,null,11,20,null,28,null,33,null,null,37,null,null,44,null,null,null,1,5,7,null,12,19,21,26,29,32,null,null,38,null,null,null,3,null,null,null,null,null,13,18,null,null,22,null,27,null,null,null,null,null,39,2,null,null,null,15,null,null,23,null,null,null,40,null,null,null,16,null,null,null,null,null,17]")
# printTree(test)
# printTree(solution.trimBST(test, 32, 44))
