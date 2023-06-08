  /**
Given two strings text1 and text2, return the length of their longest common 
subsequence. If there is no common subsequence, return 0. 

 A subsequence of a string is a new string generated from the original string 
with some characters (can be none) deleted without changing the relative order of 
the remaining characters. 

 
 For example, "ace" is a subsequence of "abcde". 
 

 A common subsequence of two strings is a subsequence that is common to both 
strings. 

 
 Example 1: 

 
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
 

 Example 2: 

 
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
 

 Example 3: 

 
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

 
 Constraints: 

 
 1 <= text1.length, text2.length <= 1000 
 text1 and text2 consist of only lowercase English characters. 
 

 Related Topics String Dynamic Programming 👍 8928 👎 102

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.HashMap;
  import java.util.Map;
  import java.util.Objects;

  public class LongestCommonSubsequence{
      public static void main(String[] args) {
           Solution solution = new LongestCommonSubsequence().new Solution();
           solution.longestCommonSubsequence("ylqpejqbalahwr", "yrkzavgdmdgtqpg");
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] dp = new int[text1.length() + 1][text2.length() + 1];
        for (int row = text1.length() - 1; row >= 0; row--) {
            for (int col = text2.length() - 1; col >= 0; col--) {
                int longest;
                if (text1.charAt(row) == text2.charAt(col))
                    longest = dp[row + 1][col + 1] + 1;
                else
                    longest = Math.max(dp[row + 1][col], dp[row][col + 1]);
                dp[row][col] = longest;
            }
        }
        return dp[0][0];
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }