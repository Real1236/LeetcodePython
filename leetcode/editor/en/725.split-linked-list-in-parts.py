# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        
        partSize = size // k
        remainder = size % k

        res = []
        cur = head
        for i in range(k):
            partHead = cur
            for _ in range(partSize - 1):
                cur = cur.next
            if remainder:
                if partSize > 0:
                    cur = cur.next
                remainder -= 1
            if cur:
                temp = cur.next
                cur.next = None
                cur = temp
            res.append(partHead)

        return res
