#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, minDiff = -1, float('inf')

        def dfs(node):
            if not node:
                return None

            dfs(node.left)

            nonlocal prev, minDiff
            if prev != -1:
                minDiff = min(minDiff, node.val - prev)

            prev = node.val

            dfs(node.right)
        
        dfs(root)
        return minDiff
        
# @lc code=end
solution = Solution()
root = deserialize("[0,null,2236,1277,2776,519]")
print(solution.minDiffInBST(root))
