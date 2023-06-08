  /**
You are given a network of n nodes, labeled from 1 to n. You are also given 
times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui 
is the source node, vi is the target node, and wi is the time it takes for a 
signal to travel from source to target. 

 We will send a signal from a given node k. Return the minimum time it takes 
for all the n nodes to receive the signal. If it is impossible for all the n nodes 
to receive the signal, return -1. 

 
 Example 1: 
 
 
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
 

 Example 2: 

 
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
 

 Example 3: 

 
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

 
 Constraints: 

 
 1 <= k <= n <= 100 
 1 <= times.length <= 6000 
 times[i].length == 3 
 1 <= ui, vi <= n 
 ui != vi 
 0 <= wi <= 100 
 All the pairs (ui, vi) are unique. (i.e., no multiple edges.) 
 

 Related Topics Depth-First Search Breadth-First Search Graph Heap (Priority 
Queue) Shortest Path 👍 5781 👎 324

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class NetworkDelayTime{
      public static void main(String[] args) {
           Solution solution = new NetworkDelayTime().new Solution();
           solution.networkDelayTime(new int[][] {{1,2,1}}, 2, 2);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, Map<Integer, Integer>> adjacencyLists = new HashMap<>();
        for (int[] edge : times) {
            adjacencyLists.putIfAbsent(edge[0], new HashMap<>());
            adjacencyLists.get(edge[0]).put(edge[1], edge[2]);
        }

        Map<Integer, Integer> nodeTimes = new HashMap<>();
        nodeTimes.put(k, 0);
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        minHeap.offer(new int[] {k, 0});

        while (!minHeap.isEmpty()) {
            int node = minHeap.peek()[0];
            int nodeTime = minHeap.poll()[1];
            if (nodeTime > nodeTimes.get(node))
                continue;
            if (!adjacencyLists.containsKey(node))
                continue;
            Map<Integer, Integer> neighbours = adjacencyLists.get(node);
            for (int neighbour : neighbours.keySet()) {
                int time = nodeTime + neighbours.get(neighbour);
                if (time < nodeTimes.getOrDefault(neighbour, Integer.MAX_VALUE)) {
                    nodeTimes.put(neighbour, time);
                    minHeap.offer(new int[] {neighbour, time});
                }
            }
        }

        if (nodeTimes.size() < n)
            return -1;
        int minTime = 0;
        for (int time : nodeTimes.values())
            minTime = Math.max(minTime, time);
        return minTime == Integer.MAX_VALUE ? -1 : minTime;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }