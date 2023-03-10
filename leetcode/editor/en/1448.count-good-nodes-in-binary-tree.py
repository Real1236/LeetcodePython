#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(cur: TreeNode, max_in_path: int) -> int:
            if not cur:
                return 0
            max_in_path = max(max_in_path, cur.val)
            sum = dfs(cur.left, max_in_path)
            sum += dfs(cur.right, max_in_path)
            sum += 0 if max_in_path > cur.val else 1
            return sum
        
        return dfs(root, float('-inf'))
        
# @lc code=end
solution = Solution()
ex1 = deserialize("[3,1,4,3,null,1,5]")
printTree(ex1)
print(solution.goodNodes(ex1))
