  /**
Given an integer array nums and an integer k, return the kᵗʰ largest element in 
the array. 

 Note that it is the kᵗʰ largest element in the sorted order, not the kᵗʰ 
distinct element. 

 You must solve it in O(n) time complexity. 

 
 Example 1: 
 Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
 
 Example 2: 
 Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
 
 Constraints: 

 
 1 <= k <= nums.length <= 10⁵ 
 -10⁴ <= nums[i] <= 10⁴ 
 

 Related Topics Array Divide and Conquer Sorting Heap (Priority Queue) 
Quickselect 👍 12167 👎 621

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.Comparator;
  import java.util.PriorityQueue;

  public class KthLargestElementInAnArray{
      public static void main(String[] args) {
           Solution solution = new KthLargestElementInAnArray().new Solution();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int num : nums) {
            minHeap.add(num);
            if (minHeap.size() > k)
                minHeap.poll();
        }
        return minHeap.poll();
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }