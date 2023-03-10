#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution(object):
    def calculate(self, s):
        stack = []
        number = 0
        result = 0
        sign = 1
        for c in s:
            if c.isdigit():
                number = (number * 10) + int(c)
    
            elif c == '+':
                result += (sign * number)
                number = 0
                sign = 1
    
            elif c == '-':
                result += (sign * number)
                number = 0
                sign = -1
                
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            
            elif c == ')':
                result += (sign * number)
                number = 0
                result *= stack.pop()
                result += stack.pop()
        
        if number != 0:
            result += (sign * number)
        return result

        
# @lc code=end
solution = Solution()
print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))    # 1 4 5 + 2 + + 3 - 6 8 + +
print(solution.calculate("- (3 + (4 + 5))"))
print(solution.calculate("1-(5)"))
print(solution.calculate("1-(     -2)"))