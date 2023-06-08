  /**
Design a class to find the kᵗʰ largest element in a stream. Note that it is the 
kᵗʰ largest element in the sorted order, not the kᵗʰ distinct element. 

 Implement KthLargest class: 

 
 KthLargest(int k, int[] nums) Initializes the object with the integer k and 
the stream of integers nums. 
 int add(int val) Appends the integer val to the stream and returns the element 
representing the kᵗʰ largest element in the stream. 
 

 
 Example 1: 

 
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
 

 
 Constraints: 

 
 1 <= k <= 10⁴ 
 0 <= nums.length <= 10⁴ 
 -10⁴ <= nums[i] <= 10⁴ 
 -10⁴ <= val <= 10⁴ 
 At most 10⁴ calls will be made to add. 
 It is guaranteed that there will be at least k elements in the array when you 
search for the kᵗʰ element. 
 

 Related Topics Tree Design Binary Search Tree Heap (Priority Queue) Binary 
Tree Data Stream 👍 3512 👎 2044

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.Comparator;
  import java.util.PriorityQueue;

  public class KthLargestElementInAStream{
      public static void main(String[] args) {
//          KthLargest obj = new KthLargest(3, new int[] {4,5,8,2});
//          int param_1 = obj.add(3);
//          int param_2 = obj.add(5);
//          int param_3 = obj.add(10);
//          int param_4 = obj.add(9);
//          int param_5 = obj.add(4);
//          System.out.println(param_1);
//          System.out.println(param_2);
//          System.out.println(param_3);
//          System.out.println(param_4);
//          System.out.println(param_5);
      }
      //leetcode submit region begin(Prohibit modification and deletion)

  class KthLargest {
      private final PriorityQueue<Integer> minHeap;
      private final int k;

      public KthLargest(int k, int[] nums) {
          this.minHeap = new PriorityQueue<>(k);
          this.k = k;
          for (int num : nums) {
              add(num);
          }
      }

      public int add(int val) {
          if (this.minHeap.size() < k) {
              this.minHeap.offer(val);
          } else if (val > this.minHeap.peek()) {
              this.minHeap.poll();
              this.minHeap.offer(val);
          }
          return this.minHeap.peek();
      }
  }

  /**
   * Your KthLargest object will be instantiated and called as such:
   * KthLargest obj = new KthLargest(k, nums);
   * int param_1 = obj.add(val);
   */
  //leetcode submit region end(Prohibit modification and deletion)

  }