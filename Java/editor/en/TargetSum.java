  /**
You are given an integer array nums and an integer target. 

 You want to build an expression out of nums by adding one of the symbols '+' 
and '-' before each integer in nums and then concatenate all the integers. 

 
 For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 
and concatenate them to build the expression "+2-1". 
 

 Return the number of different expressions that you can build, which evaluates 
to target. 

 
 Example 1: 

 
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be 
target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
 

 Example 2: 

 
Input: nums = [1], target = 1
Output: 1
 

 
 Constraints: 

 
 1 <= nums.length <= 20 
 0 <= nums[i] <= 1000 
 0 <= sum(nums[i]) <= 1000 
 -1000 <= target <= 1000 
 

 Related Topics Array Dynamic Programming Backtracking 👍 8200 👎 296

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.Arrays;
  import java.util.HashMap;
  import java.util.List;
  import java.util.Map;

  public class TargetSum{
      public static void main(String[] args) {
          Solution solution = new TargetSum().new Solution();
          //System.out.println(Arrays.stream(new int[] {2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53}).sum());;
          solution.findTargetSumWays(new int[] {2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53}, 1000);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        Integer[][] dp = new Integer[nums.length + 1][4001];
        return dfs(0, target + 1000, dp, nums);
    }

    private int dfs(int i, int target, Integer[][] dp, int[] nums) {
        if (target == 1000 && i == nums.length)
            return 1;
        if (i >= nums.length)
            return 0;

        if (dp[i][target] != null)
            return dp[i][target];

        dp[i][target] = dfs(i + 1, target - nums[i], dp, nums)
                + dfs(i + 1, target + nums[i], dp, nums);
        return dp[i][target];
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }