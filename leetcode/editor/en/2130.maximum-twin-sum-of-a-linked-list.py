# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur, prev = slow, None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        res = 0
        a, b = head, prev
        while b:
            res = max(res, a.val + b.val)
            a = a.next
            b = b.next
            
        return res
