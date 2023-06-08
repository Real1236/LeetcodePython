  /**
Given the root of a binary tree, return the zigzag level order traversal of its 
nodes' values. (i.e., from left to right, then right to left for the next level 
and alternate between). 

 
 Example 1: 
 
 
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
 

 Example 2: 

 
Input: root = [1]
Output: [[1]]
 

 Example 3: 

 
Input: root = []
Output: []
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [0, 2000]. 
 -100 <= Node.val <= 100 
 

 Related Topics Tree Breadth-First Search Binary Tree 👍 7264 👎 194

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  import java.util.*;

  public class BinaryTreeZigzagLevelOrderTraversal{
      public static void main(String[] args) {
          Solution solution = new BinaryTreeZigzagLevelOrderTraversal().new Solution();
          TreeNode four = new TreeNode(4);
          TreeNode five = new TreeNode(5);
          TreeNode two = new TreeNode(2, four, null);
          TreeNode three = new TreeNode(3, null, five);
          TreeNode root = new TreeNode(1, two, three);
          solution.zigzagLevelOrder(root);
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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        Stack<TreeNode> currentLevel = new Stack<>();
        Stack<TreeNode> nextLevel = new Stack<>();
        List<List<Integer>> res = new ArrayList<>();
        boolean leftToRight = true;

        if (root != null)
            currentLevel.push(root);

        while (!currentLevel.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int levelSize = currentLevel.size();

            for (int i = 0; i < levelSize; i++) {
                TreeNode current = currentLevel.pop();
                level.add(current.val);

                if (leftToRight) {
                    if (current.left != null)
                        nextLevel.push(current.left);
                    if (current.right != null)
                        nextLevel.push(current.right);
                } else {
                    if (current.right != null)
                        nextLevel.push(current.right);
                    if (current.left != null)
                        nextLevel.push(current.left);
                }
            }

            res.add(level);

            leftToRight = !leftToRight;
            currentLevel = nextLevel;
            nextLevel = new Stack<>();
        }

        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }