  /**
Serialization is the process of converting a data structure or object into a 
sequence of bits so that it can be stored in a file or memory buffer, or 
transmitted across a network connection link to be reconstructed later in the same or 
another computer environment. 

 Design an algorithm to serialize and deserialize a binary tree. There is no 
restriction on how your serialization/deserialization algorithm should work. You 
just need to ensure that a binary tree can be serialized to a string and this 
string can be deserialized to the original tree structure. 

 Clarification: The input/output format is the same as how LeetCode serializes 
a binary tree. You do not necessarily need to follow this format, so please be 
creative and come up with different approaches yourself. 

 
 Example 1: 
 
 
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
 

 Example 2: 

 
Input: root = []
Output: []
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [0, 10⁴]. 
 -1000 <= Node.val <= 1000 
 

 Related Topics String Tree Depth-First Search Breadth-First Search Design 
Binary Tree 👍 7792 👎 287

*/
  
  package com.shuzijun.leetcode.editor.en;

  import com.shuzijun.leetcode.TreeNode;

  import java.util.*;

  public class SerializeAndDeserializeBinaryTree{
      public static void main(String[] args) {
          Codec solution = new SerializeAndDeserializeBinaryTree().new Codec();
          System.out.println(solution.serialize(solution.deserialize("[5,4,7,3,null,2,null,-1,null,9]")));
//          solution.deserialize("[5,4,7,3,null,2,null,-1,null,9]");
//          solution.deserialize("[1,2,3,null,null,4,5]");
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
public class Codec {

    // Encodes a tree to a single string.
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

    // Decodes your encoded data to tree.
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
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
//leetcode submit region end(Prohibit modification and deletion)

  }