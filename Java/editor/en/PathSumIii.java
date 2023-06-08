  /**
Given the root of a binary tree and an integer targetSum, return the number of 
paths where the sum of the values along the path equals targetSum. 

 The path does not need to start or end at the root or a leaf, but it must go 
downwards (i.e., traveling only from parent nodes to child nodes). 

 
 Example 1: 
 
 
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
 

 Example 2: 

 
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [0, 1000]. 
 -10⁹ <= Node.val <= 10⁹ 
 -1000 <= targetSum <= 1000 
 

 Related Topics Tree Depth-First Search Binary Tree 👍 8664 👎 413

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  import java.util.HashMap;
  import java.util.Map;

  public class PathSumIii{
      public static void main(String[] args) {
          Solution solution = new PathSumIii().new Solution();

//          TreeNode three = new TreeNode(3);
//          TreeNode nTwo = new TreeNode(-2);
//          TreeNode one = new TreeNode(1);
//
//          TreeNode threeD2 = new TreeNode(3, three, nTwo);
//          TreeNode two = new TreeNode(2, null, one);
//          TreeNode eleven = new TreeNode(11);
//
//          TreeNode five = new TreeNode(5, threeD2, two);
//          TreeNode nThree = new TreeNode(-3, null, eleven);
//
//          TreeNode ten = new TreeNode(10, five, nThree);

          TreeNode six = new TreeNode(1000000000);
          TreeNode five = new TreeNode(1000000000, six, null);
          TreeNode four = new TreeNode(1000000000, five, null);
          TreeNode three = new TreeNode(294967296, four, null);
          TreeNode two = new TreeNode(1000000000, three, null);
          TreeNode root = new TreeNode(1000000000, two, null);

          System.out.println(solution.pathSum(root, 0));
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
    public int pathSum(TreeNode root, int sum) {
        Map<Long, Integer> prefixSum = new HashMap<>();
        prefixSum.put((long) 0, 1);
        return (int) dfs(root, 0, sum, prefixSum);
    }

    private long dfs(TreeNode current, long currentSum, int target, Map<Long, Integer> prefixSum) {
        if (current == null)
            return 0;

        currentSum += current.val;
        long counter = prefixSum.getOrDefault(currentSum - target, 0);
        prefixSum.put(currentSum, prefixSum.getOrDefault(currentSum, 0) + 1);

        long leftCounter = dfs(current.left, currentSum, target, prefixSum);
        long rightCounter = dfs(current.right, currentSum, target, prefixSum);
        counter += leftCounter + rightCounter;

        prefixSum.put(currentSum, prefixSum.get(currentSum) - 1);

        return counter;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }