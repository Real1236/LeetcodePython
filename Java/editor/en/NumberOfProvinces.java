  /**
There are n cities. Some of them are connected, while some are not. If city a 
is connected directly with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c. 

 A province is a group of directly or indirectly connected cities and no other 
cities outside of the group. 

 You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the iᵗ
ʰ city and the jᵗʰ city are directly connected, and isConnected[i][j] = 0 
otherwise. 

 Return the total number of provinces. 

 
 Example 1: 
 
 
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
 

 Example 2: 
 
 
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

 
 Constraints: 

 
 1 <= n <= 200 
 n == isConnected.length 
 n == isConnected[i].length 
 isConnected[i][j] is 1 or 0. 
 isConnected[i][i] == 1 
 isConnected[i][j] == isConnected[j][i] 
 

 Related Topics Depth-First Search Breadth-First Search Union Find Graph 👍 6519
 👎 270

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class NumberOfProvinces{
      public static void main(String[] args) {
           Solution solution = new NumberOfProvinces().new Solution();
           solution.findCircleNum(new int[][] {{1,1,0},{1,1,0},{0,0,1}});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int findCircleNum(int[][] isConnected) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 1; i <= isConnected.length; i++)
            graph.put(i, new ArrayList<>());
        for (int row = 0; row < isConnected.length; row++) {
            for (int col = 0; col < isConnected.length; col++) {
                if (col <= row || isConnected[row][col] == 0)
                    continue;
                graph.get(row + 1).add(col + 1);
                graph.get(col + 1).add(row + 1);
            }
        }

        Set<Integer> visited = new HashSet<>();
        int numOfIslands = 0;
        for (int i = 1; i <= isConnected.length; i++) {
            if (visited.contains(i)) continue;
            dfs(i, graph, visited);
            numOfIslands++;
        }
        return numOfIslands;
    }

    private void dfs(int city, Map<Integer, List<Integer>> graph, Set<Integer> visited) {
        visited.add(city);
        for (int connectedCities : graph.get(city)) {
            if (visited.contains(connectedCities)) continue;
            dfs(connectedCities, graph, visited);
        }
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }