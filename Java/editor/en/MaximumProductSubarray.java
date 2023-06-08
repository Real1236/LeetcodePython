  /**
Given an integer array nums, find a subarray that has the largest product, and 
return the product. 

 The test cases are generated so that the answer will fit in a 32-bit integer. 

 
 Example 1: 

 
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
 

 Example 2: 

 
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

 
 Constraints: 

 
 1 <= nums.length <= 2 * 10⁴ 
 -10 <= nums[i] <= 10 
 The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
integer. 
 

 Related Topics Array Dynamic Programming 👍 14472 👎 424

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class MaximumProductSubarray{
      public static void main(String[] args) {
           Solution solution = new MaximumProductSubarray().new Solution();
           solution.maxProduct(new int[] {4,2,-1,2,2,3});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int maxProduct(int[] nums) {
        int max = 1, min = 1, res = Integer.MIN_VALUE;
        for (int num : nums) {
            if (num == 0) {
                max = 1;
                min = 1;
                res = Math.max(res, 0);
                continue;
            }

            int checkMax = max * num;
            int checkMin = min * num;
            max = Math.max(Math.max(checkMax, checkMin), num);
            min = Math.min(Math.min(checkMax, checkMin), num);
            res = Math.max(res, max);
        }
        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }