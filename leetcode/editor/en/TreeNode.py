from collections import deque


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

def printTree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1  
    nlevels = height(root)
    width =  pow(2,nlevels+1)

    q=[(root,0,width,'c')]
    levels=[]

    while(q):
        node,level,x,align= q.pop(0)
        if node:            
            if len(levels)<=level:
                levels.append([])
        
            levels[level].append([node,level,x,align])
            seg= width//(pow(2,level+1))
            q.append((node.left,level+1,x-seg,'l'))
            q.append((node.right,level+1,x+seg,'r'))

    for i,l in enumerate(levels):
        pre=0
        preline=0
        linestr=''
        pstr=''
        seg= width//(pow(2,i+1))
        for n in l:
            valstr= str(n[0].val)
            if n[3]=='r':
                linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                preline = n[2] 
            if n[3]=='l':
               linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
               preline = n[2] + seg + seg//2
            pstr+=' '*(n[2]-pre-len(valstr))+valstr #correct the potition acording to the number size
            pre = n[2]
        print(linestr)
        print(pstr)   

# example usage
# lst = "[1,2,3,null,null,4,5]"
# lst = "[2,1,3]"
# lst = "[4,2,7,1,3,6,9]"
# lst = "[5,1,4,null,null,3,6]"
# root = deserialize(lst)
# printTree(root)
