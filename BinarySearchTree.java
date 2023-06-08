package com.shuzijun.leetcode;

import com.shuzijun.leetcode.editor.en.ContainsDuplicateIii;

public class BinarySearchTree {
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