  /**
Given the root of a binary tree, return the inorder traversal of its nodes' 
values. 

 
 Example 1: 
 
 
Input: root = [1,null,2,3]
Output: [1,3,2]
 

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

 Related Topics Stack Tree Depth-First Search Binary Tree 👍 9572 👎 453

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeDeserializer;
  import com.shuzijun.leetcode.TreeNode;

  import java.util.ArrayList;
  import java.util.List;
  import java.util.Stack;

  public class BinaryTreeInorderTraversal{
      public static void main(String[] args) {
          Solution solution = new BinaryTreeInorderTraversal().new Solution();
          TreeDeserializer td = new TreeDeserializer();
          solution.inorderTraversal(td.deserialize("[1,null,2,3]"));
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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;

        while (current != null || !stack.isEmpty()) {
            while (current != null) {
                stack.push(current);
                current = current.left;
            }

            current = stack.pop();
            res.add(current.val);
            current = current.right;
        }

        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }