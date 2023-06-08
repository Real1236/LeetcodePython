  /**
Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order. 

 
 Example 1: 
 Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
 
 Example 2: 
 Input: nums = [1], k = 1
Output: [1]
 
 
 Constraints: 

 
 1 <= nums.length <= 10⁵ 
 -10⁴ <= nums[i] <= 10⁴ 
 k is in the range [1, the number of unique elements in the array]. 
 It is guaranteed that the answer is unique. 
 

 
 Follow up: Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size. 

 Related Topics Array Hash Table Divide and Conquer Sorting Heap (Priority 
Queue) Bucket Sort Counting Quickselect 👍 11429 👎 425

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class TopKFrequentElements{
      public static void main(String[] args) {
           Solution solution = new TopKFrequentElements().new Solution();
           solution.topKFrequent(new int[] {1,1,1,2,2,3}, 2);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        List<List<Integer>> freq = new ArrayList<>(nums.length + 1);
        for (int i = 0; i < nums.length + 1; i++)
            freq.add(new ArrayList<Integer>());

        for (int n : nums)
            count.put(n, count.getOrDefault(n, 0) + 1);

        for (int n : count.keySet())
            freq.get(count.get(n)).add(n);

        int[] res = new int[k];
        int resIndex = 0;
        for (int i = freq.size() - 1; i >= 0; i--) {
            for (int n : freq.get(i)) {
                res[resIndex++] = n;
                if (resIndex == k)
                    return res;
            }
        }

        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }