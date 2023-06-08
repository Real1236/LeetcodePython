  /**
You are given two 0-indexed strings s and target. You can take some letters 
from s and rearrange them to form new strings. 

 Return the maximum number of copies of target that can be formed by taking 
letters from s and rearranging them. 

 
 Example 1: 

 
Input: s = "ilovecodingonleetcode", target = "code"
Output: 2
Explanation:
For the first copy of "code", take the letters at indices 4, 5, 6, and 7.
For the second copy of "code", take the letters at indices 17, 18, 19, and 20.
The strings that are formed are "ecod" and "code" which can both be rearranged 
into "code".
We can make at most two copies of "code", so we return 2.
 

 Example 2: 

 
Input: s = "abcba", target = "abc"
Output: 1
Explanation:
We can make one copy of "abc" by taking the letters at indices 0, 1, and 2.
We can make at most one copy of "abc", so we return 1.
Note that while there is an extra 'a' and 'b' at indices 3 and 4, we cannot 
reuse the letter 'c' at index 2, so we cannot make a second copy of "abc".
 

 Example 3: 

 
Input: s = "abbaccaddaeea", target = "aaaaa"
Output: 1
Explanation:
We can make one copy of "aaaaa" by taking the letters at indices 0, 3, 6, 9, 
and 12.
We can make at most one copy of "aaaaa", so we return 1.
 

 
 Constraints: 

 
 1 <= s.length <= 100 
 1 <= target.length <= 10 
 s and target consist of lowercase English letters. 
 

 Related Topics Hash Table String Counting 👍 272 👎 21

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.HashMap;
  import java.util.Map;

  public class RearrangeCharactersToMakeTargetString{
      public static void main(String[] args) {
           Solution solution = new RearrangeCharactersToMakeTargetString().new Solution();
           solution.rearrangeCharacters("abc", "abcd");
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int rearrangeCharacters(String s, String target) {
        Map<Character, Integer> count = new HashMap<>();
        for (int i = 0; i < target.length(); i++)
            count.put(target.charAt(i), count.getOrDefault(target.charAt(i), 0) + 1);

        Map<Character, Integer> sCount = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            if (count.containsKey(current))
                sCount.put(current, sCount.getOrDefault(current, 0) + 1);
        }

        int res = Integer.MAX_VALUE;
        for (int i = 0; i < target.length(); i++)
            res = Math.min(res, sCount.getOrDefault(target.charAt(i), 0) / count.get(target.charAt(i)));

        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }