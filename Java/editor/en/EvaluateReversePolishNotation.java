  /**
Evaluate the value of an arithmetic expression in Reverse Polish Notation. 

 Valid operators are +, -, *, and /. Each operand may be an integer or another 
expression. 

 Note that division between two integers should truncate toward zero. 

 It is guaranteed that the given RPN expression is always valid. That means the 
expression would always evaluate to a result, and there will not be any 
division by zero operation. 

 
 Example 1: 

 
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
 

 Example 2: 

 
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
 

 Example 3: 

 
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

 
 Constraints: 

 
 1 <= tokens.length <= 10⁴ 
 tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the 
range [-200, 200]. 
 

 Related Topics Array Math Stack 👍 4061 👎 718

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.Stack;

  public class EvaluateReversePolishNotation{
      public static void main(String[] args) {
           Solution solution = new EvaluateReversePolishNotation().new Solution();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> nums = new Stack<>();
        for (String token : tokens) {
            if (token.equals("+")) {
                nums.push(nums.pop() + nums.pop());
            } else if (token.equals("-")) {
                int second = nums.pop();
                int first = nums.pop();
                nums.push(first - second);
            } else if (token.equals("*")) {
                nums.push(nums.pop() * nums.pop());
            } else if (token.equals("/")) {
                int second = nums.pop();
                int first = nums.pop();
                nums.push(first / second);
            } else {
                nums.push(Integer.parseInt(token));
            }
        }
        return nums.pop();
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }