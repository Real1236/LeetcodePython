  /**
Given an integer n, return true if it is a power of three. Otherwise, return 
false. 

 An integer n is a power of three, if there exists an integer x such that n == 3
ˣ. 

 
 Example 1: 

 
Input: n = 27
Output: true
Explanation: 27 = 3³
 

 Example 2: 

 
Input: n = 0
Output: false
Explanation: There is no x where 3ˣ = 0.
 

 Example 3: 

 
Input: n = -1
Output: false
Explanation: There is no x where 3ˣ = (-1).
 

 
 Constraints: 

 
 -2³¹ <= n <= 2³¹ - 1 
 

 
Follow up: Could you solve it without loops/recursion?

 Related Topics Math Recursion 👍 2036 👎 192

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class PowerOfThree{
      public static void main(String[] args) {
           Solution solution = new PowerOfThree().new Solution();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public boolean isPowerOfThree(int n) {
        if (n == 1) {
            return true;
        } else if (n % 3 != 0 || n == 0) {
            return false;
        }

        return isPowerOfThree(n / 3);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }