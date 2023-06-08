  /**
Given a sorted integer array arr, two integers k and x, return the k closest 
integers to x in the array. The result should also be sorted in ascending order. 

 An integer a is closer to x than an integer b if: 

 
 |a - x| < |b - x|, or 
 |a - x| == |b - x| and a < b 
 

 
 Example 1: 
 Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
 
 Example 2: 
 Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 
 
 Constraints: 

 
 1 <= k <= arr.length 
 1 <= arr.length <= 10⁴ 
 arr is sorted in ascending order. 
 -10⁴ <= arr[i], x <= 10⁴ 
 

 Related Topics Array Two Pointers Binary Search Sliding Window Sorting Heap (
Priority Queue) 👍 6249 👎 511

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class FindKClosestElements{
      public static void main(String[] args) {
           Solution solution = new FindKClosestElements().new Solution();
           solution.findClosestElements(new int[] {1,2,3,4,5}, 4, -1);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int leftIndex = 0, rightIndex = arr.length - 1, middle = 0;
        while (leftIndex <= rightIndex) {
            middle = leftIndex + (rightIndex - leftIndex) / 2;

            if (arr[middle] == x)
                break;

            if (arr[middle] < x)
                leftIndex = middle + 1;
            else
                rightIndex = middle - 1;
        }

        if (arr[middle] > x && middle > 0) {
            if (x - arr[middle - 1] <= arr[middle] - x)
                middle--;
        } else if (arr[middle] < x && middle < arr.length - 1){
            if (arr[middle + 1] - x < x - arr[middle])
                middle++;
        }

        rightIndex = middle;
        leftIndex = middle;
        while (rightIndex - leftIndex + 1 < k) {
            if (leftIndex == 0)
                rightIndex++;
            else if (rightIndex == arr.length - 1)
                leftIndex--;
            else if ((x - arr[leftIndex - 1]) <= (arr[rightIndex + 1] - x))
                leftIndex--;
            else
                rightIndex++;
        }

        List<Integer> res = new ArrayList<>();
        for (int i = leftIndex; i <= rightIndex; i++)
            res.add(arr[i]);

        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }