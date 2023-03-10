#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(cur: TreeNode, from_parent: int) -> TreeNode:
            if not cur:
                return 0
            
            if cur.right:
                right = dfs(cur.right, from_parent)
                cur.val += right
            else:
                cur.val += from_parent
                
            if cur.left:
                left = dfs(cur.left, cur.val)
                return left
            return cur.val

        dfs(root, 0)
        return root

        
# @lc code=end
solution = Solution()
tree = deserialize("[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]")
printTree(tree)
print("")
printTree(solution.convertBST(tree))
