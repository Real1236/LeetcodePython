#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}   # Key -> key int, Value -> ListNode
        self.head, self.tail = ListNode(-1, -1), ListNode(-1, -1)   # Dummy nodes
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity

    def remove(self, node: ListNode) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def append(self, node: ListNode) -> None:
        prev, next = self.tail.prev, self.tail
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.append(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        self.map[key] = ListNode(key, value)
        self.append(self.map[key])

        if len(self.map) > self.capacity:
            self.map.pop(self.head.next.key)
            self.remove(self.head.next)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

# #Test 1
# lRUCache = LRUCache(2)
# lRUCache.put(1, 1)  # cache is {1=1}
# lRUCache.put(2, 2)  # cache is {1=1, 2=2}
# print(lRUCache.get(1))     # return 1
# lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(lRUCache.get(2))     # returns -1 (not found)
# lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(lRUCache.get(1))     # return -1 (not found)
# print(lRUCache.get(3))     # return 3
# print(lRUCache.get(4))

# #Test 2
# lRUCache = LRUCache(2)
# lRUCache.put(1, 0)  # cache is {1=1}
# lRUCache.put(2, 2)  # cache is {1=1, 2=2}
# print(lRUCache.get(1))     # return 0
# lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(lRUCache.get(2))     # returns -1 (not found)
# lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(lRUCache.get(1))     # return -1 (not found)
# print(lRUCache.get(3))     # return 3
# print(lRUCache.get(4))

# #Test 3
# lRUCache = LRUCache(2)
# print(lRUCache.get(2))     # return -1
# lRUCache.put(2, 6)  # cache is {2=6}
# print(lRUCache.get(1))     # return -1
# lRUCache.put(1, 5)  # cache is {1=5, 2=6}
# lRUCache.put(1, 2)  # cache is {1=2, 2=6}
# print(lRUCache.get(1))     # return 2
# print(lRUCache.get(2))     # returns 6

#Test 4
lRUCache = LRUCache(3)
lRUCache.put(1, 1)  # cache is {1=1}
lRUCache.put(2, 2)  # cache is {1=1, 2=2}
lRUCache.put(3, 3)  # cache is {1=1, 2=2, 3=3}
lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {2=2, 3=3, 4=4}
print(lRUCache.get(4))     # return 4
print(lRUCache.get(3))     # return 3
print(lRUCache.get(2))     # return 1
print(lRUCache.get(1))     # returns -1 (not found)
lRUCache.put(5, 5)  # LRU key was 4, evicts key 4, cache is {3=3, 2=2, 5=5}
print(lRUCache.get(1))     # returns -1
print(lRUCache.get(2))     # return 2
print(lRUCache.get(3))     # return 3
print(lRUCache.get(4))     # return -1
print(lRUCache.get(5))     # return 5