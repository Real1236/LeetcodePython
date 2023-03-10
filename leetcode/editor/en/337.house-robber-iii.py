#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
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
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(cur: TreeNode) -> list:
            if not cur:
                return [0,0]
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            skip_cur = max(left) + max(right)
            add_cur = left[1] + right[1] + cur.val
            return [add_cur, skip_cur]

        return max(dfs(root))

# @lc code=end
solution = Solution()

tree1 = deserialize("[3,2,3,null,3,null,1]")
printTree(tree1)
print(solution.rob(tree1))
