  /**
Given two integer arrays preorder and inorder where preorder is the preorder 
traversal of a binary tree and inorder is the inorder traversal of the same tree, 
construct and return the binary tree. 

 
 Example 1: 
 
 
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
 

 Example 2: 

 
Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

 
 Constraints: 

 
 1 <= preorder.length <= 3000 
 inorder.length == preorder.length 
 -3000 <= preorder[i], inorder[i] <= 3000 
 preorder and inorder consist of unique values. 
 Each value of inorder also appears in preorder. 
 preorder is guaranteed to be the preorder traversal of the tree. 
 inorder is guaranteed to be the inorder traversal of the tree. 
 

 Related Topics Array Hash Table Divide and Conquer Tree Binary Tree 👍 11130 👎
 309

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  import java.util.HashMap;
  import java.util.Map;

  public class ConstructBinaryTreeFromPreorderAndInorderTraversal{
      public static void main(String[] args) {
          Solution solution = new ConstructBinaryTreeFromPreorderAndInorderTraversal().new Solution();
          int[] preorder = {3,9,20,15,7};
          int[] inorder = {9,3,15,20,7};
          solution.buildTree(preorder, inorder);
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
    private int pIndex = 0;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < preorder.length; i++)
            map.put(inorder[i], i);

        TreeNode root = new TreeNode(preorder[this.pIndex++]);

        dfs(preorder, map, root, 0, map.get(root.val) - 1);
        dfs(preorder, map, root, map.get(root.val) + 1, inorder.length - 1);

        return root;
    }

    private void dfs(int[] preorder, Map<Integer, Integer> map, TreeNode parent, int startIndex, int endIndex) {
        if (startIndex > endIndex)
            return;

        TreeNode current = new TreeNode(preorder[this.pIndex++]);
        int nodeIndex = map.get(current.val);

        if (nodeIndex < map.get(parent.val))
            parent.left = current;
        else
            parent.right = current;

        dfs(preorder, map, current, startIndex, nodeIndex - 1);
        dfs(preorder, map, current, nodeIndex + 1, endIndex);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }