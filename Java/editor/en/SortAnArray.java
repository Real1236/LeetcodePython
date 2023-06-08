  /**
Given an array of integers nums, sort the array in ascending order and return 
it. 

 You must solve the problem without using any built-in functions in O(nlog(n)) 
time complexity and with the smallest space complexity possible. 

 
 Example 1: 

 
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not 
changed (for example, 2 and 3), while the positions of other numbers are changed (
for example, 1 and 5).
 

 Example 2: 

 
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

 
 Constraints: 

 
 1 <= nums.length <= 5 * 10⁴ 
 -5 * 10⁴ <= nums[i] <= 5 * 10⁴ 
 

 Related Topics Array Divide and Conquer Sorting Heap (Priority Queue) Merge 
Sort Bucket Sort Radix Sort Counting Sort 👍 2863 👎 575

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class SortAnArray{
      public static void main(String[] args) {
           Solution solution = new SortAnArray().new Solution();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int[] sortArray(int[] nums) {
        for (int i = nums.length / 2 - 1; i >= 0; i--) {
            heapify(nums, nums.length, i);
        }

        for (int i = nums.length - 1; i > 0; i--) {
            int temp = nums[0];
            nums[0] = nums[i];
            nums[i] = temp;
            heapify(nums, i, 0);
        }

        return nums;
    }

    private void heapify(int[] nums, int heapSize, int index) {
        int lcIndex = index * 2 + 1;
        int rcIndex = index * 2 + 2;
        int largestNumIndex = index;

        if (lcIndex < heapSize && nums[largestNumIndex] < nums[lcIndex])
            largestNumIndex = lcIndex;
        if (rcIndex < heapSize && nums[largestNumIndex] < nums[rcIndex])
            largestNumIndex = rcIndex;

        if (largestNumIndex != index) {
            int temp = nums[largestNumIndex];
            nums[largestNumIndex] = nums[index];
            nums[index] = temp;
            heapify(nums, heapSize, largestNumIndex);
        }
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }