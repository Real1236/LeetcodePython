  /**
You are a professional robber planning to rob houses along a street. Each house 
has a certain amount of money stashed, the only constraint stopping you from 
robbing each of them is that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into 
on the same night. 

 Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
 

 
 Example 1: 

 
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
 

 Example 2: 

 
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (
money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

 
 Constraints: 

 
 1 <= nums.length <= 100 
 0 <= nums[i] <= 400 
 

 Related Topics Array Dynamic Programming 👍 15396 👎 301

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.ArrayList;
  import java.util.HashMap;
  import java.util.List;
  import java.util.Map;

  public class HouseRobber{
      public static void main(String[] args) {
           Solution solution = new HouseRobber().new Solution();
           solution.rob(new int[] {2,1,1,2});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1)
            return nums[0];
        if (nums.length == 2)
            return Math.max(nums[0], nums[1]);

        nums[1] = Math.max(nums[0], nums[1]);
        for (int i = 2; i < nums.length; i++)
            nums[i] = Math.max(nums[i - 2] + nums[i], nums[i - 1]);
        return nums[nums.length - 1];
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }