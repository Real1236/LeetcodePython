package com.shuzijun.leetcode;

import java.util.*;

public class TreeDeserializer {
    public TreeNode deserialize(String data) {
        if (data.equals("[]"))
            return null;

        String[] treeArray = data.substring(1, data.length() - 1).split(",");
        List<TreeNode> levelOrderNodes = new ArrayList<>();
        Map<Integer, TreeNode> map = new HashMap<>();   // key -> index in treeArray, value -> corresponding TreeNode
        for (int i = 0; i < treeArray.length; i++) {
            String node = treeArray[i];
            if (!node.equals("null")) {
                TreeNode treeNode = new TreeNode(Integer.parseInt(node));
                levelOrderNodes.add(treeNode);
                map.put(i, treeNode);
            }
        }

        for (int i = 0; i < levelOrderNodes.size(); i++) {
            TreeNode current = levelOrderNodes.get(i);

            int leftIndex = 2 * i + 1;
            int rightIndex = 2 * i + 2;
            boolean leftNull = leftIndex >= treeArray.length || treeArray[leftIndex].equals("null");
            boolean rightNull = rightIndex >= treeArray.length || treeArray[rightIndex].equals("null");

            if (!leftNull)
                current.left = map.get(leftIndex);
            if (!rightNull)
                current.right = map.get(rightIndex);
        }

        return levelOrderNodes.get(0);
    }

    public String serialize(TreeNode root) {
        List<String> levelOrderedList = new ArrayList<>();
        if (root != null)
            levelOrderedList.add(Integer.toString(root.val));
        else
            return "[]";

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode current = queue.poll();

                if (current.left == null) {
                    levelOrderedList.add("null");
                } else {
                    levelOrderedList.add(Integer.toString(current.left.val));
                    queue.add(current.left);
                }

                if (current.right == null) {
                    levelOrderedList.add("null");
                } else {
                    levelOrderedList.add(Integer.toString(current.right.val));
                    queue.add(current.right);
                }
            }
        }

        while (levelOrderedList.get(levelOrderedList.size() - 1).equals("null"))
            levelOrderedList.remove(levelOrderedList.size() - 1);

        String treeString = String.join(",", levelOrderedList);

        return "[" + treeString + "]";
    }
}
