  /**
You are given an array of variable pairs equations and an array of real numbers 
values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / 
Bi = values[i]. Each Ai or Bi is a string that represents a single variable. 

 You are also given some queries, where queries[j] = [Cj, Dj] represents the jᵗʰ
 query where you must find the answer for Cj / Dj = ?. 

 Return the answers to all queries. If a single answer cannot be determined, 
return -1.0. 

 Note: The input is always valid. You may assume that evaluating the queries 
will not result in division by zero and that there is no contradiction. 

 
 Example 1: 

 
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a",
"c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
 

 Example 2: 

 
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
 

 Example 3: 

 
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],[
"a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

 
 Constraints: 

 
 1 <= equations.length <= 20 
 equations[i].length == 2 
 1 <= Ai.length, Bi.length <= 5 
 values.length == equations.length 
 0.0 < values[i] <= 20.0 
 1 <= queries.length <= 20 
 queries[i].length == 2 
 1 <= Cj.length, Dj.length <= 5 
 Ai, Bi, Cj, Dj consist of lower case English letters and digits. 
 

 Related Topics Array Depth-First Search Breadth-First Search Union Find Graph 
Shortest Path 👍 6623 👎 572

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class EvaluateDivision{
      public static void main(String[] args) {
          Solution solution = new EvaluateDivision().new Solution();

          List<List<String>> equations = new ArrayList<>();
          for (int i = 0; i < 4; i++)
              equations.add(new ArrayList<>());
          equations.get(0).add("x1");
          equations.get(0).add("x2");
          equations.get(1).add("x2");
          equations.get(1).add("x3");
          equations.get(2).add("x3");
          equations.get(2).add("x4");
          equations.get(3).add("x4");
          equations.get(3).add("x5");

          double[] values = new double[] {3.0,4.0,5.0,6.0};

          List<List<String>> queries = new ArrayList<>();
          for (int i = 0; i < 6; i++)
              queries.add(new ArrayList<>());
          queries.get(0).add("x1");
          queries.get(0).add("x5");
          queries.get(1).add("x5");
          queries.get(1).add("x2");
          queries.get(2).add("x2");
          queries.get(2).add("x4");
          queries.get(3).add("x2");
          queries.get(3).add("x2");
          queries.get(4).add("x2");
          queries.get(4).add("x9");
          queries.get(5).add("x9");
          queries.get(5).add("x9");

          solution.calcEquation(equations, values, queries);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> graph = new HashMap<>();
        for (int i = 0; i < equations.size(); i++) {
            String start = equations.get(i).get(0);
            String end = equations.get(i).get(1);

            graph.putIfAbsent(start, new HashMap<>());
            graph.get(start).put(end, values[i]);
            graph.putIfAbsent(end, new HashMap<>());
            graph.get(end).put(start, 1/values[i]);
        }

        double[] res = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            String start = queries.get(i).get(0);
            String end = queries.get(i).get(1);

            if (!graph.containsKey(start) || !graph.containsKey(end))
                res[i] = -1;
            else
                res[i] = dfs(start, end, graph, new HashSet<>());
        }

        return res;
    }

    private double dfs(String start, String end, Map<String, Map<String, Double>> graph, Set<String> visited) {
        if (graph.get(start).containsKey(end))
            return graph.get(start).get(end);

        visited.add(start);
        for (String neighbour : graph.get(start).keySet()) {
            if (!visited.contains(neighbour)) {
                double product = dfs(neighbour, end, graph, visited);
                if (product != -1)
                    return product * graph.get(start).get(neighbour);
            }
        }
        return -1;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }