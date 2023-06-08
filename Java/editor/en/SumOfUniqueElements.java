  /**
You are given an integer array nums. The unique elements of an array are the 
elements that appear exactly once in the array. 

 Return the sum of all the unique elements of nums. 

 
 Example 1: 

 
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
 

 Example 2: 

 
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
 

 Example 3: 

 
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
 

 
 Constraints: 

 
 1 <= nums.length <= 100 
 1 <= nums[i] <= 100 
 

 Related Topics Array Hash Table Counting 👍 958 👎 21

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class SumOfUniqueElements{
      public static void main(String[] args) {
           Solution solution = new SumOfUniqueElements().new Solution();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int sumOfUnique(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums)
            count.put(num, count.getOrDefault(num, 0) + 1);

        int sum = 0;
        for (int num : count.keySet()) {
            if (count.get(num) == 1)
                sum += num;
        }
        return sum;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }