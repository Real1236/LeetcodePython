  /**
Given the roots of two binary trees p and q, write a function to check if they 
are the same or not. 

 Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value. 

 
 Example 1: 
 
 
Input: p = [1,2,3], q = [1,2,3]
Output: true
 

 Example 2: 
 
 
Input: p = [1,2], q = [1,null,2]
Output: false
 

 Example 3: 
 
 
Input: p = [1,2,1], q = [1,1,2]
Output: false
 

 
 Constraints: 

 
 The number of nodes in both trees is in the range [0, 100]. 
 -10⁴ <= Node.val <= 10⁴ 
 

 Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 7234
 👎 153

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeDeserializer;
  import com.shuzijun.leetcode.TreeNode;

  public class SameTree{
      public static void main(String[] args) {
          Solution solution = new SameTree().new Solution();
          TreeDeserializer treeDeserializer = new TreeDeserializer();

          TreeNode p = treeDeserializer.deserialize("[1,2,3,4,5,6,null,8,null,10,11,12,null,14,15]");
          TreeNode q = treeDeserializer.deserialize("[1,2,3,4,5,6,null,8,null,10,11,12,null,14,15]");
          System.out.println(solution.isSameTree(p, q));

          TreeNode p2 = treeDeserializer.deserialize("[1,2,3,4,5,6,null,8,null,10,11,12,null,14,15]");
          TreeNode q2 = treeDeserializer.deserialize("[1,2,3,4,5,6,null,8,null,null,11,12,null,14,15]");
          System.out.println(solution.isSameTree(p2, q2));
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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null)
            return true;

        if (p == null || q == null || p.val != q.val)
            return false;

        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }