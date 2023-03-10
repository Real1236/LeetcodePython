#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for operation in operations:
            if operation == "+":
                stack.append(stack[-1] + stack[-2])
            elif operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)
        
# @lc code=end

