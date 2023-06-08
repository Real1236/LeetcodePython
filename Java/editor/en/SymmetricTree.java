  /**
Given the root of a binary tree, check whether it is a mirror of itself (i.e., 
symmetric around its center). 

 
 Example 1: 
 
 
Input: root = [1,2,2,3,4,4,3]
Output: true
 

 Example 2: 
 
 
Input: root = [1,2,2,null,3,null,3]
Output: false
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [1, 1000]. 
 -100 <= Node.val <= 100 
 

 
Follow up: Could you solve it both recursively and iteratively?

 Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 1108
6 👎 253

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  public class SymmetricTree{
      public static void main(String[] args) {
           Solution solution = new SymmetricTree().new Solution();
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
    public boolean isSymmetric(TreeNode root) {
        return helper(root.left, root.right);
    }

    private boolean helper(TreeNode left, TreeNode right) {
        // if both nodes exist, code continues. otherwise checks that both nodes are null
        if (left == null || right == null) {
            return left == right;
        }

        if (left.val != right.val) {
            return false;
        }

        boolean outsideSymmetry = helper(left.left, right.right);
        boolean insideSymmetry = helper(left.right, right.left);

        return outsideSymmetry && insideSymmetry;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }