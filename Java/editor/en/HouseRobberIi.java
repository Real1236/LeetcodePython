  /**
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed. All houses at this place are arranged in
a circle. That means the first house is the neighbor of the last one. Meanwhile,
 adjacent houses have a security system connected, and it will automatically
contact the police if two adjacent houses were broken into on the same night.

 Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.



 Example 1:


Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2)
, because they are adjacent houses.


 Example 2:


Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.


 Example 3:


Input: nums = [1,2,3]
Output: 3



 Constraints:


 1 <= nums.length <= 100
 0 <= nums[i] <= 1000


 Related Topics Array Dynamic Programming 👍 7282 👎 106

*/

  package com.shuzijun.leetcode.editor.en;

  import java.util.Arrays;

  public class HouseRobberIi{
      public static void main(String[] args) {
           Solution solution = new HouseRobberIi().new Solution();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1)
            return nums[0];
        return Math.max(helper(0, nums.length - 1, nums), helper(1, nums.length, nums));
    }

    private int helper(int start, int end, int[] nums) {
        int rob1 = 0, rob2 = 0;
        for (int i = start; i < end; i++) {
            int newRob = Math.max(rob1 + nums[i], rob2);
            rob1 = rob2;
            rob2 = newRob;
        }
        return rob2;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }