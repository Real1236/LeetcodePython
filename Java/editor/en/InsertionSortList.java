  /**
Given the head of a singly linked list, sort the list using insertion sort, and 
return the sorted list's head. 

 The steps of the insertion sort algorithm: 

 
 Insertion sort iterates, consuming one input element each repetition and 
growing a sorted output list. 
 At each iteration, insertion sort removes one element from the input data, 
finds the location it belongs within the sorted list and inserts it there. 
 It repeats until no input elements remain. 
 

 The following is a graphical example of the insertion sort algorithm. The 
partially sorted list (black) initially contains only the first element in the list. 
One element (red) is removed from the input data and inserted in-place into the 
sorted list with each iteration. 
 
 
 Example 1: 
 
 
Input: head = [4,2,1,3]
Output: [1,2,3,4]
 

 Example 2: 
 
 
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
 

 
 Constraints: 

 
 The number of nodes in the list is in the range [1, 5000]. 
 -5000 <= Node.val <= 5000 
 

 Related Topics Linked List Sorting 👍 2324 👎 814

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.ListNode;

  public class InsertionSortList{
      public static void main(String[] args) {
          Solution solution = new InsertionSortList().new Solution();
          ListNode four = new ListNode(0);
          ListNode three = new ListNode(4, four);
          ListNode one = new ListNode(3, three);
          ListNode two = new ListNode(5, one);
          ListNode head = new ListNode(-1, two);
          solution.insertionSortList(head);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode lastSortedNode = head;
        while (lastSortedNode.next != null) {
            if (lastSortedNode.val <= lastSortedNode.next.val) {
                lastSortedNode = lastSortedNode.next;
                continue;
            }

            ListNode nodeToBeSorted = lastSortedNode.next;
            ListNode prevInsert = null;
            ListNode insert = head;
            boolean replaceHead = true;
            while (nodeToBeSorted.val > insert.val) {
                prevInsert = insert;
                insert = insert.next;
                replaceHead = false;
            }

            if (nodeToBeSorted.equals(insert)) {
                lastSortedNode = nodeToBeSorted;
                continue;
            }
            
            lastSortedNode.next = nodeToBeSorted.next;
            nodeToBeSorted.next = insert;

            if (replaceHead)
                head = nodeToBeSorted;
            else
                prevInsert.next = nodeToBeSorted;
        }

        return head;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }