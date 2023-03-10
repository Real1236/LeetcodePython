#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(cur: TreeNode, nodes_before: int) -> tuple:
            if not cur:
                return (0, False)
            left = dfs(cur.left, nodes_before)
            if left[1]:
                return left
            
            nodes_before += left[0]
            if nodes_before == k - 1:
                return (cur.val, True)
            
            right = dfs(cur.right, nodes_before + 1)
            if right[1]:
                return right
            
            return (left[0] + right[0] + 1, False)
        
        return dfs(root, 0)[0]

# @lc code=end
solution = Solution()

test1 = deserialize("[3,1,4,null,2]")
printTree(test1)
print(solution.kthSmallest(test1, 1))

test2 = deserialize("[5,3,6,2,4,null,null,1]")
printTree(test2)
print(solution.kthSmallest(test2, 3))

test3 = deserialize("[1,null,2]")
printTree(test3)
print(solution.kthSmallest(test3, 2))

test4 = deserialize("[5,3,6,2,4,null,null,1]")
printTree(test4)
print(solution.kthSmallest(test4, 4))

test5 = deserialize("[45,30,46,10,36,null,49,8,24,34,42,48,null,4,9,14,25,31,35,41,43,47,null,0,6,null,null,11,20,null,28,null,33,null,null,37,null,null,44,null,null,null,1,5,7,null,12,19,21,26,29,32,null,null,38,null,null,null,3,null,null,null,null,null,13,18,null,null,22,null,27,null,null,null,null,null,39,2,null,null,null,15,null,null,23,null,null,null,40,null,null,null,16,null,null,null,null,null,17]")
# printTree(test5)
print(solution.kthSmallest(test5, 32))
