# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([[root, 1, 1]])
        prevLevel = 1
        leftIndex = 1
        res = 0
        while q:
            node, index, level = q.popleft()
            if level > prevLevel:
                prevLevel = level
                leftIndex = index
            res = max(res, index - leftIndex + 1)
            if node.left:
                q.append([node.left, index * 2, level + 1])
            if node.right:
                q.append([node.right, index * 2 + 1, level + 1])
        return res
