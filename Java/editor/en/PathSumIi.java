  /**
Given the root of a binary tree and an integer targetSum, return all root-to-
leaf paths where the sum of the node values in the path equals targetSum. Each 
path should be returned as a list of the node values, not node references. 

 A root-to-leaf path is a path starting from the root and ending at any leaf 
node. A leaf is a node with no children. 

 
 Example 1: 
 
 
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
 

 Example 2: 
 
 
Input: root = [1,2,3], targetSum = 5
Output: []
 

 Example 3: 

 
Input: root = [1,2], targetSum = 0
Output: []
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [0, 5000]. 
 -1000 <= Node.val <= 1000 
 -1000 <= targetSum <= 1000 
 

 Related Topics Backtracking Tree Depth-First Search Binary Tree 👍 6259 👎 132

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  import java.util.ArrayList;
  import java.util.List;

  public class PathSumIi{
      public static void main(String[] args) {
          Solution solution = new PathSumIi().new Solution();

          TreeNode seven = new TreeNode(7);
          TreeNode two = new TreeNode(2);
          TreeNode five = new TreeNode(5);
          TreeNode one = new TreeNode(1);

          TreeNode eleven = new TreeNode(11, seven, two);
          TreeNode thirteen = new TreeNode(13);
          TreeNode fourL3 = new TreeNode(4, five, one);

          TreeNode fourL2 = new TreeNode(4, eleven, null);
          TreeNode eight = new TreeNode(8, thirteen, fourL3);

          TreeNode root = new TreeNode(5, fourL2, eight);

          solution.pathSum(root, 22);
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
    private List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        dfs(root, targetSum, new ArrayList<>());
        return this.res;
    }

    private void dfs(TreeNode current, int currentSum, List<Integer> path) {
        if (current == null)
            return;

        currentSum -= current.val;
        path.add(current.val);

        if (current.left == null && current.right == null && currentSum == 0)
            this.res.add(new ArrayList<>(path));

        dfs(current.left, currentSum, path);
        dfs(current.right, currentSum, path);

        path.remove(path.size() - 1);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }