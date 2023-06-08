  /**
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money. 

 Return the fewest number of coins that you need to make up that amount. If 
that amount of money cannot be made up by any combination of the coins, return -1. 

 You may assume that you have an infinite number of each kind of coin. 

 
 Example 1: 

 
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
 

 Example 2: 

 
Input: coins = [2], amount = 3
Output: -1
 

 Example 3: 

 
Input: coins = [1], amount = 0
Output: 0
 

 
 Constraints: 

 
 1 <= coins.length <= 12 
 1 <= coins[i] <= 2³¹ - 1 
 0 <= amount <= 10⁴ 
 

 Related Topics Array Dynamic Programming Breadth-First Search 👍 14671 👎 336

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class CoinChange{
      public static void main(String[] args) {
           Solution solution = new CoinChange().new Solution();
           solution.coinChange(new int[] {2}, 3);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int coinChange(int[] coins, int amount) {
        Integer[] dp = new Integer[amount + 1]; // Index -> Amount, Value -> Min # of coins needed
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            int min = Integer.MAX_VALUE;
            for (int coin : coins) {
                int index = i - coin;
                if (index >= 0 && dp[index] != null)
                    min = Math.min(1 + dp[index], min);
            }
            if (min != Integer.MAX_VALUE)
                dp[i] = min;
        }
        return dp[amount] != null ? dp[amount] : -1;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }