  /**
Given an array nums with n objects colored red, white, or blue, sort them in-
place so that objects of the same color are adjacent, with the colors in the order 
red, white, and blue. 

 We will use the integers 0, 1, and 2 to represent the color red, white, and 
blue, respectively. 

 You must solve this problem without using the library's sort function. 

 
 Example 1: 

 
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
 

 Example 2: 

 
Input: nums = [2,0,1]
Output: [0,1,2]
 

 
 Constraints: 

 
 n == nums.length 
 1 <= n <= 300 
 nums[i] is either 0, 1, or 2. 
 

 
 Follow up: Could you come up with a one-pass algorithm using only constant 
extra space? 

 Related Topics Array Two Pointers Sorting 👍 12651 👎 471

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class SortColors{
      public static void main(String[] args) {
           Solution solution = new SortColors().new Solution();
           solution.sortColors(new int[] {2,0,2,1,1,0});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public void sortColors(int[] nums) {
        int[] count = new int[3];
        for (int num : nums) {
            count[num] = count[num] + 1;
        }

        int startingIndex = 0;
        for (int i = 0; i < count.length; i++) {
            int total = count[i];
            count[i] = startingIndex;
            startingIndex += total;
        }

        int[] sortedNums = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            sortedNums[count[num]] = num;
            count[num] = count[num] + 1;
        }

        for (int i = 0; i < nums.length; i++)
            nums[i] = sortedNums[i];
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }