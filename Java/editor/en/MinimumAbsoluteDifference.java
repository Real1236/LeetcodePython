  /**
Given an array of distinct integers arr, find all pairs of elements with the 
minimum absolute difference of any two elements. 

 Return a list of pairs in ascending order(with respect to pairs), each pair [a,
 b] follows 

 
 a, b are from arr 
 a < b 
 b - a equals to the minimum absolute difference of any two elements in arr 
 

 
 Example 1: 

 
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with 
difference equal to 1 in ascending order. 

 Example 2: 

 
Input: arr = [1,3,6,10,15]
Output: [[1,3]]
 

 Example 3: 

 
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
 

 
 Constraints: 

 
 2 <= arr.length <= 10⁵ 
 -10⁶ <= arr[i] <= 10⁶ 
 

 Related Topics Array Sorting 👍 1761 👎 61

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.ArrayList;
  import java.util.Arrays;
  import java.util.List;

  public class MinimumAbsoluteDifference{
      public static void main(String[] args) {
          Solution solution = new MinimumAbsoluteDifference().new Solution();
          solution.minimumAbsDifference(new int[] {3,8,-10,23,19,-4,-14,27});
          solution.minimumAbsDifference(new int[] {0});
          solution.minimumAbsDifference(new int[] {1,0});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
        int minDifference = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length - 1; i++)
            minDifference = Math.min(minDifference, Math.abs(arr[i] - arr[i + 1]));
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < arr.length - 1; i++) {
            if (Math.abs(arr[i] - arr[i + 1]) == minDifference) {
                List<Integer> twoElements = new ArrayList<>();
                twoElements.add(arr[i]);
                twoElements.add(arr[i + 1]);
                res.add(twoElements);
            }
        }
        return res;
    }

    private void quickSort(int[] arr, int start, int end) {
        if (end > start) {
            int partition = partition(arr, start, end);

            if (start < partition)
                quickSort(arr, start, partition);
            if (end > partition + 1)
                quickSort(arr, partition + 1, end);
        }
    }

    private int partition(int[] arr, int left, int right) {
        int pivotValue = arr[(left + right) / 2];

        while (right > left) {
            while (arr[left] < pivotValue)
                left++;
            while (arr[right] > pivotValue)
                right--;

            int temp = arr[right];
            arr[right] = arr[left];
            arr[left] = temp;
        }

        return left;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }