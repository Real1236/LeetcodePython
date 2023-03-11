#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from TreeNode import *


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(cur: TreeNode) -> List[TreeNode]:   # [max of one branch, sum of both branches]
            if not cur:
                return [0, 0]
            
            left = dfs(cur.left)
            right = dfs(cur.right)

            max_branch = max(left[0], right[0]) + cur.val
            max_both_branches = max(left[1], right[1], left[0] + right[0] + cur.val)

            return [max_branch, max_both_branches]

        return max(dfs(root))

# @lc code=end
solution = Solution()

root = deserialize("[-10,9,20,null,null,15,7]")
printTree(root)
print(solution.maxPathSum(root))
