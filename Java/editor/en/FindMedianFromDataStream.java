  /**
The median is the middle value in an ordered integer list. If the size of the 
list is even, there is no middle value and the median is the mean of the two 
middle values. 

 
 For example, for arr = [2,3,4], the median is 3. 
 For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5. 
 

 Implement the MedianFinder class: 

 
 MedianFinder() initializes the MedianFinder object. 
 void addNum(int num) adds the integer num from the data stream to the data 
structure. 
 double findMedian() returns the median of all elements so far. Answers within 1
0⁻⁵ of the actual answer will be accepted. 
 

 
 Example 1: 

 
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

 
 Constraints: 

 
 -10⁵ <= num <= 10⁵ 
 There will be at least one element in the data structure before calling 
findMedian. 
 At most 5 * 10⁴ calls will be made to addNum and findMedian. 
 

 
 Follow up: 

 
 If all integer numbers from the stream are in the range [0, 100], how would 
you optimize your solution? 
 If 99% of all integer numbers from the stream are in the range [0, 100], how 
would you optimize your solution? 
 

 Related Topics Two Pointers Design Sorting Heap (Priority Queue) Data Stream 👍
 8427 👎 152

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.ArrayList;
  import java.util.Comparator;
  import java.util.List;
  import java.util.PriorityQueue;

  public class FindMedianFromDataStream{
      public static void main(String[] args) {
          MedianFinder solution = new FindMedianFromDataStream().new MedianFinder();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class MedianFinder {
    private final PriorityQueue<Integer> smallHeap;
    private final PriorityQueue<Integer> largeHeap;

    public MedianFinder() {
        this.smallHeap = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2 - o1;
            }
        });
        this.largeHeap = new PriorityQueue<>();
    }

    public void addNum(int num) {
        this.largeHeap.offer(num);
        this.smallHeap.offer(this.largeHeap.poll());
        if (this.smallHeap.size() - this.largeHeap.size() > 1)
            this.largeHeap.offer(this.smallHeap.poll());
    }
    
    public double findMedian() {
        if (this.smallHeap.size() == this.largeHeap.size())
             return (double) (this.smallHeap.peek() + this.largeHeap.peek()) / 2;

        return (double) this.smallHeap.peek();
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
//leetcode submit region end(Prohibit modification and deletion)

  }