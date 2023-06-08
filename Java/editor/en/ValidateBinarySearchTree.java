  /**
Given the root of a binary tree, determine if it is a valid binary search tree (
BST). 

 A valid BST is defined as follows: 

 
 The left subtree of a node contains only nodes with keys less than the node's 
key. 
 The right subtree of a node contains only nodes with keys greater than the 
node's key. 
 Both the left and right subtrees must also be binary search trees. 
 

 
 Example 1: 
 
 
Input: root = [2,1,3]
Output: true
 

 Example 2: 
 
 
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [1, 10⁴]. 
 -2³¹ <= Node.val <= 2³¹ - 1 
 

 Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 12687 
👎 1021

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeDeserializer;
  import com.shuzijun.leetcode.TreeNode;

  public class ValidateBinarySearchTree{
      public static void main(String[] args) {
          Solution solution = new ValidateBinarySearchTree().new Solution();
          TreeDeserializer treeDeserializer = new TreeDeserializer();
          solution.isValidBST(treeDeserializer.deserialize("[-2147483648,null,2147483647]"));
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
    public boolean isValidBST(TreeNode root) {
        return dfs(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean dfs(TreeNode current, long min, long max) {
        if (current == null) return true;

        if (current.val <= min || current.val >= max)
            return false;

        return dfs(current.left, min, current.val) && dfs(current.right, current.val, max);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }