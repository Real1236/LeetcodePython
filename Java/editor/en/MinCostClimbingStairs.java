  /**
You are given an integer array cost where cost[i] is the cost of iᵗʰ step on a 
staircase. Once you pay the cost, you can either climb one or two steps. 

 You can either start from the step with index 0, or the step with index 1. 

 Return the minimum cost to reach the top of the floor. 

 
 Example 1: 

 
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
 

 Example 2: 

 
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

 
 Constraints: 

 
 2 <= cost.length <= 1000 
 0 <= cost[i] <= 999 
 

 Related Topics Array Dynamic Programming 👍 8336 👎 1314

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class MinCostClimbingStairs{
      public static void main(String[] args) {
           Solution solution = new MinCostClimbingStairs().new Solution();
           solution.minCostClimbingStairs(new int[] {1,100,1,1,1,100,1,1,100,1});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        for (int i = cost.length - 3; i >= 0; i--)
            cost[i] = Math.min(cost[i + 1], cost[i + 2]) + cost[i];
        return Math.min(cost[0], cost[1]);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }