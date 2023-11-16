# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        for _ in range(k - 1):
            left = left.next
            
        right, b = head, left
        while b.next:
            right = right.next
            b = b.next
        
        left.val, right.val = right.val, left.val
        return head
