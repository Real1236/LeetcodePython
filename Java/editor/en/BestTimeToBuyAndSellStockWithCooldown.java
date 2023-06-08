  /**
You are given an array prices where prices[i] is the price of a given stock on 
the iᵗʰ day. 

 Find the maximum profit you can achieve. You may complete as many transactions 
as you like (i.e., buy one and sell one share of the stock multiple times) with 
the following restrictions: 

 
 After you sell your stock, you cannot buy stock on the next day (i.e., 
cooldown one day). 
 

 Note: You may not engage in multiple transactions simultaneously (i.e., you 
must sell the stock before you buy again). 

 
 Example 1: 

 
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
 

 Example 2: 

 
Input: prices = [1]
Output: 0
 

 
 Constraints: 

 
 1 <= prices.length <= 5000 
 0 <= prices[i] <= 1000 
 

 Related Topics Array Dynamic Programming 👍 6953 👎 236

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.Arrays;
  import java.util.HashMap;
  import java.util.List;
  import java.util.Map;

  public class BestTimeToBuyAndSellStockWithCooldown{
      public static void main(String[] args) {
           Solution solution = new BestTimeToBuyAndSellStockWithCooldown().new Solution();
           solution.maxProfit(new int[] {1,2,3,0,2});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int maxProfit(int[] prices) {
        Integer[][] cache = new Integer[2][prices.length];  // i = buying/selling, j = day, value = max profit
        return dfs(0, 1, cache, prices);
    }

    private int dfs(int day, int buying, Integer[][] cache, int[] prices) {
        if (day >= prices.length)
            return 0;

        if (cache[buying][day] != null)
            return cache[buying][day];

        int cooldown = dfs(day + 1, buying, cache, prices);
        int buyOrSell = Integer.MIN_VALUE;
        if (buying == 1)
            buyOrSell = dfs(day + 1, 0, cache, prices) - prices[day];
        else
            buyOrSell = dfs(day + 2, 1, cache, prices) + prices[day];

        int maxProfit = Math.max(cooldown, buyOrSell);
        cache[buying][day] = maxProfit;
        return maxProfit;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }