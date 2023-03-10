#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        postfix = []
        stack = []
        num = 0
        for c in s:
            if c.isnumeric():
                num *= 10
                num += int(c)
            elif c != " ":
                postfix.append(num)
                num = 0
            
            if c == "+" or c == "-":
                while stack:
                    postfix.append(stack.pop())
                stack.append(c)
            elif c == "*" or c == "/":
                while stack and (stack[-1] == "*" or stack[-1] == "/"):
                    postfix.append(stack.pop())
                stack.append(c)

        postfix.append(num)
        while stack:
            postfix.append(stack.pop())

        res = 0
        for c in postfix:
            if c == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif c == "-":
                res = stack[-2] - stack.pop()
                stack.pop()
                stack.append(res)
            elif c == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif c == "/":
                res = stack[-2] // stack.pop()
                stack.pop()
                stack.append(res)
            else:
                stack.append(int(c))

        return stack[0]

        
# @lc code=end
solution = Solution()
print(solution.calculate("3+2*2"))
print(solution.calculate(" 3/2 "))
print(solution.calculate(" 3+5 / 2 "))

