  /**
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0
's (water), return the number of islands. 

 An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. You may assume all four edges of the grid are all 
surrounded by water. 

 
 Example 1: 

 
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
 

 Example 2: 

 
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

 
 Constraints: 

 
 m == grid.length 
 n == grid[i].length 
 1 <= m, n <= 300 
 grid[i][j] is '0' or '1'. 
 

 Related Topics Array Depth-First Search Breadth-First Search Union Find Matrix 
👍 17382 👎 400

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class NumberOfIslands{
      public static void main(String[] args) {
          Solution solution = new NumberOfIslands().new Solution();
          //char[][] grid = new char[][] {{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}};
          char[][] grid = new char[][] {{'1','1','1'},{'0','1','0'},{'1','1','1'}};
          solution.numIslands(grid);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {
                if (grid[row][col] == '0') continue;

                count++;
                findIsland(grid, row, col);
            }
        }
        return count;
    }

    private void findIsland(char[][] grid, int row, int col) {
        if (grid[row][col] == '0') return;

        grid[row][col] = '0';

        if (col < grid[0].length - 1) findIsland(grid, row, col + 1);
        if (row < grid.length - 1) findIsland(grid, row + 1, col);
        if (col > 0) findIsland(grid, row, col - 1);
        if (row > 0) findIsland(grid, row - 1, col);
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }