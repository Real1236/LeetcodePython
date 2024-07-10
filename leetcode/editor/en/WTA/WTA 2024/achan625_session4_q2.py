# Question 2
# Given a valid mathematical expression, convert it from infix notation to postfix notation. Valid symbols in the input are: uppercase and lowercase letters, +, -, *, and /.

# Infix: A + B
# Postfix: AB+

# Example 1:
# Input: "A+B*C+D"
# Output: "ABC*+D+"

# Example 2:

# Input: "A*C/B-D+E"
# Output: "AC*B/D-E+

def to_postfix(infix: str) -> str:
    res, stack = "", []
    for c in infix:
        if c.isalpha():
            res += c
        elif c == "*":
            stack.append(c)
        else:
            while stack:
                res += stack.pop()
            stack.append(c)
    while stack:
        res += stack.pop()
    return res


print(to_postfix("A+B*C+D"))
print(to_postfix("A*C/B-D+E"))
print(to_postfix("A+B"))
print(to_postfix("G-H+I*J"))
print(to_postfix("L/M-N*O+P"))

# It iterates through the input string, directly appending letters to the result and using a stack for operators to manage precedence.  The function's time complexity is O(N), and its space complexity is also O(N), due to the stack usage for operators.