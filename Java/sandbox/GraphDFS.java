package com.shuzijun.leetcode.sandbox;

import com.shuzijun.leetcode.Graph;
import com.shuzijun.leetcode.Vertex;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class GraphDFS {
    public List<Vertex<Integer>> dfs(Vertex<Integer> start, boolean preorder) {
        Set<Vertex<Integer>> visited = new HashSet<>();
        List<Vertex<Integer>> res = new ArrayList<>();
        if (preorder)
            preorderHelper(start, visited, res);
        else
            postorderHelper(start, visited, res);
        return res;
    }

    public void preorderHelper(Vertex<Integer> vertex, Set<Vertex<Integer>> visited, List<Vertex<Integer>> res) {
        visited.add(vertex);
        res.add(vertex);
        for (Vertex<Integer> neighbour : vertex.getAjacencyMap().keySet()) {
            if (!visited.contains(neighbour))
                preorderHelper(neighbour, visited, res);
        }
    }

    public void postorderHelper(Vertex<Integer> vertex, Set<Vertex<Integer>> visited, List<Vertex<Integer>> res) {
        visited.add(vertex);
        for (Vertex<Integer> neighbour : vertex.getAjacencyMap().keySet()) {
            if (!visited.contains(neighbour))
                postorderHelper(neighbour, visited, res);
        }
        res.add(vertex);
    }

    public static void main(String args[]) {
        GraphDFS run = new GraphDFS();
        int index = 0;

        // Directed graph
        Graph<Integer> g = new Graph<>(false, true);
        g.addEdge(5, 2, null);
        g.addEdge(5, 0, null);
        g.addEdge(4, 0, null);
        g.addEdge(4, 1, null);
        g.addEdge(2, 3, null);
        g.addEdge(3, 1, null);
        List<List<Vertex<Integer>>> preorderTraversals = new ArrayList<>();
        List<List<Vertex<Integer>>> postorderTraversals = new ArrayList<>();
        for (int i = 0; i < 6; i++) {
            Vertex<Integer> current = g.getVertex(i);
            preorderTraversals.add(run.dfs(current, true));
            postorderTraversals.add(run.dfs(current, false));
        }

        System.out.println("PREORDER TRAVERSALS\n");
        index = 0;
        for (List<Vertex<Integer>> traversal : preorderTraversals) {
            System.out.println("Following is a preorder DFS traversal of the given graph starting at Vertex: " + index++);
            for (Vertex<Integer> vertex : traversal)
                System.out.print(vertex.getData() + " ");
            System.out.println("\n-------------------------------------------------------------------------");
        }

        System.out.println("POSTORDER TRAVERSALS\n");
        index = 0;
        for (List<Vertex<Integer>> traversal : postorderTraversals) {
            System.out.println("Following is a postorder DFS traversal of the given graph starting at Vertex: " + index++);
            for (Vertex<Integer> vertex : traversal)
                System.out.print(vertex.getData() + " ");
            System.out.println("\n-------------------------------------------------------------------------");
        }

        // Undirected graph
        Graph<Integer> h = new Graph<>(false, false);
        h.addEdge(0, 1, null);
        h.addEdge(0, 2, null);
        h.addEdge(1, 3, null);
        h.addEdge(2, 3, null);
        h.addEdge(3, 4, null);
        h.addEdge(4, 5, null);
        h.addEdge(2, 6, null);
        List<List<Vertex<Integer>>> hPreorderTraversals = new ArrayList<>();
        List<List<Vertex<Integer>>> hPostorderTraversals = new ArrayList<>();
        for (int i = 0; i < 7; i++) {
            Vertex<Integer> current = h.getVertex(i);
            hPreorderTraversals.add(run.dfs(current, true));
            hPostorderTraversals.add(run.dfs(current, false));
        }

        System.out.println("PREORDER TRAVERSALS\n");
        index = 0;
        for (List<Vertex<Integer>> traversal : hPreorderTraversals) {
            System.out.println("Following is a preorder DFS traversal of the given graph starting at Vertex: " + index++);
            for (Vertex<Integer> vertex : traversal)
                System.out.print(vertex.getData() + " ");
            System.out.println("\n-------------------------------------------------------------------------");
        }

        System.out.println("POSTORDER TRAVERSALS\n");
        index = 0;
        for (List<Vertex<Integer>> traversal : hPostorderTraversals) {
            System.out.println("Following is a postorder DFS traversal of the given graph starting at Vertex: " + index++);
            for (Vertex<Integer> vertex : traversal)
                System.out.print(vertex.getData() + " ");
            System.out.println("\n-------------------------------------------------------------------------");
        }
    }
}
