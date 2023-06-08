  /**
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of 
two given nodes in the BST. 

 According to the definition of LCA on Wikipedia: “The lowest common ancestor 
is defined between two nodes p and q as the lowest node in T that has both p and 
q as descendants (where we allow a node to be a descendant of itself).” 

 
 Example 1: 
 
 
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
 

 Example 2: 
 
 
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of 
itself according to the LCA definition.
 

 Example 3: 

 
Input: root = [2,1], p = 2, q = 1
Output: 2
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [2, 10⁵]. 
 -10⁹ <= Node.val <= 10⁹ 
 All Node.val are unique. 
 p != q 
 p and q will exist in the BST. 
 

 Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 7960 ?
? 235

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeDeserializer;
  import com.shuzijun.leetcode.TreeNode;

  public class LowestCommonAncestorOfABinarySearchTree{
      public static void main(String[] args) {
          Solution solution = new LowestCommonAncestorOfABinarySearchTree().new Solution();
          TreeDeserializer td = new TreeDeserializer();
          TreeNode root = td.deserialize("[6,2,8,0,4,7,9,null,null,3,5]");
          TreeNode p = root.left;
          TreeNode q = p.right;
          solution.lowestCommonAncestor(root, p, q);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        while (true) {
            if (root.val > p.val && root.val > q.val) {
                root = root.left;
            } else if (root.val < p.val && root.val < q.val) {
                root = root.right;
            } else {
                return root;
            }
        }
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }