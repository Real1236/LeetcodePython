#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import List, Optional

from TreeNode import *


class Solution:
    def __init__(self, curId=1):
        self.curId = curId

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        serialToId = {}
        idCount = defaultdict(int)
        res = []

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            serial = str(left) + "," + str(node.val) + "," + str(right)
            serialId = serialToId.get(serial, self.curId)
            if serialId == self.curId:
                self.curId += 1
            serialToId[serial] = serialId
            idCount[serialId] += 1
            if idCount[serialId] == 2:
                print(node.val)
                res.append(node)
            return serialId
        
        dfs(root)
        return res
            
# @lc code=end
solution = Solution()
root = deserialize("[1,2,3,4,null,2,4,null,null,4]")
printTree(root)
for tree in solution.findDuplicateSubtrees(root):
    printTree(tree)
