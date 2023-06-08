  /**
Given the root of a binary tree, return the level order traversal of its nodes' 
values. (i.e., from left to right, level by level). 

 
 Example 1: 
 
 
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
 

 Example 2: 

 
Input: root = [1]
Output: [[1]]
 

 Example 3: 

 
Input: root = []
Output: []
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [0, 2000]. 
 -1000 <= Node.val <= 1000 
 

 Related Topics Tree Breadth-First Search Binary Tree 👍 10839 👎 202

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  import java.util.*;

  public class BinaryTreeLevelOrderTraversal{
      public static void main(String[] args) {
          Solution solution = new BinaryTreeLevelOrderTraversal().new Solution();
          TreeNode fifteen = new TreeNode(15);
          TreeNode seven = new TreeNode(7);
          TreeNode twenty = new TreeNode(20, fifteen, seven);
          TreeNode five = new TreeNode(5);
          TreeNode four = new TreeNode(4);
          TreeNode nine = new TreeNode(9, five, four);
          TreeNode three = new TreeNode(3, nine, twenty);
          solution.levelOrder(three);
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
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
            res.add(level);
        }

        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }