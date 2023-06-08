  /**
Given an encoded string, return its decoded string. 

 The encoding rule is: k[encoded_string], where the encoded_string inside the 
square brackets is being repeated exactly k times. Note that k is guaranteed to 
be a positive integer. 

 You may assume that the input string is always valid; there are no extra white 
spaces, square brackets are well-formed, etc. Furthermore, you may assume that 
the original data does not contain any digits and that digits are only for those 
repeat numbers, k. For example, there will not be input like 3a or 2[4]. 

 The test cases are generated so that the length of the output will never 
exceed 10⁵. 

 
 Example 1: 

 
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
 

 Example 2: 

 
Input: s = "3[a2[c]]"
Output: "accaccacc"
 

 Example 3: 

 
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

 
 Constraints: 

 
 1 <= s.length <= 30 
 s consists of lowercase English letters, digits, and square brackets '[]'. 
 s is guaranteed to be a valid input. 
 All the integers in s are in the range [1, 300]. 
 

 Related Topics String Stack Recursion 👍 9558 👎 417

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.ArrayList;
  import java.util.List;
  import java.util.Stack;

  public class DecodeString{
      public static void main(String[] args) {
           Solution solution = new DecodeString().new Solution();
           solution.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef");
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public String decodeString(String s) {
        Stack<String> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ']') {
                StringBuilder substring = new StringBuilder();
                while (!stack.peek().equals("[")) {
                    substring.append(new StringBuilder(stack.pop()).reverse());
                }
                stack.pop();

                int k = 0;
                int digit = 1;
                while (!stack.isEmpty() && Character.isDigit(stack.peek().charAt(0))) {
                    k = Integer.parseInt(stack.pop()) * digit + k;
                    digit *= 10;
                }

                substring.reverse();
                for (int j = 0; j < k; j++) stack.push(substring.toString());
            } else {
                stack.push(String.valueOf(s.charAt(i)));
            }
        }
        return String.join("", stack);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }