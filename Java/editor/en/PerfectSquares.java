  /**
Given an integer n, return the least number of perfect square numbers that sum 
to n. 

 A perfect square is an integer that is the square of an integer; in other 
words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 
are perfect squares while 3 and 11 are not. 

 
 Example 1: 

 
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
 

 Example 2: 

 
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

 
 Constraints: 

 
 1 <= n <= 10⁴ 
 

 Related Topics Math Dynamic Programming Breadth-First Search 👍 7595 👎 322

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.HashSet;
  import java.util.LinkedList;
  import java.util.Queue;
  import java.util.Set;

  public class PerfectSquares{
      public static void main(String[] args) {
           Solution solution = new PerfectSquares().new Solution();
           System.out.println(solution.numSquares(12));
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int numSquares(int n) {
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        queue.add(n);

        int[] perfectSquares = new int[(int) Math.sqrt(n)];
        for (int i = 0; i < perfectSquares.length; i++) {
            perfectSquares[i] = (int) Math.pow(i + 1, 2);
        }

        int res = 1;
        while (!queue.isEmpty()) {
            int qSize = queue.size();
            for (int i = 0; i < qSize; i++) {
                int current = queue.poll();
                visited.add(current);
                int j = 0;
                while (j < perfectSquares.length && perfectSquares[j] <= current) {
                    if (current - perfectSquares[j] == 0) return res;
                    if (!visited.contains(current - perfectSquares[j])) {
                        visited.add(current - perfectSquares[j]);
                        queue.add(current - perfectSquares[j++]);
                    } else {
                        j++;
                    }
                }
            }
            res++;
        }
        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }