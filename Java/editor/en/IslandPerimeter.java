  /**
You are given row x col grid representing a map where grid[i][j] = 1 represents 
land and grid[i][j] = 0 represents water. 

 Grid cells are connected horizontally/vertically (not diagonally). The grid is 
completely surrounded by water, and there is exactly one island (i.e., one or 
more connected land cells). 

 The island doesn't have "lakes", meaning the water inside isn't connected to 
the water around the island. One cell is a square with side length 1. The grid is 
rectangular, width and height don't exceed 100. Determine the perimeter of the 
island. 

 
 Example 1: 
 
 
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
 

 Example 2: 

 
Input: grid = [[1]]
Output: 4
 

 Example 3: 

 
Input: grid = [[1,0]]
Output: 4
 

 
 Constraints: 

 
 row == grid.length 
 col == grid[i].length 
 1 <= row, col <= 100 
 grid[i][j] is 0 or 1. 
 There is exactly one island in grid. 
 

 Related Topics Array Depth-First Search Breadth-First Search Matrix 👍 5126 👎 
257

*/
  
  package com.shuzijun.leetcode.editor.en;
  public class IslandPerimeter{
      public static void main(String[] args) {
           Solution solution = new IslandPerimeter().new Solution();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int islandPerimeter(int[][] grid) {
        int perimeter = 0;
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[row].length; col++) {
                if (grid[row][col] == 0) {
                    if (col < grid[row].length - 1 && grid[row][col + 1] == 1) perimeter++;
                    if (row < grid.length - 1 && grid[row + 1][col] == 1) perimeter++;
                } else {
                    if (row == 0) perimeter++;
                    if (row == grid.length - 1) perimeter++;
                    if (col == 0) perimeter++;
                    if (col == grid[row].length - 1) perimeter++;
                    if (col < grid[row].length - 1 && grid[row][col + 1] == 0) perimeter++;
                    if (row < grid.length - 1 && grid[row + 1][col] == 0) perimeter++;
                }
            }
        }
        return perimeter;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }