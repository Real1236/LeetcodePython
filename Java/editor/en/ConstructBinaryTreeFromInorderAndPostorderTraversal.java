  /**
Given two integer arrays inorder and postorder where inorder is the inorder 
traversal of a binary tree and postorder is the postorder traversal of the same 
tree, construct and return the binary tree. 

 
 Example 1: 
 
 
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
 

 Example 2: 

 
Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

 
 Constraints: 

 
 1 <= inorder.length <= 3000 
 postorder.length == inorder.length 
 -3000 <= inorder[i], postorder[i] <= 3000 
 inorder and postorder consist of unique values. 
 Each value of postorder also appears in inorder. 
 inorder is guaranteed to be the inorder traversal of the tree. 
 postorder is guaranteed to be the postorder traversal of the tree. 
 

 Related Topics Array Hash Table Divide and Conquer Tree Binary Tree 👍 5286 👎 
79

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  import java.util.HashMap;
  import java.util.Map;

  public class ConstructBinaryTreeFromInorderAndPostorderTraversal{
      public static void main(String[] args) {
          Solution solution = new ConstructBinaryTreeFromInorderAndPostorderTraversal().new Solution();
          int[] inorder = {9,3,15,20,7};
          int[] postorder = {9,15,7,20,3};
          solution.buildTree(inorder, postorder);
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
    private Map<Integer, Integer> hm = new HashMap<>(); // Map to keep track of element's index in inorder array
    private int[] postorder;
    private int index; // Index to keep track of current element in postorder

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        this.postorder = postorder;
        this.index = postorder.length - 1;

        // Element as the key and index as their value
        for (int i = 0; i < postorder.length; i++) {
            hm.put(inorder[i], i);
        }

        TreeNode root = new TreeNode(this.postorder[this.index--]);// Build the root node

        // Build the right side
        dfs(root, hm.get(root.val) + 1, postorder.length - 1);

        // Build the left side
        dfs(root, 0, hm.get(root.val) - 1);
        return root;
    }

    private void dfs(TreeNode root, int start, int end) {
        if (start > end)
            return;

        // mid = the root of the current subtree in inorder array
        int curVal = this.postorder[this.index--];
        int mid = hm.get(curVal);

        // Build the root node of the current subtree
        TreeNode cur = new TreeNode(curVal);

        // Determine where to add the current node
        if (hm.get(root.val) < mid) {
            root.right = cur;
        } else {
            root.left = cur;
        }

        // Build the right side
        dfs(cur, mid + 1, end);

        // Build the left side
        dfs(cur, start, mid - 1);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }