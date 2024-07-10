# Helper functions for testing
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

def serialize(root: TreeNode) -> str:
    levelOrderedList = []
    if root is not None:
        levelOrderedList.append(str(root.val))
    else:
        return "[]"

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        for i in range(levelSize):
            current = queue.popleft()

            if current.left is None:
                levelOrderedList.append("null")
            else:
                levelOrderedList.append(str(current.left.val))
                queue.append(current.left)

            if current.right is None:
                levelOrderedList.append("null")
            else:
                levelOrderedList.append(str(current.right.val))
                queue.append(current.right)

    while levelOrderedList[-1] == "null":
        levelOrderedList.pop()

    treeString = ",".join(levelOrderedList)

    return "[" + treeString + "]"

# Question 1
# Given two nodes in a valid binary search tree, find the minimum distance between the nodes. The distance between two nodes is the number of edges on the path from one node to the other.

# Input trees are given in level order.

# For this question, here's a couple of templated binary Tree structures you can use in your solution.

from collections import deque
from typing import List

def findMinDistance(root: TreeNode, a: int, b: int) -> int:
    def getPath(cur: TreeNode, path: List[TreeNode], target: int) -> bool:
        if not cur:
            return False
        
        path.append(cur)

        if cur.val == target:
            return True
        
        if(getPath(cur.left, path, target) or getPath(cur.right, path, target)):
            return True
        
        path.pop()
        return False
    
    a_path = []
    getPath(root, a_path, a)
    
    b_path = []
    getPath(root, b_path, b)
    
    for i in range(min(len(a_path), len(b_path))):
        if a_path[i].val != b_path[i].val:
            return len(a_path) + len(b_path) - 2 * i
    
    return len(a_path) + len(b_path) - 2 * min(len(a_path), len(b_path))

# Test Cases
root = deserialize("[4,2,6,1,3]")
a, b = 6, 1
print(findMinDistance(root, a, b))

root = deserialize("[1,0,48,null,null,12,49]")
a, b = 12, 49
print(findMinDistance(root, a, b))

root = deserialize("[5,2,12,1,3,9,21,null,null,null,null,null,null,19,25]")
a, b = 3, 9
print(findMinDistance(root, a, b))

root = deserialize("[1,2,3,4,5,6,7,null,null,null,null,null,8]")
a, b = 4, 5
print(findMinDistance(root, a, b))
a, b = 4, 6
print(findMinDistance(root, a, b))
a, b = 3, 4
print(findMinDistance(root, a, b))
a, b = 2, 4
print(findMinDistance(root, a, b))
a, b = 8, 5
print(findMinDistance(root, a, b))

# Used DFS to find the paths to node a and b. Then subtracted the intersection of the paths to get the minimum distance. TC and SC of O(n) for DFS.