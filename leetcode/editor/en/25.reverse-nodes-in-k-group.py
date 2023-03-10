#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy

        cur = head
        while True:
            nextGroup = cur
            count = 0
            while nextGroup and count < k:
                nextGroup = nextGroup.next
                count += 1
            if count < k and not nextGroup:
                break

            prev = nextGroup
            while cur != nextGroup:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            temp = prevGroup.next
            prevGroup.next = prev
            prevGroup = temp
        
        return dummy.next

# @lc code=end
solution = Solution()
# linked_list = convert([1,2,3,4,5])
linked_list = convert_to_linked([1,2])
print_linked(solution.reverseKGroup(linked_list, 2))
