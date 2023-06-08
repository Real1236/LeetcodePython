  /**
You are given the root node of a binary search tree (BST) and a value to insert 
into the tree. Return the root node of the BST after the insertion. It is 
guaranteed that the new value does not exist in the original BST. 

 Notice that there may exist multiple valid ways for the insertion, as long as 
the tree remains a BST after insertion. You can return any of them. 

 
 Example 1: 
 
 
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

 

 Example 2: 

 
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
 

 Example 3: 

 
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 

 
 Constraints: 

 
 The number of nodes in the tree will be in the range [0, 10⁴]. 
 -10⁸ <= Node.val <= 10⁸ 
 All the values Node.val are unique. 
 -10⁸ <= val <= 10⁸ 
 It's guaranteed that val does not exist in the original BST. 
 

 Related Topics Tree Binary Search Tree Binary Tree 👍 4057 👎 152

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  public class InsertIntoABinarySearchTree{
      public static void main(String[] args) {
           Solution solution = new InsertIntoABinarySearchTree().new Solution();
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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null)
            return new TreeNode(val);

        if (val < root.val) {
            helper(root.left, root, val, true);
        } else {
            helper(root.right, root, val, false);
        }

        return root;
    }

    private void helper(TreeNode current, TreeNode parent, int val, boolean leftChild) {
        if (current == null) {
            if (leftChild) parent.left = new TreeNode(val);
            else parent.right = new TreeNode(val);
            return;
        }

        if (val < current.val) {
            helper(current.left, current, val, true);
        } else {
            helper(current.right, current, val, false);
        }
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }