  /**
Given a string s, return the number of palindromic substrings in it. 

 A string is a palindrome when it reads the same backward as forward. 

 A substring is a contiguous sequence of characters within the string. 

 
 Example 1: 

 
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

 Example 2: 

 
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

 
 Constraints: 

 
 1 <= s.length <= 1000 
 s consists of lowercase English letters. 
 

 Related Topics String Dynamic Programming 👍 8401 👎 179

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class PalindromicSubstrings{
      public static void main(String[] args) {
           Solution solution = new PalindromicSubstrings().new Solution();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int countSubstrings(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            count += numOfPals(i, i, s);
            count += numOfPals(i, i + 1, s);
        }
        return count;
    }

    private int numOfPals(int left, int right, String s) {
        int count = 0;
        while (left >= 0 && right < s.length() && s.charAt(left--) == s.charAt(right++))
            count++;
        return count;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }