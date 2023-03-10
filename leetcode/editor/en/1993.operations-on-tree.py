#
# @lc app=leetcode id=1993 lang=python3
#
# [1993] Operations on Tree
#

# @lc code=start
from typing import List


class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = [[] for i in range(len(parent))]
        for i, p in enumerate(parent):
            if p >= 0:
                self.children[p].append(i)
        self.locked = [0] * len(parent)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] == 0:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = 0
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        def unlockDescendants(num: int, locked_found: bool) -> bool:
            if self.locked[num] != 0:
                self.locked[num] = 0
                locked_found = True
            for c in self.children[num]:
                locked_found = unlockDescendants(c, locked_found) or locked_found
            return locked_found

        if self.locked[num] != 0:
            return False
        cur = num
        while cur >= 0:
            if self.locked[cur] != 0:
                return False
            cur = self.parent[cur]
        if unlockDescendants(num, False):
            self.locked[num] = user
            return True
        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
# @lc code=end
lockingTree = LockingTree([-1, 0, 0, 1, 1, 2, 2])
print(lockingTree.lock(2,2))
print(lockingTree.unlock(2, 3))
print(lockingTree.unlock(2, 2))
print(lockingTree.lock(4, 5))
print(lockingTree.upgrade(0, 1))
print(lockingTree.lock(0, 1))