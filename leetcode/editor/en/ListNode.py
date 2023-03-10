from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convert_to_linked(list: List[ListNode]) -> ListNode:
    cur = dummy = ListNode(0)
    for e in list:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next

def print_linked(head: ListNode):
    res = str(head.val)
    cur = head.next
    while cur:
        res += " -> " + str(cur.val)
        cur = cur.next
    print(res)