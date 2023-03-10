#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from ListNode import *


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left_head: Optional[ListNode], right_head: Optional[ListNode]) -> Optional[ListNode]:
            if not left_head:
                return right_head
            if not right_head:
                return left_head
            
            new_head = None
            if left_head.val <= right_head.val:
                new_head = left_head
                left_head = left_head.next
            else:
                new_head = right_head
                right_head = right_head.next
            current = new_head

            while left_head and right_head:
                if left_head.val <= right_head.val:
                    current.next = left_head
                    left_head = left_head.next
                else:
                    current.next = right_head
                    right_head = right_head.next
                current = current.next
            
            current.next = left_head if left_head else right_head
            return new_head

        def middleNode(start: Optional[ListNode]) -> Optional[ListNode]:
            before_mid = None
            while start and start.next:
                before_mid = before_mid.next if before_mid else start
                start = start.next.next
            mid = before_mid.next
            before_mid.next = None
            return mid
        
        if not head or not head.next:
            return head
        right, left = self.sortList(middleNode(head)), self.sortList(head)
        return merge(left, right)
        
# @lc code=end
solution = Solution()
test1head = convert_to_linked([-1,5,3,4,0])
print_linked(solution.sortList(test1head))
