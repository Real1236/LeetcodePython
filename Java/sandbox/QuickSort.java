package com.shuzijun.leetcode.sandbox;

import java.util.Arrays;

public class QuickSort {
    public int[] quickSort(int[] arr) {
        if (arr.length <= 1) {
            return arr;
        }
        return quickSort(arr, 0, arr.length - 1);
    }

    public int[] quickSort(int[] arr, int start, int end) {
        if (end > start) {
            int partition = partition(arr, start, end);
            if (start < partition) {
                quickSort(arr, start, partition);
            }
            if (partition + 1 < end) {
                quickSort(arr, partition + 1, end);
            }
        }
        return arr;
    }

    public int partition(int[] arr, int leftPointer, int rightPointer) {

        int pivot = arr[Math.floorDiv((leftPointer + rightPointer), 2)];

        while (leftPointer < rightPointer) {
            while (arr[leftPointer] < pivot)
                leftPointer++;

            while (arr[rightPointer] > pivot)
                rightPointer--;

            if (leftPointer < rightPointer) {
                int temp = arr[rightPointer];
                arr[rightPointer] = arr[leftPointer];
                arr[leftPointer] = temp;
            }
        }
        return leftPointer;
    }

    public static void main(String[] args) {
        QuickSort qs = new QuickSort();
        int[] unsorted = {39, 15, 24, 35, 76, 19};
        System.out.println("Sorting the array " + Arrays.toString(unsorted));
        qs.quickSort(unsorted);
        System.out.println("After sorting: " + Arrays.toString(unsorted));
    }
}
