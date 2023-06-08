  /**
There are a total of numCourses courses you have to take, labeled from 0 to 
numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, 
bi] indicates that you must take course bi first if you want to take course ai. 

 
 For example, the pair [0, 1], indicates that to take course 0 you have to 
first take course 1. 
 

 Return true if you can finish all courses. Otherwise, return false. 

 
 Example 1: 

 
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
 

 Example 2: 

 
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you 
should also have finished course 1. So it is impossible.
 

 
 Constraints: 

 
 1 <= numCourses <= 2000 
 0 <= prerequisites.length <= 5000 
 prerequisites[i].length == 2 
 0 <= ai, bi < numCourses 
 All the pairs prerequisites[i] are unique. 
 

 Related Topics Depth-First Search Breadth-First Search Graph Topological Sort ?
? 11807 👎 458

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class CourseSchedule{
      public static void main(String[] args) {
          Solution solution = new CourseSchedule().new Solution();
          //System.out.println(solution.canFinish(5, new int[][] {{0,1},{0,2},{1,3},{1,4},{3,4}}));
          //System.out.println(solution.canFinish(5, new int[][] {{1,4},{2,4},{3,1},{3,2}}));
          System.out.println(solution.canFinish(7, new int[][] {{1,0},{0,3},{0,2},{3,2},{2,5},{4,5},{5,6},{2,4}}));
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> prerequisiteMap = new HashMap<>();
        for (int i = 0; i < numCourses; i++)
            prerequisiteMap.put(i, new ArrayList<>());
        for (int[] pair : prerequisites)
            prerequisiteMap.get(pair[0]).add(pair[1]);

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i, prerequisiteMap, new HashSet<>()))
                return false;
        }
        return true;
    }

    private boolean dfs(int course, Map<Integer, List<Integer>> prerequisiteMap, Set<Integer> currentPath) {
        if (prerequisiteMap.get(course).isEmpty())
            return true;
        if (currentPath.contains(course))
            return false;

        currentPath.add(course);
        for (int prerequisite : prerequisiteMap.get(course)) {
            if (!dfs(prerequisite, prerequisiteMap, currentPath))
                return false;
        }

        prerequisiteMap.get(course).clear();
        return true;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }