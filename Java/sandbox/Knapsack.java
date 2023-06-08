package com.shuzijun.leetcode.sandbox;

public class Knapsack {
    // Returns the maximum value that can be put in a knapsack of capacity W
    public static int knapSack(int weightCap, int[] weights, int[] values) {
        Integer[][] memo = new Integer[weights.length][weightCap + 1];
        return knapSackHelper(0, weightCap, memo, weights, values);
    }

    private static int knapSackHelper (int i, int weightCap, Integer[][] memo, int[] weights, int[] values) {
        if (i == weights.length || weightCap == 0)
            return 0;
        if (weights[i] > weightCap)
            return (knapSackHelper(i + 1, weightCap, memo, weights, values));
        if (memo[i][weightCap] != null)
            return memo[i][weightCap];

        int valAdded = values[i] + knapSackHelper(i + 1, weightCap - weights[i], memo, weights, values);
        int valNotAdded = knapSackHelper(i + 1, weightCap, memo, weights, values);

        memo[i][weightCap] = Math.max(valAdded, valNotAdded);
        return memo[i][weightCap];
    }

    // Driver code
    public static void main(String args[])
    {
        int[] values = new int[] { 60, 100, 120 };
        int[] weights = new int[] { 10, 20, 30 };
        int weightCap = 50;
        // int[] values = new int[] { 250, 300, 500 };
        // int[] weights = new int[] { 1, 3, 5 };
        // int weightCap = 5;
        System.out.println(knapSack(weightCap, weights, values));
    }
}