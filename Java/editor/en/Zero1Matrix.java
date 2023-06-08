  /**
Given an m x n binary matrix mat, return the distance of the nearest 0 for each 
cell. 

 The distance between two adjacent cells is 1. 

 
 Example 1: 
 
 
Input: mat = [[0,0,0},{0,1,0},{0,0,0]]
Output: [[0,0,0},{0,1,0},{0,0,0]]
 

 Example 2: 
 
 
Input: mat = [[0,0,0},{0,1,0},{1,1,1]]
Output: [[0,0,0},{0,1,0},{1,2,1]]
 

 
 Constraints: 

 
 m == mat.length 
 n == mat[i].length 
 1 <= m, n <= 10⁴ 
 1 <= m * n <= 10⁴ 
 mat[i][j] is either 0 or 1. 
 There is at least one 0 in mat. 
 

 Related Topics Array Dynamic Programming Breadth-First Search Matrix 👍 5816 👎
 291

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class Zero1Matrix{
      public static void main(String[] args) {
           Solution solution = new Zero1Matrix().new Solution();
           int[][] mat = {{1,1,0,0,1}
                         ,{1,0,0,1,0}
                         ,{1,1,1,0,0}
                         ,{0,1,1,1,0}};
           solution.updateMatrix(mat);
      }
//leetcode submit region begin(Prohibit modification and deletion)
public class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        if (matrix.length == 0) return matrix;

        int rows = matrix.length;
        int cols = matrix[0].length;
        int[][] dist = new int[rows][cols];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE/2);

        //First pass: check for left and top
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    dist[i][j] = 0;
                } else {
                    if (i > 0)
                        dist[i][j] = Math.min(dist[i][j], dist[i - 1][j] + 1);
                    if (j > 0)
                        dist[i][j] = Math.min(dist[i][j], dist[i][j - 1] + 1);
                }
            }
        }

        //Second pass: check for bottom and right
        for (int i = rows - 1; i >= 0; i--) {
            for (int j = cols - 1; j >= 0; j--) {
                if (i < rows - 1)
                    dist[i][j] = Math.min(dist[i][j], dist[i + 1][j] + 1);
                if (j < cols - 1)
                    dist[i][j] = Math.min(dist[i][j], dist[i][j + 1] + 1);
            }
        }
        return dist;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }