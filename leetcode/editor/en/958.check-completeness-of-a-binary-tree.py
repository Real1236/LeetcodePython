#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
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
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        end = False
        while q:
            node = q.popleft()
            if end and node:
                return False
            if not node:
                end = True
            else:                
                q.append(node.left)
                q.append(node.right)
        return True
        
        
        
# @lc code=end
# printTree(deserialize("[1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15]"))
solution = Solution()

root = deserialize("[1,2,3,4,5,6]")
printTree(root)
print(solution.isCompleteTree(root))

root = deserialize("[1,2,3,4,5,null,7]")
printTree(root)
print(solution.isCompleteTree(root))

root = deserialize("[1,2,null,4,5,6,7,8,9]")
printTree(root)
print(solution.isCompleteTree(root))
