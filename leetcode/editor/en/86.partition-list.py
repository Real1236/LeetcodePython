#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p_node = None
        cur = head
        before_p_node = None
        while cur:
            if not p_node:
                if cur.val >= x:
                    p_node = cur
                else:
                    before_p_node = cur
                cur = cur.next
            elif cur.val < x:
                before_p_node.next = cur
                temp = cur.next
                cur.next = p_node
                cur = temp
            else:
                cur = cur.next
        return head

        
# @lc code=end
solution = Solution()
print_linked(solution.partition(convert_to_linked([1,4,3,2,5,2]), 3))
