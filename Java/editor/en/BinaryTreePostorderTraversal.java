  /**
Given the root of a binary tree, return the postorder traversal of its nodes' 
values. 

 
 Example 1: 
 
 
Input: root = [1,null,2,3]
Output: [3,2,1]
 

 Example 2: 

 
Input: root = []
Output: []
 

 Example 3: 

 
Input: root = [1]
Output: [1]
 

 
 Constraints: 

 
 The number of the nodes in the tree is in the range [0, 100]. 
 -100 <= Node.val <= 100 
 

 
Follow up: Recursive solution is trivial, could you do it iteratively?

 Related Topics Stack Tree Depth-First Search Binary Tree 👍 4945 👎 153

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  import java.util.ArrayList;
  import java.util.List;
  import java.util.Stack;

  public class BinaryTreePostorderTraversal{
      public static void main(String[] args) {
          Solution solution = new BinaryTreePostorderTraversal().new Solution();
          TreeNode three = new TreeNode(3);
          TreeNode four = new TreeNode(4);
          TreeNode five = new TreeNode(5);
          TreeNode two = new TreeNode(2, three, four);
          TreeNode one = new TreeNode(1, two, five);
          solution.postorderTraversal(one);
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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        Stack<TreeNode> finalStack = new Stack<>();

        if (root == null) {
            return res;
        }

        stack.push(root);
        while(!stack.isEmpty()) {
            TreeNode current = stack.pop();
            finalStack.push(current);

            if (current.left != null)
                stack.push(current.left);

            if (current.right != null)
                stack.push(current.right);
        }
        while(!finalStack.isEmpty()) {
            res.add(finalStack.pop().val);
        }

        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }