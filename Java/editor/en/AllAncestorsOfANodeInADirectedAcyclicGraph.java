  /**
You are given a positive integer n representing the number of nodes of a 
Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive). 

 You are also given a 2D integer array edges, where edges[i] = [fromi, toi] 
denotes that there is a unidirectional edge from fromi to toi in the graph. 

 Return a list answer, where answer[i] is the list of ancestors of the iᵗʰ node,
 sorted in ascending order. 

 A node u is an ancestor of another node v if u can reach v via a set of edges. 


 
 Example 1: 
 
 
Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
Explanation:
The above diagram represents the input graph.
- Nodes 0, 1, and 2 do not have any ancestors.
- Node 3 has two ancestors 0 and 1.
- Node 4 has two ancestors 0 and 2.
- Node 5 has three ancestors 0, 1, and 3.
- Node 6 has five ancestors 0, 1, 2, 3, and 4.
- Node 7 has four ancestors 0, 1, 2, and 3.
 

 Example 2: 
 
 
Input: n = 5, edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],
[3,4]]
Output: [[],[0],[0,1],[0,1,2],[0,1,2,3]]
Explanation:
The above diagram represents the input graph.
- Node 0 does not have any ancestor.
- Node 1 has one ancestor 0.
- Node 2 has two ancestors 0 and 1.
- Node 3 has three ancestors 0, 1, and 2.
- Node 4 has four ancestors 0, 1, 2, and 3.
 

 
 Constraints: 

 
 1 <= n <= 1000 
 0 <= edges.length <= min(2000, n * (n - 1) / 2) 
 edges[i].length == 2 
 0 <= fromi, toi <= n - 1 
 fromi != toi 
 There are no duplicate edges. 
 The graph is directed and acyclic. 
 

 Related Topics Depth-First Search Breadth-First Search Graph Topological Sort ?
? 660 👎 8

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class AllAncestorsOfANodeInADirectedAcyclicGraph{
      public static void main(String[] args) {
          Solution solution = new AllAncestorsOfANodeInADirectedAcyclicGraph().new Solution();
          // int[][] edges = new int[][] {{0,3},{0,4},{1,3},{2,4},{2,7},{3,5},{3,6},{3,7},{4,6}};
          int[][] edges = new int[][] {{0,3},{5,0},{2,3},{4,3},{5,3},{1,3},{2,5},{0,1},{4,5},{4,2},{4,0},{2,1},{5,1}};
          solution.getAncestors(6, edges);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        Map<Integer, List<Integer>> children = new HashMap<>();
        int[] inDegree = new int[n];
        for (int[] edge : edges) {
            children.computeIfAbsent(edge[0], key -> new ArrayList<>()).add(edge[1]);
            inDegree[edge[1]]++;
        }
        
        List<Set<Integer>> ancestorLists = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            ancestorLists.add(new HashSet<>());
            if (inDegree[i] == 0)
                queue.offer(i);
        }
            
        while (!queue.isEmpty()) {
            int parent = queue.poll();
            for (int child : children.getOrDefault(parent, new ArrayList<>())) {
                ancestorLists.get(child).add(parent);
                ancestorLists.get(child).addAll(ancestorLists.get(parent));
                if (--inDegree[child] == 0)
                    queue.offer(child);
            }
        }

        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            res.add(new ArrayList<>(ancestorLists.get(i)));
            Collections.sort(res.get(i));
        }
        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }