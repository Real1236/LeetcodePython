package com.shuzijun.leetcode;

import java.util.HashMap;
import java.util.Map;

public class Vertex<V> {
    private V data;
    private Map<Vertex<V>, Edge<V>> adjacencyMap;

    public Vertex(V input) {
        this.data = input;
        this.adjacencyMap = new HashMap<>();
    }

    public void addEdge(Vertex<V> v, Integer weight) {
        this.adjacencyMap.put(v, new Edge<>(this, v, weight));
    }

    public void removeEdge(Vertex<V> v) {
        this.adjacencyMap.remove(v);
    }

    public Map<Vertex<V>, Edge<V>> getAjacencyMap() { return adjacencyMap; }
    public V getData() { return data; }
}
