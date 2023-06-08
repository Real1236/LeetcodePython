package com.shuzijun.leetcode.sandbox;

import com.shuzijun.leetcode.Graph;
import com.shuzijun.leetcode.Vertex;

import java.util.*;

public class TopologicalSort {
    public List<Integer> topologicalSort(Graph<Integer> graph) {
        Stack<Integer> stack = new Stack<>();
        Set<Integer> visited = new HashSet<>();

        // Call the recursive helper function to store Topological Sort starting from all vertices one by one
        for (int i = 0; i < graph.getVertices().size(); i++)
            if (!visited.contains(i))
                topologicalSortUtil(graph, i, visited, stack);

        List<Integer> res = new ArrayList<>();
        while (!stack.empty())
            res.add(stack.pop());
        return res;
    }

    // A recursive function used by topologicalSort
    public void topologicalSortUtil(Graph<Integer> graph, int v, Set<Integer> visited, Stack<Integer> stack) {
        visited.add(v); // Mark the current node as visited.

        // Recur for all the vertices adjacent to this vertex
        for (Vertex<Integer> vertex : graph.getAdjacentVertices(v)) {
            if (!visited.contains(vertex.getData()))
                topologicalSortUtil(graph, vertex.getData(), visited, stack);
        }

        stack.push(v); // Push current vertex to stack which stores result
    }

    public static void main(String args[]) {
        TopologicalSort run = new TopologicalSort();

        // Create a graph given in the above diagram
        Graph<Integer> g = new Graph<>(false, true);
        g.addEdge(5, 2, null);
        g.addEdge(5, 0, null);
        g.addEdge(4, 0, null);
        g.addEdge(4, 1, null);
        g.addEdge(2, 3, null);
        g.addEdge(3, 1, null);

        List<Integer> traversal = run.topologicalSort(g);
        System.out.println("Following is a Topological " + "sort of the given graph");
        for (Integer vertex : traversal)
            System.out.print(vertex + " ");
    }
}
