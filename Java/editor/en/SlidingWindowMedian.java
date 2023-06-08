  /**
The median is the middle value in an ordered integer list. If the size of the 
list is even, there is no middle value. So the median is the mean of the two 
middle values. 

 
 For examples, if arr = [2,3,4], the median is 3. 
 For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5. 
 

 You are given an integer array nums and an integer k. There is a sliding 
window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves 
right by one position. 

 Return the median array for each window in the original array. Answers within 1
0⁻⁵ of the actual value will be accepted. 

 
 Example 1: 

 
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
 

 Example 2: 

 
Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
 

 
 Constraints: 

 
 1 <= k <= nums.length <= 10⁵ 
 -2³¹ <= nums[i] <= 2³¹ - 1 
 

 Related Topics Array Hash Table Sliding Window Heap (Priority Queue) 👍 2526 👎
 147

*/
  
  package com.shuzijun.leetcode.editor.en;

  import javax.print.attribute.standard.Media;
  import java.util.*;

  public class SlidingWindowMedian{
      public static void main(String[] args) {
           Solution solution = new SlidingWindowMedian().new Solution();
           solution.medianSlidingWindow(new int[] {1,3,-1,-3,5,3,6,7}, 3);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        double[] res = new double[nums.length + 1 - k];

        MedianFinder dataStream = new MedianFinder();
        for (int i = 0; i < nums.length; i++) {
            dataStream.addNum(nums[i]);

            if (dataStream.getSize() > k)
                dataStream.deleteNum(nums[i - k]);

            if (dataStream.getSize() == k)
                res[i - k + 1] = dataStream.findMedian();
        }

        return res;
    }
}

class MedianFinder {
    private final PriorityQueue<Integer> smallHeap;
    private final PriorityQueue<Integer> largeHeap;
    private Map<Integer, Integer> deleteMap;
    private int size;

    public MedianFinder() {
        this.smallHeap = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2.compareTo(o1);
            }
        });
        this.largeHeap = new PriorityQueue<>();
        this.deleteMap = new HashMap<>();
        this.size = 0;
    }

    public void addNum(int num) {
        this.size++;
        this.largeHeap.offer(num);
        this.smallHeap.offer(this.largeHeap.poll());
        rebalance();
    }

    public double findMedian() {
        while (this.deleteMap.containsKey(this.smallHeap.peek())) {
            removeFromMap(this.smallHeap.poll());
            rebalance();
        }
        while (this.deleteMap.containsKey(this.largeHeap.peek())) {
            removeFromMap(this.largeHeap.poll());
            rebalance();
        }

        if (this.size < this.smallHeap.size() + this.largeHeap.size()) {
            for (int num : this.deleteMap.keySet()) {
                if (num < this.smallHeap.peek()) {
                    this.smallHeap.remove(num);
                    removeFromMap(num);
                } else {
                    this.largeHeap.remove(num);
                    removeFromMap(num);
                }
            }
            rebalance();
        }

        if (this.smallHeap.size() == this.largeHeap.size())
            return ((double) this.smallHeap.peek() + (double) this.largeHeap.peek()) / 2;

        return (double) this.smallHeap.peek();
    }

    public void deleteNum(int num) {
        this.size--;
        this.deleteMap.put(num, this.deleteMap.getOrDefault(num, 0) + 1);
    }

    public int getSize() {
        return size;
    }

    private void rebalance() {
        while (this.largeHeap.size() > this.smallHeap.size())
            this.smallHeap.offer(this.largeHeap.poll());

        while (this.smallHeap.size() - this.largeHeap.size() > 1)
            this.largeHeap.offer(this.smallHeap.poll());
    }

    private void removeFromMap(int toBeDeleted) {
        if (this.deleteMap.get(toBeDeleted) > 1)
            this.deleteMap.put(toBeDeleted, this.deleteMap.get(toBeDeleted) - 1);
        else
            this.deleteMap.remove(toBeDeleted);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }