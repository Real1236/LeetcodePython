  /**
Implement pow(x, n), which calculates x raised to the power n (i.e., xⁿ). 

 
 Example 1: 

 
Input: x = 2.00000, n = 10
Output: 1024.00000
 

 Example 2: 

 
Input: x = 2.10000, n = 3
Output: 9.26100
 

 Example 3: 

 
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2⁻² = 1/2² = 1/4 = 0.25
 

 
 Constraints: 

 
 -100.0 < x < 100.0 
 -2³¹ <= n <= 2³¹-1 
 -10⁴ <= xⁿ <= 10⁴ 
 

 Related Topics Math Recursion 👍 5638 👎 6231

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class PowxN{
      public static void main(String[] args) {
           Solution solution = new PowxN().new Solution();
           System.out.println(solution.myPow(2, 10));
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public double myPow(double x, int n) {
        if (n < 0) {
            return 1 / multiply(x, -n);
        } else if (n > 0) {
            return multiply(x, n);
        }

        return 1;
    }

    private double multiply(double x, int n) {
        if (n == 0) return 1;
        if (x == 0) return 0;

        if (n % 2 == 0) {
            return multiply(x * x, n / 2);
        } else {
            return x * multiply(x * x, n / 2);
        }
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }