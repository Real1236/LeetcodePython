package com.shuzijun.leetcode;

public class Edge<V> {
    private Vertex<V> start, end;
    private Integer weight;

    public Edge(Vertex<V> u, Vertex<V> v, Integer weight) {
        this.start = u;
        this.end = v;
        this.weight = weight;
    }

    public Integer getWeight() { return weight;}
    public Vertex getEnd() { return end; }
    public Vertex getStart() { return start; }
}