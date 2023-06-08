  /**
Given a string s, return the longest palindromic substring in s. 

 
 Example 1: 

 
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
 

 Example 2: 

 
Input: s = "cbbd"
Output: "bb"
 

 
 Constraints: 

 
 1 <= s.length <= 1000 
 s consist of only digits and English letters. 
 

 Related Topics String Dynamic Programming 👍 22760 👎 1319

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.ArrayList;
  import java.util.List;

  public class LongestPalindromicSubstring{
      public static void main(String[] args) {
           Solution solution = new LongestPalindromicSubstring().new Solution();
           solution.longestPalindrome("babad");
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public String longestPalindrome(String s) {
        String res = "";
        for (int i = 0; i < s.length(); i++) {
            res = helper(i, i, s, res);
            res = helper(i, i + 1, s, res);
        }
        return res;
    }

    private String helper(int left, int right, String s, String res) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            if (right - left + 1 > res.length())
                res = s.substring(left, right + 1);
            left--;
            right++;
        }
        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }