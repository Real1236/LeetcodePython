  /**
Given the head of a singly linked list, reverse the list, and return the 
reversed list. 

 
 Example 1: 
 
 
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
 

 Example 2: 
 
 
Input: head = [1,2]
Output: [2,1]
 

 Example 3: 

 
Input: head = []
Output: []
 

 
 Constraints: 

 
 The number of nodes in the list is the range [0, 5000]. 
 -5000 <= Node.val <= 5000 
 

 
 Follow up: A linked list can be reversed either iteratively or recursively. 
Could you implement both? 

 Related Topics Linked List Recursion 👍 14297 👎 247

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.ListNode;

  public class ReverseLinkedList{
      public static void main(String[] args) {
           Solution solution = new ReverseLinkedList().new Solution();
           ListNode listNode1 = new ListNode(1);
           ListNode listNode2 = new ListNode(2);
           ListNode listNode3 = new ListNode(3);
           ListNode listNode4 = new ListNode(4);
           ListNode listNode5 = new ListNode(5);
           ListNode listNode6 = new ListNode(6);
           listNode1.next = listNode2;
           listNode2.next = listNode3;
           listNode3.next = listNode4;
           listNode4.next = listNode5;
           listNode5.next = listNode6;
           System.out.println(solution.reverseList(listNode1));
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
    public ListNode reverseList(ListNode head) {
        return reverse(head, null);
    }

    private ListNode reverse(ListNode node, ListNode prevNode) {
        if (node == null) {
            return prevNode;
        }
        ListNode nextNode = node.next;
        node.next = prevNode;
        return reverse(nextNode, node);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }