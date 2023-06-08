  /**
Given an integer rowIndex, return the rowIndexᵗʰ (0-indexed) row of the 
Pascal's triangle. 

 In Pascal's triangle, each number is the sum of the two numbers directly above 
it as shown: 
 
 
 Example 1: 
 Input: rowIndex = 3
Output: [1,3,3,1]
 
 Example 2: 
 Input: rowIndex = 0
Output: [1]
 
 Example 3: 
 Input: rowIndex = 1
Output: [1,1]
 
 
 Constraints: 

 
 0 <= rowIndex <= 33 
 

 
 Follow up: Could you optimize your algorithm to use only O(rowIndex) extra 
space? 

 Related Topics Array Dynamic Programming 👍 3105 👎 279

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.ArrayList;
  import java.util.List;

  public class PascalsTriangleIi{
      public static void main(String[] args) {
           Solution solution = new PascalsTriangleIi().new Solution();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<>();

        if (rowIndex == 0) {
            res.add(1);
            return res;
        }

        List<Integer> aboveRow = getRow(rowIndex - 1);

        for (int i = 0; i <= rowIndex; i++) {
            if (i == 0 || i == rowIndex)
                res.add(1);
            else
                res.add(aboveRow.get(i - 1) + aboveRow.get(i));
        }

        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }