  /**
Given the root of a binary tree, return the preorder traversal of its nodes' 
values. 

 
 Example 1: 
 
 
Input: root = [1,null,2,3]
Output: [1,2,3]
 

 Example 2: 

 
Input: root = []
Output: []
 

 Example 3: 

 
Input: root = [1]
Output: [1]
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [0, 100]. 
 -100 <= Node.val <= 100 
 

 
 Follow up: Recursive solution is trivial, could you do it iteratively? 

 Related Topics Stack Tree Depth-First Search Binary Tree 👍 4952 👎 139

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  import java.util.ArrayList;
  import java.util.List;
  import java.util.Stack;

  public class BinaryTreePreorderTraversal{
      public static void main(String[] args) {
           Solution solution = new BinaryTreePreorderTraversal().new Solution();
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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode current = stack.pop();
            if (current != null) {
                res.add(current.val);
                stack.push(current.right);
                stack.push(current.left);
            }
        }
        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }