#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node: TreeNode, str_tree: str) -> str:
            str_tree += str(node.val)
            if not (node.left or node.right):
                return str_tree
            
            str_tree += "("
            str_tree = dfs(node.left, str_tree) if node.left else str_tree
            str_tree += ")"
            if node.right:
                str_tree += "("
                str_tree = dfs(node.right, str_tree)
                str_tree += ")"
            
            return str_tree

        return dfs(root, "")
        
# @lc code=end
solution = Solution()
tree1 = deserialize("[1,2,3,4]")
printTree(tree1)
print(solution.tree2str(tree1))
