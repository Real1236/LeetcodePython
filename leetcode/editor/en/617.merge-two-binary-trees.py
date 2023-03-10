#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(a: TreeNode, b:TreeNode, parent: TreeNode, left: bool=True) -> None:
            if not (a or b):
                return
            if not a:
                if left:
                    parent.left = b
                else:
                    parent.right = b
            elif not b:
                if left:
                    parent.left = a
                else:
                    parent.right = a
            else:
                a.val += b.val
                dfs(a.left, b.left, a)
                dfs(a.right, b.right, a, False)
        
        if not (root1 or root2):
            return None
        if not root1:
            return root2
        elif not root2:
            return root1
        dfs(root1, root2, root1)
        return root1

# @lc code=end

