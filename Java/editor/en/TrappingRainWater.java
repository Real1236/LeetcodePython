  /**
Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it can trap after raining. 

 
 Example 1: 
 
 
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,
1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are 
being trapped.
 

 Example 2: 

 
Input: height = [4,2,0,3,2,5]
Output: 9
 

 
 Constraints: 

 
 n == height.length 
 1 <= n <= 2 * 10⁴ 
 0 <= height[i] <= 10⁵ 
 

 Related Topics Array Two Pointers Dynamic Programming Stack Monotonic Stack 👍 
23946 👎 332

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class TrappingRainWater{
      public static void main(String[] args) {
           Solution solution = new TrappingRainWater().new Solution();
           solution.trap(new int[] {0,1,0,2,1,0,1,3,2,1,2,1});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int trap(int[] height) {
        int left = 0, right = 0, leftMax = 0, rightMax = 0, totalWater = 0;

        while (left < height.length) {
            if (height[left] > leftMax) {
                leftMax = height[left++];
                right = left;
                rightMax = height[right];
                break;
            } else {
                left++;
            }
        }
        boolean boundsSet = false;
        while (right < height.length) {
            if (height[right] >= leftMax) {
                rightMax = height[right++];
                boundsSet = true;
            } else {
                right++;
            }
            if (boundsSet) {
                for (int i = left; i < right - 1; i++)
                    totalWater += Math.min(leftMax, rightMax) - height[i];
                leftMax = rightMax;
                left = right;
                boundsSet = false;
            }
        }

//        boolean incrementLeft = true, incrementRight = false;
//        while (right < height.length) {
//            if (incrementLeft) {
//                if (height[left] > leftMax) {
//                    leftMax = height[left++];
//                    right = left;
//                    rightMax = height[right];
//                    incrementLeft = false;
//                    incrementRight = true;
//                } else {
//                    left++;
//                }
//            }
//            if (incrementRight) {
//                if (height[right] > leftMax) {
//                    rightMax = height[right++];
//                    incrementRight = false;
//                } else {
//                    right++;
//                }
//            }
//            if (!incrementLeft && !incrementRight) {
//                for (int i = left; i < right - 1; i++)
//                    totalWater += Math.min(leftMax, rightMax) - height[i];
//                leftMax = rightMax;
//                incrementLeft = true;
//                left = right;
//            }
//        }
        return totalWater;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }