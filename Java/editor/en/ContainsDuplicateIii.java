  /**
You are given an integer array nums and two integers indexDiff and valueDiff. 

 Find a pair of indices (i, j) such that: 

 
 i != j, 
 abs(i - j) <= indexDiff. 
 abs(nums[i] - nums[j]) <= valueDiff, and 
 

 Return true if such pair exists or false otherwise. 

 
 Example 1: 

 
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
 

 Example 2: 

 
Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the 
three conditions, so we return false.
 

 
 Constraints: 

 
 2 <= nums.length <= 10⁵ 
 -10⁹ <= nums[i] <= 10⁹ 
 1 <= indexDiff <= nums.length 
 0 <= valueDiff <= 10⁹ 
 

 Related Topics Array Sliding Window Sorting Bucket Sort Ordered Set 👍 120 👎 2


*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  import java.util.TreeSet;

  public class ContainsDuplicateIii{
      public static void main(String[] args) {
          Solution solution = new ContainsDuplicateIii().new Solution();
          solution.containsNearbyAlmostDuplicate(new int[] {1,5,9,1,5,9}, 2, 3);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        BinarySearchTree bst = new BinarySearchTree();
        for (int i = 0; i < nums.length; i++) {
            Integer floor = bst.floor(nums[i]);
            if (floor != null && (long) nums[i] - (long) floor <= (long) valueDiff) return true;

            Integer ceiling = bst.ceiling(nums[i]);
            if (ceiling != null && (long) ceiling - (long) nums[i] <= (long) valueDiff) return true;

            bst.add(nums[i]);
            if (bst.getSize() > indexDiff) bst.delete(nums[i - indexDiff]);
        }
        return false;
    }

    private TreeNode addToBST(TreeNode root, int num) {
        if (root == null) return new TreeNode(num);

        if (num <= root.val) {
            root.left = addToBST(root, num);
        } else {
            root.right = addToBST(root, num);
        }

        return root;
    }
}

class BinarySearchTree {
    private TreeNode root;
    private int size;

    public BinarySearchTree() { this.size = 0; }

    public BinarySearchTree(TreeNode root) {
        this.root = root;
        this.size = 0;
        sizeOfGivenTree(root);
    }
    private void sizeOfGivenTree(TreeNode root) {
        if (root == null) return;
        this.size++;
        sizeOfGivenTree(root.left);
        sizeOfGivenTree(root.right);
    }

    public TreeNode add(int val) {
        if (this.root == null) this.root = new TreeNode(val);
        else if (val < this.root.val) addHelper(this.root.left, this.root, val, true);
        else addHelper(this.root.right, this.root, val, false);
        this.size++;
        return this.root;
    }

    private void addHelper(TreeNode current, TreeNode parent, int val, boolean leftChild) {
        if (current == null) {
            if (leftChild) parent.left = new TreeNode(val);
            else parent.right = new TreeNode(val);
            return;
        }
        if (val < current.val) addHelper(current.left, current, val, true);
        else addHelper(current.right, current, val, false);
    }

    public TreeNode delete(int key) {
        if (this.root == null) return null;

        if (key < root.val) root.left = deleteHelper(root.left, key);
        else if (key > root.val) root.right = deleteHelper(root.right, key);
        else {
            if (this.root.left == null && this.root.right == null) {
                return null;
            } else if (this.root.left != null && this.root.right == null) {
                this.root = this.root.left;
            } else if (this.root.left == null) {
                this.root = this.root.right;
            } else {
                TreeNode parent = this.root;
                TreeNode swap = this.root.right;
                while (swap.left != null) {
                    parent = swap;
                    swap = swap.left;
                }

                this.root.val = swap.val;
                if (parent == this.root) this.root.right = deleteHelper(swap, swap.val);
                else parent.left = deleteHelper(swap, swap.val);
            }
        }

        this.size--;
        return this.root;
    }

    private TreeNode deleteHelper(TreeNode current, int key) {
        if (current == null) return null;

        if (key < current.val) {
            current.left = deleteHelper(current.left, key);
        } else if (key > current.val) {
            current.right = deleteHelper(current.right, key);
        } else {
            if (current.left == null && current.right == null) {
                return null;
            } else if (current.left != null && current.right == null) {
                return current.left;
            } else if (current.left == null) {
                return current.right;
            } else {
                TreeNode parent = current;
                TreeNode swap = current.right;
                while (swap.left != null) {
                    parent = swap;
                    swap = swap.left;
                }

                current.val = swap.val;
                if (parent == current) current.right = deleteHelper(swap, swap.val);
                else parent.left = deleteHelper(swap, swap.val);

                return current;
            }
        }

        return current;
    }

    public int first() {
        TreeNode current = this.root;
        while (current.left != null) current = current.left;
        return current.val;
    }

    public int last() {
        TreeNode current = this.root;
        while (current.right != null) current = current.right;
        return current.val;
    }

    public Integer ceiling(int value) {
        return ceilingHelper(this.root, value, null);
    }

    private Integer ceilingHelper(TreeNode current, int value, Integer res) {
        if (current == null) return null;

        if (current.val == value) return value;

        if (current.val > value) {
            if (current.left == null) return current.val;
            return ceilingHelper(current.left, value, current.val);
        }

        if (current.right == null) return res;
        return ceilingHelper(current.right, value, res);
    }

    public Integer floor(int value) {
        return floorHelper(this.root, value, null);
    }

    private Integer floorHelper(TreeNode current, int value, Integer res) {
        if (current == null) return null;

        if (current.val == value) return value;

        if (current.val > value) {
            if (current.left == null) return res;
            return floorHelper(current.left, value, res);
        }

        if (current.right == null) return current.val;
        return floorHelper(current.right, value, current.val);
    }

    public int getSize() {
        return size;
    }
}

//leetcode submit region end(Prohibit modification and deletion)

  }