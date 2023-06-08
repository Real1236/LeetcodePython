  /**
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree. 

 A height-balanced binary tree is a binary tree in which the depth of the two 
subtrees of every node never differs by more than one. 

 
 Example 1: 
 
 
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

 

 Example 2: 
 
 
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

 
 Constraints: 

 
 1 <= nums.length <= 10⁴ 
 -10⁴ <= nums[i] <= 10⁴ 
 nums is sorted in a strictly increasing order. 
 

 Related Topics Array Divide and Conquer Tree Binary Search Tree Binary Tree 👍 
8314 👎 418

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeDeserializer;
  import com.shuzijun.leetcode.TreeNode;

  public class ConvertSortedArrayToBinarySearchTree{
      public static void main(String[] args) {
          Solution solution = new ConvertSortedArrayToBinarySearchTree().new Solution();
          TreeDeserializer td = new TreeDeserializer();
          System.out.println(td.serialize(solution.sortedArrayToBST(new int[] {-10,-3,0,5,9})));
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
    public TreeNode sortedArrayToBST(int[] nums) {
        return helper(nums, 0, nums.length - 1);
    }

    private TreeNode helper(int[] nums, int start, int end) {
        if (start == end) return new TreeNode(nums[start]);
        else if (start > end) return null;

        int mid = (start + end) / 2;
        TreeNode current = new TreeNode(nums[mid]);
        current.left = helper(nums, start, mid - 1);
        current.right = helper(nums, mid + 1, end);

        return current;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }