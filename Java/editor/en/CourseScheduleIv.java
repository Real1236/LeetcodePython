  /**
There are a total of numCourses courses you have to take, labeled from 0 to 
numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, 
bi] indicates that you must take course ai first if you want to take course bi. 

 
 For example, the pair [0, 1] indicates that you have to take course 0 before 
you can take course 1. 
 

 Prerequisites can also be indirect. If course a is a prerequisite of course b, 
and course b is a prerequisite of course c, then course a is a prerequisite of 
course c. 

 You are also given an array queries where queries[j] = [uj, vj]. For the jᵗʰ 
query, you should answer whether course uj is a prerequisite of course vj or not. 


 Return a boolean array answer, where answer[j] is the answer to the jᵗʰ query. 


 
 Example 1: 
 
 
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before 
you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.
 

 Example 2: 

 
Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.
 

 Example 3: 
 
 
Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,
2]]
Output: [true,true]
 

 
 Constraints: 

 
 2 <= numCourses <= 100 
 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2) 
 prerequisites[i].length == 2 
 0 <= ai, bi <= n - 1 
 ai != bi 
 All the pairs [ai, bi] are unique. 
 The prerequisites graph has no cycles. 
 1 <= queries.length <= 10⁴ 
 0 <= ui, vi <= n - 1 
 ui != vi 
 

 Related Topics Depth-First Search Breadth-First Search Graph Topological Sort ?
? 1040 👎 53

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class CourseScheduleIv{
      public static void main(String[] args) {
           Solution solution = new CourseScheduleIv().new Solution();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        List<Set<Integer>> adjacencyLists = new ArrayList<>();
        int[] inDegrees = new int[numCourses];
        for (int i = 0; i < numCourses; i++)
            adjacencyLists.add(new HashSet<>());
        for (int[] pair : prerequisites) {
            adjacencyLists.get(pair[0]).add(pair[1]);
            inDegrees[pair[1]]++;
        }

        List<Set<Integer>> prereqLists = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegrees[i] == 0)
                queue.offer(i);
            prereqLists.add(new HashSet<>());
        }

        while (!queue.isEmpty()) {
            int course = queue.poll();
            for (int neighbour : adjacencyLists.get(course)) {
                prereqLists.get(neighbour).add(course);
                prereqLists.get(neighbour).addAll(prereqLists.get(course));
                if (--inDegrees[neighbour] == 0)
                    queue.offer(neighbour);
            }
        }

        List<Boolean> queryResults = new ArrayList<>(queries.length);
        for (int[] query : queries)
            queryResults.add(prereqLists.get(query[1]).contains(query[0]));
        return queryResults;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }