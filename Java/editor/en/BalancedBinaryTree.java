  /**
Given a binary tree, determine if it is height-balanced. 

 For this problem, a height-balanced binary tree is defined as: 

 
 a binary tree in which the left and right subtrees of every node differ in 
height by no more than 1. 
 

 
 Example 1: 
 
 
Input: root = [3,9,20,null,null,15,7]
Output: true
 

 Example 2: 
 
 
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
 

 Example 3: 

 
Input: root = []
Output: true
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [0, 5000]. 
 -10⁴ <= Node.val <= 10⁴ 
 

 Related Topics Tree Depth-First Search Binary Tree 👍 7472 👎 392

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  public class BalancedBinaryTree{
      public static void main(String[] args) {
           Solution solution = new BalancedBinaryTree().new Solution();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private boolean balanced = true;
    public boolean isBalanced(TreeNode root) {
        height(root);
        return this.balanced;
    }

    private int height(TreeNode current) {
        if (current == null)
            return -1;

        int leftHeight = height(current.left) + 1;
        int rightHeight = height(current.right) + 1;

        if (Math.abs(leftHeight - rightHeight) > 1)
            this.balanced = false;

        return Math.max(leftHeight, rightHeight);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }