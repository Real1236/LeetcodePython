  /**
A tree is an undirected graph in which any two vertices are connected by 
exactly one path. In other words, any connected graph without simple cycles is a tree. 


 Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges 
where edges[i] = [ai, bi] indicates that there is an undirected edge between the 
two nodes ai and bi in the tree, you can choose any node of the tree as the 
root. When you select a node x as the root, the result tree has height h. Among all 
possible rooted trees, those with minimum height (i.e. min(h)) are called 
minimum height trees (MHTs). 

 Return a list of all MHTs' root labels. You can return the answer in any order.
 

 The height of a rooted tree is the number of edges on the longest downward 
path between the root and a leaf. 

 
 Example 1: 
 
 
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node 
with label 1 which is the only MHT.
 

 Example 2: 
 
 
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 

 
 Constraints: 

 
 1 <= n <= 2 * 10⁴ 
 edges.length == n - 1 
 0 <= ai, bi < n 
 ai != bi 
 All the pairs (ai, bi) are distinct. 
 The given input is guaranteed to be a tree and there will be no repeated edges.
 
 

 Related Topics Depth-First Search Breadth-First Search Graph Topological Sort ?
? 6179 👎 265

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class MinimumHeightTrees{
      public static void main(String[] args) {
           Solution solution = new MinimumHeightTrees().new Solution();
           solution.findMinHeightTrees(4, new int[][] {{1,0},{1,2},{1,3}});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n < 2) {
            List<Integer> res = new ArrayList<>();
            for (int i = 0; i < n; i++)
                res.add(i);
            return res;
        }

        List<List<Integer>> adjacencyList = new ArrayList<>();
        for (int i = 0; i < n; i++)
            adjacencyList.add(new LinkedList<>());
        for (int[] edge : edges) {
            adjacencyList.get(edge[0]).add(edge[1]);
            adjacencyList.get(edge[1]).add(edge[0]);
        }

        Queue<Integer> leafNodes = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (adjacencyList.get(i).size() == 1)
                leafNodes.add(i);
        }

        int nodesLeft = n;
        while (nodesLeft > 2) {
            int leafNodesInLevel = leafNodes.size();
            nodesLeft -= leafNodesInLevel;
            for (int i = 0; i < leafNodesInLevel; i++) {
                int leafNode = leafNodes.poll();
                int parent = adjacencyList.get(leafNode).get(0);
                adjacencyList.get(parent).remove((Integer) leafNode);
                if (adjacencyList.get(parent).size() == 1)
                    leafNodes.offer(parent);
            }
        }
        return new ArrayList<>(leafNodes);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }