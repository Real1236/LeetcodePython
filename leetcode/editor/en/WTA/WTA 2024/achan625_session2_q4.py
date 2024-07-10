# Question 4 - Linked Lists
# Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# Example 1:
# Input: 
# N = 8
# head = Node(X)
# values in linked list: {1,2,2,1,2,0,2,2}
# E.g. head = Node(1), head.next = Node(2), and so on
# Output:
# The head of a linked list sorted as followed {0, 1, 1, 2, 2, 2, 2, 2}
# Explanation:
# All the 0s are segregated to the left end of the linked list, 2s to the right end of the list, and 1s in between.

# Example 2:
# Input: 
# N = 4
# head = Node(X)
# values in linked list: { 2, 2, 0, 1}
# Output:
# The head of a linked list sorted as followed {0, 1, 2, 2}
# Explanation:
# After arranging all the 0s,1s and 2s in the given format, the output will be 0 1 2 2.

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def segregate(head: ListNode) -> ListNode:
        zeroD = ListNode(0)
        oneD = ListNode(1)
        twoD = ListNode(2)

        zero = zeroD
        one = oneD
        two = twoD
        
        curr_node = head
        while curr_node :
            if curr_node.val == 0:
                zero.next = curr_node
                zero = zero.next
            elif curr_node.val == 1:
                one.next = curr_node
                one = one.next
            else:
                two.next = curr_node
                two =two.next
            curr_node = curr_node.next
        
        if oneD.next:
            zero.next = oneD.next
        else:
            zero.next = twoD.next
        one.next = twoD.next
        two.next = None
        
        return zeroD.next

# Function to create a linked list from a list of values
def createLinkedList(values: List[int]):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Function to print the linked list
def printLinkedList(head: ListNode) -> None:
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Test cases
values = [1, 2, 2, 1, 2, 0, 2, 2]
head = createLinkedList(values)
printLinkedList(segregate(head))

values = [2, 2, 0, 1]
head = createLinkedList(values)
printLinkedList(segregate(head))

values = [0, 1, 0, 2, 1, 0]
head = createLinkedList(values)
printLinkedList(segregate(head))

values = [2, 1, 0, 0, 2, 1, 1, 2]
head = createLinkedList(values)
printLinkedList(segregate(head))

# Segregates a linked list into three separate lists based on the node values (0s, 1s, and 2s), using three dummy nodes to track the starts of these lists. It traverses the original list once, appending each node to the appropriate list based on its value. Finally, it links these three lists together in the order of 0s, 1s, and 2s, and returns the head of the newly ordered list. This approach ensures a time complexity of O(N) and a space complexity of O(1), as it reuses the original nodes without requiring additional space for node storage.