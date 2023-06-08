  /**
There is a bi-directional graph with n vertices, where each vertex is labeled 
from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D 
integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge 
between vertex ui and vertex vi. Every vertex pair is connected by at most one edge,
 and no vertex has an edge to itself. 

 You want to determine if there is a valid path that exists from vertex source 
to vertex destination. 

 Given edges and the integers n, source, and destination, return true if there 
is a valid path from source to destination, or false otherwise. 

 
 Example 1: 
 
 
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
 

 Example 2: 
 
 
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination =
 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
 

 
 Constraints: 

 
 1 <= n <= 2 * 10⁵ 
 0 <= edges.length <= 2 * 10⁵ 
 edges[i].length == 2 
 0 <= ui, vi <= n - 1 
 ui != vi 
 0 <= source, destination <= n - 1 
 There are no duplicate edges. 
 There are no self edges. 
 

 Related Topics Depth-First Search Breadth-First Search Union Find Graph 👍 1630
 👎 90

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class FindIfPathExistsInGraph{
      public static void main(String[] args) {
           Solution solution = new FindIfPathExistsInGraph().new Solution();
           int[][] edges = {{0,1},{1,2},{2,0}};
           solution.validPath(3, edges, 0, 2);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        Map<Integer, List<Integer>> graph = new HashMap<>();    // Key --> vertex value, Value --> vertex's neighbours
        for (int[] edge : edges) {
            graph.putIfAbsent(edge[0], new ArrayList<>());
            graph.putIfAbsent(edge[1], new ArrayList<>());
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        return dfs(graph, new boolean[n], source, destination);
    }

    private boolean dfs(Map<Integer, List<Integer>> graph, boolean[] visited, int current, int destination) {
        if (current == destination)
            return true;

        if (!visited[current]) {
            visited[current] = true;
            for (int neighbour : graph.get(current))
                if (dfs(graph, visited, neighbour, destination))
                    return true;
        }

        return false;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }