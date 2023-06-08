package com.shuzijun.leetcode.sandbox;

import java.util.HashMap;
import java.util.Map;

public class RobloxQ3 {
    public int solution(int[][] matrix) {
        Map<Integer, Integer> countY = new HashMap<>();
        Map<Integer, Integer> countNotY = new HashMap<>();
        for (int row = 0; row < matrix.length; row++) {
            for (int col = 0; col < matrix[row].length; col++) {
                if (((row == col || col == matrix.length - 1 - row) && row <= matrix.length / 2)
                        || (col == matrix.length / 2 && row > matrix.length / 2)) {
                    countY.put(matrix[row][col], countY.getOrDefault(matrix[row][col], 0) + 1);
                } else {
                    countNotY.put(matrix[row][col], countNotY.getOrDefault(matrix[row][col], 0) + 1);
                }
            }
        }

        int greatestCountY = -1;
        int greatestCountNotY = -1;
        for (int i = 0; i <= 2; i++) {
            if (countY.getOrDefault(i, 0) > countY.getOrDefault(greatestCountY, 0)) {
                greatestCountY = i;
            }
            if (countNotY.getOrDefault(i, 0) > countNotY.getOrDefault(greatestCountNotY, 0)) {
                greatestCountNotY = i;
            }
        }

        if (greatestCountNotY != greatestCountY) {
            int sumY = 0;
            int sumNotY = 0;
            for (int i = 0; i <= 2; i++) {
                if (i != greatestCountY) {
                    sumY += countY.getOrDefault(i, 0);
                }
                if (i != greatestCountNotY) {
                    sumNotY += countNotY.getOrDefault(i, 0);
                }
            }
            return sumY + sumNotY;
        }

        int nextGreatestCountY = -1;
        for (int i = 0; i <= 2; i++) {
            if (i != greatestCountY) {
                nextGreatestCountY = Math.max(countY.getOrDefault(i, 0), nextGreatestCountY);
            }
        }

        int sumY = 0;
        int sumNotY = 0;
        for (int i = 0; i <= 2; i++) {
            if (i != nextGreatestCountY) {
                sumY += countY.getOrDefault(i, 0);
            }
            if (i != greatestCountNotY) {
                sumNotY += countNotY.getOrDefault(i, 0);
            }
        }
        return sumY + sumNotY;
    }

    public static void main(String[] args) {
        RobloxQ3 sandbox = new RobloxQ3();
        sandbox.solution(new int[][] {{1, 0, 2},{1, 2, 0},{0, 2, 0}});
    }
}
