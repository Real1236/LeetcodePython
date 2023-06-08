  /**
You are given a 0-indexed array of strings nums, where each string is of equal 
length and consists of only digits. 

 You are also given a 0-indexed 2D integer array queries where queries[i] = [ki,
 trimi]. For each queries[i], you need to: 

 
 Trim each number in nums to its rightmost trimi digits. 
 Determine the index of the kiᵗʰ smallest trimmed number in nums. If two 
trimmed numbers are equal, the number with the lower index is considered to be smaller.
 
 Reset each number in nums to its original length. 
 

 Return an array answer of the same length as queries, where answer[i] is the 
answer to the iᵗʰ query. 

 Note: 

 
 To trim to the rightmost x digits means to keep removing the leftmost digit, 
until only x digits remain. 
 Strings in nums may contain leading zeros. 
 

 
 Example 1: 

 
Input: nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]
Output: [2,2,1,0]
Explanation:
1. After trimming to the last digit, nums = ["2","3","1","4"]. The smallest 
number is 1 at index 2.
2. Trimmed to the last 3 digits, nums is unchanged. The 2ⁿᵈ smallest number is 2
51 at index 2.
3. Trimmed to the last 2 digits, nums = ["02","73","51","14"]. The 4ᵗʰ smallest 
number is 73.
4. Trimmed to the last 2 digits, the smallest number is 2 at index 0.
   Note that the trimmed number "02" is evaluated as 2.
 

 Example 2: 

 
Input: nums = ["24","37","96","04"], queries = [[2,1],[2,2]]
Output: [3,0]
Explanation:
1. Trimmed to the last digit, nums = ["4","7","6","4"]. The 2ⁿᵈ smallest number 
is 4 at index 3.
   There are two occurrences of 4, but the one at index 0 is considered smaller 
than the one at index 3.
2. Trimmed to the last 2 digits, nums is unchanged. The 2ⁿᵈ smallest number is 2
4.
 

 
 Constraints: 

 
 1 <= nums.length <= 100 
 1 <= nums[i].length <= 100 
 nums[i] consists of only digits. 
 All nums[i].length are equal. 
 1 <= queries.length <= 100 
 queries[i].length == 2 
 1 <= ki <= nums.length 
 1 <= trimi <= nums[i].length 
 

 
 Follow up: Could you use the Radix Sort Algorithm to solve this problem? What 
will be the complexity of that solution? 

 Related Topics Array String Divide and Conquer Sorting Heap (Priority Queue) 
Radix Sort Quickselect 👍 179 👎 342

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class QueryKthSmallestTrimmedNumber{
      public static void main(String[] args) {
          Solution solution = new QueryKthSmallestTrimmedNumber().new Solution();
          // Test 1
          //solution.smallestTrimmedNumbers(new String[] {"102","473","251","814"},
          //                                 new int[][] {{1,1},{2,3},{4,2},{1,2}});
          // Test 2
          solution.smallestTrimmedNumbers(new String[] {"9415","5908","1840","5307"},
                  new int[][] {{3,2},{2,2},{3,3},{1,3}});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    private void radixSort(String[] arr, Map<Integer, int[]> trimmedNums) {
        String[] newArr = Arrays.copyOf(arr, arr.length);
        int maxDigits = arr[0].length();
        for (int i = 0; i < maxDigits; i++)
            countingSort(arr, newArr, i, trimmedNums);
    }

    private void countingSort(String[] arr, String[] newArr, int digitFromRight,
                              Map<Integer, int[]> trimmedNums) {
        int[] counts = new int[10];
        int digitFromLeft = arr[0].length() - 1 - digitFromRight;
        Map<String, Queue<Integer>> arrIndices = new HashMap<>();

        for (int i = 0; i < arr.length; i++) {
            if (arrIndices.get(arr[i].substring(digitFromLeft)) == null) {
                Queue<Integer> queue = new LinkedList<>();
                queue.offer(i);
                arrIndices.put(arr[i].substring(digitFromLeft), queue);
            } else {
                arrIndices.get(arr[i].substring(digitFromLeft)).offer(i);
            }
            int numAtDigit = Character.getNumericValue(newArr[i].charAt(digitFromLeft));
            counts[numAtDigit]++;
        }

        int startingIndex = 0;
        for (int i = 0; i < counts.length; i++) {
            int count = counts[i];
            counts[i] = startingIndex;
            startingIndex += count;
        }

        String[] sortedDigit = new String[arr.length];
        for (int i = 0; i < arr.length; i++) {
            int numAtDigit = Character.getNumericValue(newArr[i].charAt(digitFromLeft));
            String trimmedNum = newArr[i].substring(digitFromLeft);
            sortedDigit[counts[numAtDigit]] = trimmedNum;
            counts[numAtDigit]++;
        }

        int[] sortedIndices = new int[sortedDigit.length];
        String[] updatedArr = new String[arr.length];
        for (int i = 0; i < sortedIndices.length; i++) {
            updatedArr[i] = arr[arrIndices.get(sortedDigit[i]).peek()];
            sortedIndices[i] = arrIndices.get(sortedDigit[i]).poll();
        }

        for (int i = 0; i < newArr.length; i++)
            newArr[i] = updatedArr[i];

        trimmedNums.put(digitFromRight + 1, sortedIndices);
    }

    public int[] smallestTrimmedNumbers(String[] nums, int[][] queries) {
        Map<Integer, int[]> trimmedNums = new HashMap<>();
        radixSort(nums, trimmedNums);
        int[] res = new int[queries.length];
        for (int i = 0; i < res.length; i++) {
            int k = queries[i][0];
            int trim = queries[i][1];
            res[i] = trimmedNums.get(trim)[k - 1];
        }
        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }