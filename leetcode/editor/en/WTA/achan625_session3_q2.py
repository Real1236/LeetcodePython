# Question 2
# You are given the root of a binary tree, a node with a specific value called target and an integer k. 
# Your task is to find all the nodes in the binary tree that are at a distance of exactly k from the target node. 
# Return an array containing the values of all such nodes (in any order). All of the tree node values are unique. 

# Example: 

# Input: 

# Tree = See Tree 1

# k = 2

# target = 9

# Output: [7, 5]

# Explanation: The nodes with values 7 and 5 have a distance of 2 from the target node that has a value of 9.


from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(data: str) -> TreeNode:
    if data == "[]":
        return None

    treeArray = data[1:-1].split(",")
    levelOrderNodes = []
    map = {}  # key -> index in treeArray, value -> corresponding TreeNode
    for i in range(len(treeArray)):
        node = treeArray[i]
        if node != "null":
            treeNode = TreeNode(int(node))
            levelOrderNodes.append(treeNode)
            map[i] = treeNode

    for i in range(len(levelOrderNodes)):
        current = levelOrderNodes[i]

        leftIndex = 2 * i + 1
        rightIndex = 2 * i + 2
        leftNull = leftIndex >= len(treeArray) or treeArray[leftIndex] == "null"
        rightNull = rightIndex >= len(treeArray) or treeArray[rightIndex] == "null"

        if not leftNull:
            current.left = map[leftIndex]
        if not rightNull:
            current.right = map[rightIndex]

    return levelOrderNodes[0]


class Solution:
    def findKDistanceNodes(self, tree: TreeNode, k: int, target: int) -> List[int]:
        nodeParents = {tree: None}

        def fillParents(root: TreeNode) -> TreeNode:
            if not root:
                return
            
            targetNode = None
            if root.left:
                nodeParents[root.left] = root
                targetNode = fillParents(root.left)
            if root.right:
                nodeParents[root.right] = root
                if targetNode:
                    fillParents(root.right)
                else:
                    targetNode = fillParents(root.right)

            if root.val == target:
                targetNode = root

            return targetNode
        
        targetNode = fillParents(tree)
        q = deque([targetNode])
        visited = set([targetNode])
        res = []
        layer = 0
        while q and layer <= k:
            layerSize = len(q)
            for _ in range(layerSize):
                node = q.popleft()
                visited.add(node)
                if layer == k:
                    res.append(node.val)
                    continue
                if node.left and node.left not in visited:
                    q.append(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                if nodeParents[node] and nodeParents[node] not in visited:
                    q.append(nodeParents[node])
            layer += 1
        return res

solution = Solution()

# Example 1
root = deserialize("[1,7,9,2,6,null,13,null,null,12,11,5,null]")
print(solution.findKDistanceNodes(root, 2, 9))

# Test Case 1
root = deserialize("[3,5,1,6,2,0,8,null,null,7,4]")
print(solution.findKDistanceNodes(root, 2, 5))

# Test Case 2
root = deserialize("[0,6,1,null,null,null,2,7,3,null,8,4,9,null,null,null,5]")
print(solution.findKDistanceNodes(root, 5, 7))
