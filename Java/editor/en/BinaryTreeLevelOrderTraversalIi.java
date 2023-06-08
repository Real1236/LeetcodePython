  /**
Given the root of a binary tree, return the bottom-up level order traversal of 
its nodes' values. (i.e., from left to right, level by level from leaf to root). 


 
 Example 1: 
 
 
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
 

 Example 2: 

 
Input: root = [1]
Output: [[1]]
 

 Example 3: 

 
Input: root = []
Output: []
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [0, 2000]. 
 -1000 <= Node.val <= 1000 
 

 Related Topics Tree Breadth-First Search Binary Tree 👍 3781 👎 299

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  import java.util.*;

  public class BinaryTreeLevelOrderTraversalIi{
      public static void main(String[] args) {
           Solution solution = new BinaryTreeLevelOrderTraversalIi().new Solution();
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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        Stack<List<Integer>> stack = new Stack<>();
        List<List<Integer>> res = new ArrayList<>();

        if (root != null)
            queue.add(root);

        while (!queue.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode current = queue.remove();
                level.add(current.val);

                if (current.left != null)
                    queue.add(current.left);
                if (current.right != null)
                    queue.add(current.right);
            }
            stack.add(level);
        }

        while (!stack.isEmpty()) {
            res.add(stack.pop());
        }

        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }