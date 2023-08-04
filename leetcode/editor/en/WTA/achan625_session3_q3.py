# Question 3
# You are given two non-empty linked lists that represent two non-negative integers. 
# The digits of each integer are stored in reverse order, and each node in the linked list contains a single digit. 
# Your task is to add the two numbers represented by these linked lists and return the sum as a new linked list.

# You can assume that the input linked lists do not contain any leading zeros, except the number 0 itself. 
 
# Example:
# Input: 
# Linked List 1 = 7->8->2, Linked List 2 = 8->4->3
# Output:
# Linked List Result = 5->3->6
# Explanation
# 287 + 348 = 635


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


class Solution:
    def addLinkedLists(self, head1: ListNode, head2: ListNode) -> ListNode:
        def add(num: int, cur: ListNode) -> int:
            digit = 0
            while cur:
                num += cur.val * 10 ** digit
                cur = cur.next
                digit += 1
            return num

        total = add(0, head1)
        total = add(total, head2)

        prev = None
        for c in str(total):
            cur = ListNode(int(c))
            cur.next = prev
            prev = cur
        
        return cur

solution = Solution()

# Example 1
print_linked(solution.addLinkedLists(convert_to_linked([7,8,2]),convert_to_linked([8,4,3])))

# Test Case 1
print_linked(solution.addLinkedLists(convert_to_linked([2,4,3]),convert_to_linked([5,6,4])))

# Test Case 2
print_linked(solution.addLinkedLists(convert_to_linked([9,9,9,9,9,9,9]),convert_to_linked([9,9,9,9])))
