#
# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
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
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val != root2.val:
            return False
        
        a = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        b = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        return a or b
        
# @lc code=end
solution = Solution()

# root1 = deserialize("[1,2,3,4,5,6,null,null,null,7,8]")
# root2 = deserialize("[1,3,2,null,6,4,5,null,null,null,null,8,7]")
# print(solution.flipEquiv(root1, root2))

root1 = deserialize("[6,1,0]")
printTree(root1)
root2 = deserialize("[6,null,1]")
printTree(root2)
print(solution.flipEquiv(root1, root2))
