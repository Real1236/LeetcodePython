  /**
Given a string s and a dictionary of strings wordDict, return true if s can be 
segmented into a space-separated sequence of one or more dictionary words. 

 Note that the same word in the dictionary may be reused multiple times in the 
segmentation. 

 
 Example 1: 

 
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
 

 Example 2: 

 
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen 
apple".
Note that you are allowed to reuse a dictionary word.
 

 Example 3: 

 
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

 
 Constraints: 

 
 1 <= s.length <= 300 
 1 <= wordDict.length <= 1000 
 1 <= wordDict[i].length <= 20 
 s and wordDict[i] consist of only lowercase English letters. 
 All the strings of wordDict are unique. 
 

 Related Topics Hash Table String Dynamic Programming Trie Memoization 👍 12884 
👎 546

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.List;

  public class WordBreak{
      public static void main(String[] args) {
           Solution solution = new WordBreak().new Solution();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[s.length()] = true;
        for (int i = s.length(); i >= 0; i--) {
            for (String word : wordDict) {
                if (s.startsWith(word, i))
                    dp[i] = dp[i + word.length()];
                if (dp[i])
                    break;
            }
        }
        return dp[0];
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }