  /**
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1
 and s2. 

 An interleaving of two strings s and t is a configuration where s and t are 
divided into n and m substrings respectively, such that: 

 
 s = s1 + s2 + ... + sn 
 t = t1 + t2 + ... + tm 
 |n - m| <= 1 
 The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3
 + s3 + ... 
 

 Note: a + b is the concatenation of strings a and b. 

 
 Example 1: 
 
 
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = 
"aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
 

 Example 2: 

 
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string 
to obtain s3.
 

 Example 3: 

 
Input: s1 = "", s2 = "", s3 = ""
Output: true
 

 
 Constraints: 

 
 0 <= s1.length, s2.length <= 100 
 0 <= s3.length <= 200 
 s1, s2, and s3 consist of lowercase English letters. 
 

 
 Follow up: Could you solve it using only O(s2.length) additional memory space? 


 Related Topics String Dynamic Programming 👍 6030 👎 369

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class InterleavingString{
      public static void main(String[] args) {
           Solution solution = new InterleavingString().new Solution();
           solution.isInterleave("aabcc", "dbbca", "aadbbcbcac");
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length())
            return false;
        boolean[] dp = new boolean[s2.length() + 1];
        dp[s2.length()] = true;
        for (int p1 = s1.length(); p1 >= 0; p1--) {
            for (int p2 = s2.length(); p2 >= 0; p2--) {
                if (p1 < s1.length() && dp[p2])
                    dp[p2] = s1.charAt(p1) == s3.charAt(p1 + p2);
                if (p2 < s2.length() && dp[p2 + 1])
                    dp[p2] = s2.charAt(p2) == s3.charAt(p1 + p2);
            }
        }
        return dp[0];
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }