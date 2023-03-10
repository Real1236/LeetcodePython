#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
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
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0:[], 1:[TreeNode()]}
        def backtrack(n: int) -> List[TreeNode]:
            if n in dp:
                return dp[n]
            
            res = []
            for left in range(n):
                right = n - 1 - left
                left_subtrees = backtrack(left)
                right_subtrees = backtrack(right)
                for left_tree in left_subtrees:
                    for right_tree in right_subtrees:
                        res.append(TreeNode(0, left_tree, right_tree))
            dp[n] = res
            return res
        
        return backtrack(n)
    
        
# @lc code=end
solution = Solution()

print(solution.allPossibleFBT(7))
