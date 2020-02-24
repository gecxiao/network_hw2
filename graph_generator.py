#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt


def bfs(G, s):
    visited = {}  # initialize visited, using dict.
    for node in nx.nodes(G):
        visited[str(node)] = False  # set visited[i]=False
    queue = []  # initialize ToExplore list, since BFS, using queue
    S = []  # the list we want to return
    S.append(s)  # add s to S.
    queue.append(s)  # add s to ToExplore
    visited[str(s)] = True  # set visitied[s] tobe true.
    while queue:  # while ToExplore is non-empty
        s = queue.pop(0)  # remove s from ToExplore
        for v in G.neighbors(s):  # for every edge in adj(s)
            if not visited[str(v)]:  # if (visited[y]==False)
                queue.append(v)  # add y toexplore
                visited[str(v)] = True  # set visited[y]=True
                S.append(v)  # add y to S.
    return S


def bfs_helper(G, s, t):
    S = bfs(G, s)
    return t in S


def ford_fulkerson(G, s, t):
    f = 0  # maxflow number
    G_residual = nx.preflow_push(G, s, t)  #
    while bfs_helper(G_residual, s, t):  # if there is a path from s to t in the reversed graph
        return 1
    return f


fh = open("test.edgelist.txt", 'rb')
G = nx.read_edgelist(fh)
# print(G.nodes.data())
# print(G.edges.data())
# print(G.nodes)
print(bfs(G, '1'))
# plt.draw()
nx.draw(G)

# has some issue with creating isolated node.
