package com.shuzijun.leetcode;

import java.util.*;

public class Graph<V> {
    private List<Vertex<V>> vertices;
    private Map<V, Vertex<V>> vertexMap;
    // private Map<Vertex<V>, Vertex<V>> edges;
    private boolean isWeighted;
    private boolean isDirected;

    public Graph(boolean isWeighted, boolean isDirected) {
        this.vertices = new ArrayList<>();
        this.vertexMap = new HashMap<>();
        // this.edges = new HashMap<>();
        this.isWeighted = isWeighted;
        this.isDirected = isDirected;
    }

    public Vertex<V> addVertex(V data) {
        Vertex<V> newVertex = new Vertex<>(data);
        this.vertices.add(newVertex);
        this.vertexMap.put(data, newVertex);
        return newVertex;
    }

    public void addEdge(Vertex<V> u, Vertex<V> v, Integer weight) {
        if (!this.isWeighted)
            weight = null;

        // Map<Vertex<V>, Edge<V>> adjacencyMap = this.edges.get(u).getAjacencyMap();
        // adjacencyMap.put(u, v);
        // this.edges.put(u, v);
        u.addEdge(v, weight);
        if (!this.isDirected) {
            // this.edges.put(v, u);
            v.addEdge(u, weight);
        }
    }
    public void addEdge(V vertex1, V vertex2, Integer weight) {
        Vertex<V> u;
        Vertex<V> v;

        if (this.vertexMap.containsKey(vertex1))
            u = vertexMap.get(vertex1);
        else
            u = addVertex(vertex1);

        if (this.vertexMap.containsKey(vertex2))
            v = vertexMap.get(vertex2);
        else
            v = addVertex(vertex2);

        addEdge(u, v, weight);
    }

    public void removeEdge(Vertex<V> u, Vertex<V> v) {
        u.removeEdge(v);
        if (!this.isDirected)
            v.removeEdge(u);
    }

    public void removeVertex(Vertex<V> u) {
        this.vertices.remove(u);
        //Vertex<V> v = this.edges.remove(u);
        //this.edges.remove(v);
    }

    public boolean isDirected() {
        return isDirected;
    }

    public boolean isWeighted() {
        return isWeighted;
    }

    public List<Vertex<V>> getVertices() {
        return vertices;
    }

    //public Map<Vertex<V>, Vertex<V>> getEdges() {
    //    return edges;
    //}

    public List<Vertex<V>> getAdjacentVertices(V data) {
        return new ArrayList<>(getVertex(data).getAjacencyMap().keySet());
    }

    public Vertex<V> getVertex(V data) {
        for (Vertex<V> vertex : this.vertices) {
            if (vertex.getData() == data) {
                return vertex;
            }
        }
        return null;
    }
}