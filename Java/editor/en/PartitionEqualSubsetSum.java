  /**
Given a non-empty array nums containing only positive integers, find if the 
array can be partitioned into two subsets such that the sum of elements in both 
subsets is equal. 

 
 Example 1: 

 
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

 Example 2: 

 
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

 
 Constraints: 

 
 1 <= nums.length <= 200 
 1 <= nums[i] <= 100 
 

 Related Topics Array Dynamic Programming 👍 9378 👎 153

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.Arrays;
  import java.util.HashSet;
  import java.util.Set;

  public class PartitionEqualSubsetSum{
      public static void main(String[] args) {
           Solution solution = new PartitionEqualSubsetSum().new Solution();
           solution.canPartition(new int[] {3,3,1,5});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public boolean canPartition(int[] nums) {
        int sum = Arrays.stream(nums).sum();
        if (sum % 2 == 1) return false;

        sum /= 2;
        boolean[] dp = new boolean[sum+1];
        dp[0] = true;
        for (int num : nums) {
            for (int i = sum; i >= num; i--)
                dp[i] = dp[i] || dp[i-num];
        }
        return dp[sum];
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }