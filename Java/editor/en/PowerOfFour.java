  /**
Given an integer n, return true if it is a power of four. Otherwise, return 
false. 

 An integer n is a power of four, if there exists an integer x such that n == 4ˣ
. 

 
 Example 1: 
 Input: n = 16
Output: true
 
 Example 2: 
 Input: n = 5
Output: false
 
 Example 3: 
 Input: n = 1
Output: true
 
 
 Constraints: 

 
 -2³¹ <= n <= 2³¹ - 1 
 

 
Follow up: Could you solve it without loops/recursion?

 Related Topics Math Bit Manipulation Recursion 👍 2584 👎 314

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class PowerOfFour{
      public static void main(String[] args) {
           Solution solution = new PowerOfFour().new Solution();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public boolean isPowerOfFour(int n) {
        if (n == 1) {
            return true;
        } else if (n % 4 != 0 || n == 0) {
            return false;
        }

        return isPowerOfFour(n / 4);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }