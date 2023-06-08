  /**
You are given an n x n integer matrix grid where each value grid[i][j] 
represents the elevation at that point (i, j). 

 The rain starts to fall. At time t, the depth of the water everywhere is t. 
You can swim from a square to another 4-directionally adjacent square if and only 
if the elevation of both squares individually are at most t. You can swim 
infinite distances in zero time. Of course, you must stay within the boundaries of the 
grid during your swim. 

 Return the least time until you can reach the bottom right square (n - 1, n - 1
) if you start at the top left square (0, 0). 

 
 Example 1: 
 
 
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a 
higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
 

 Example 2: 
 
 
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10
,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
 

 
 Constraints: 

 
 n == grid.length 
 n == grid[i].length 
 1 <= n <= 50 
 0 <= grid[i][j] < n² 
 Each value grid[i][j] is unique. 
 

 Related Topics Array Binary Search Depth-First Search Breadth-First Search 
Union Find Heap (Priority Queue) Matrix 👍 2673 👎 177

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  import javafx.util.Pair;

  public class SwimInRisingWater{
      public static void main(String[] args) {
           Solution solution = new SwimInRisingWater().new Solution();
           solution.swimInWater(new int[][] {{0,2}, {1,3}});
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int swimInWater(int[][] grid) {
        Set<List<Integer>> visited = new HashSet<>();
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(arr -> arr[0])); // arr[0] -> path height, arr[1] -> row, arr[2] -> col

        visited.add(Arrays.asList(0,0));
        minHeap.offer(new int[] {grid[0][0], 0, 0});

        int[][] directions = new int[][] {{0,1}, {0,-1}, {1,0}, {-1,0}};
        while (!minHeap.isEmpty()) {
            int t = minHeap.peek()[0], row = minHeap.peek()[1], col = minHeap.poll()[2];
            if (row == grid.length - 1 && col == grid.length - 1)
                return t;
            for (int[] direction : directions) {
                int nRow = row + direction[0], nCol = col + direction[1];
                if (visited.contains(Arrays.asList(nRow, nCol)) || nRow == -1 || nCol == -1 || nRow == grid.length || nCol == grid.length)
                    continue;
                visited.add(Arrays.asList(nRow, nCol));
                minHeap.offer(new int[] {Math.max(t, grid[nRow][nCol]), nRow, nCol});
            }
        }

        return -1;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }