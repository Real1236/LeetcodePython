  /**
Given an integer array nums, return the length of the longest strictly 
increasing subsequence. 

 
 Example 1: 

 
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
length is 4.
 

 Example 2: 

 
Input: nums = [0,1,0,3,2,3]
Output: 4
 

 Example 3: 

 
Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

 
 Constraints: 

 
 1 <= nums.length <= 2500 
 -10⁴ <= nums[i] <= 10⁴ 
 

 
 Follow up: Can you come up with an algorithm that runs in O(n log(n)) time 
complexity? 

 Related Topics Array Binary Search Dynamic Programming 👍 15797 👎 291

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class LongestIncreasingSubsequence{
      public static void main(String[] args) {
           Solution solution = new LongestIncreasingSubsequence().new Solution();
           solution.lengthOfLIS(new int[] {10,9,2,5,3,7,101,18});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int lengthOfLIS(int[] nums) {
        int res = -1;
        int[] dp = new int[nums.length];
        for (int i = nums.length - 1; i >= 0; i--) {
            int max = 0;
            for (int j = i; j < nums.length; j++) {
                if (nums[i] < nums[j])
                    max = Math.max(max, dp[j]);
            }
            dp[i] = ++max;
            res = Math.max(max, res);
        }
        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }