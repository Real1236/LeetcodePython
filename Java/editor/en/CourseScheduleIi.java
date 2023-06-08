  /**
There are a total of numCourses courses you have to take, labeled from 0 to 
numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, 
bi] indicates that you must take course bi first if you want to take course ai. 

 
 For example, the pair [0, 1], indicates that to take course 0 you have to 
first take course 1. 
 

 Return the ordering of courses you should take to finish all courses. If there 
are many valid answers, return any of them. If it is impossible to finish all 
courses, return an empty array. 

 
 Example 1: 

 
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you 
should have finished course 0. So the correct course order is [0,1].
 

 Example 2: 

 
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you 
should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after 
you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

 

 Example 3: 

 
Input: numCourses = 1, prerequisites = []
Output: [0]
 

 
 Constraints: 

 
 1 <= numCourses <= 2000 
 0 <= prerequisites.length <= numCourses * (numCourses - 1) 
 prerequisites[i].length == 2 
 0 <= ai, bi < numCourses 
 ai != bi 
 All the pairs [ai, bi] are distinct. 
 

 Related Topics Depth-First Search Breadth-First Search Graph Topological Sort ?
? 8184 👎 274

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class CourseScheduleIi{
      public static void main(String[] args) {
          Solution solution = new CourseScheduleIi().new Solution();
          solution.findOrder(4, new int[][] {{1,0},{2,0},{3,1},{3,2}});
          //solution.findOrder(3, new int[][] {{0,1},{0,2},{1,2}});
          //solution.findOrder(7, new int[][] {{1,0},{0,3},{0,2},{3,2},{2,5},{4,5},{5,6},{2,4}});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    private int resIndex;

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> prerequisiteMap = new HashMap<>();
        for (int i = 0; i < numCourses; i++)
            prerequisiteMap.put(i, new ArrayList<>());
        for (int[] pair : prerequisites)
            prerequisiteMap.get(pair[0]).add(pair[1]);

        int[] res = new int[numCourses];
        this.resIndex = 0;
        Set<Integer> validCourses = new HashSet<>();
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i, res, prerequisiteMap, validCourses, new HashSet<>()))
                return new int[] {};
        }
        return res;
    }

    private boolean dfs(int course, int[] res, Map<Integer, List<Integer>> prerequisiteMap,
                        Set<Integer> validCourses, Set<Integer> currentPath) {
        if (validCourses.contains(course))
            return true;
        if (currentPath.contains(course))
            return false;

        currentPath.add(course);
        for (int prerequisite : prerequisiteMap.get(course)) {
            if (!dfs(prerequisite, res, prerequisiteMap, validCourses, currentPath))
                return false;
        }

        res[this.resIndex++] = course;
        validCourses.add(course);
        return true;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }