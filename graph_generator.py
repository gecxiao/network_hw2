#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt


def BFS(G, s):
    visited={}
    for node in nx.nodes(G):
        visited[str(node)]=False
    queue = []
    S = []
    queue.append(s)
    visited[str(s)] = True
    while queue:
        s = queue.pop(0)
        for v in G.neighbors(s):
            if not visited[str(v)]:
                queue.append(v)
                visited[str(v)] = True
                S.append(v)
    return S


def max_flow(G, s, t):
    f = 0
    G_reverse = nx.reverse(G)

fh=open("test.edgelist.txt",'rb')
G=nx.read_edgelist(fh)
#print(G.nodes.data())
#print(G.edges.data())
#print(G.nodes)
print(BFS(G,'1'))
#plt.draw()
nx.draw(G)

#has some issue with creating isolated node.


