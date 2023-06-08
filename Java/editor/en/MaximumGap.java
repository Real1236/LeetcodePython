  /**
Given an integer array nums, return the maximum difference between two 
successive elements in its sorted form. If the array contains less than two elements, 
return 0. 

 You must write an algorithm that runs in linear time and uses linear extra 
space. 

 
 Example 1: 

 
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) 
has the maximum difference 3.
 

 Example 2: 

 
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 

 
 Constraints: 

 
 1 <= nums.length <= 10⁵ 
 0 <= nums[i] <= 10⁹ 
 

 Related Topics Array Sorting Bucket Sort Radix Sort 👍 2486 👎 313

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class MaximumGap{
      public static void main(String[] args) {
           Solution solution = new MaximumGap().new Solution();
           solution.maximumGap(new int[] {15,8,35,7,965,8,435,5,7,6,87,85278});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int maximumGap(int[] nums) {
        if (nums.length < 2)
            return 0;

        int maxNum = -1;
        for (int num : nums)
            maxNum = Math.max(maxNum, num);

        int digit = 1;
        while (maxNum > 0) {
            countingSort(nums, digit);
            digit *= 10;
            maxNum /= 10;
        }

        int maxGap = 0;
        for (int i = 0; i < nums.length - 1; i++)
            maxGap = Math.max(maxGap, nums[i + 1] - nums[i]);

        return maxGap;
    }

    private void countingSort(int[] nums, int digit) {
        int[] count = new int[10];
        for (int num : nums)
            count[(num / digit) % 10]++;

        int index = 0;
        for (int i = 0; i < count.length; i++) {
            int numCount = count[i];
            count[i] = index;
            index += numCount;
        }

        int[] sortedNums = new int[nums.length];
        for (int num : nums) {
            int startIndex = count[(num / digit) % 10]++;
            sortedNums[startIndex] = num;
        }

        for (int i = 0; i < nums.length; i++)
            nums[i] = sortedNums[i];
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }