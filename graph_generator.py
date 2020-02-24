#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx


# from networkx.algorithms.flow import preflow_push


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


def ford_fulkerson_bfs(G, s, t):
    f = 0  # maxflow number
    path = bfs(G, s)
    for i in range(1, len(path)):
        G.add_edge(path[i], path[i-1], weight=0)
    while bfs_helper(G, s, t):  # if there is a path from s to t in the residual graph
        path = bfs(G, s)  
        i = 0
        capacity = float('inf') 
        while path[i] != t:
            capacity = min(G[path[i]][path[i + 1]]['weight'], capacity)
            i += 1
        i = 0
        while path[i] != t:
            G[path[i]][path[i + 1]]['weight'] -= capacity  # update residual graph
            G[path[i + 1]][path[i]]['weight'] += capacity  # update residual graph
            i += 1
        f += capacity #update maxflow
        if capacity == 0: #if there is no flow, break the loop
            break
    return f


def ford_fulkerson_dijkstra(G, s, t):
    f = 0  # maxflow number
    path = nx.dijkstra_path(G, s, t)
    for i in range(1, len(path)):
        G.add_edge(path[i], path[i-1], weight=0)
    while nx.dijkstra_path(G, s, t):  # if there is a path from s to t in the residual graph
        path = nx.dijkstra_path(G, s, t)  # [1,2,3,4]
        i = 0
        capacity = float('inf')
        while path[i] != t:
            capacity = min(G[path[i]][path[i + 1]]['weight'], capacity)
            i += 1
        i = 0
        while path[i] != t:
            G[path[i]][path[i + 1]]['weight'] -= capacity
            # G.add_edge(i+1,i, weight = 0)
            # print(G.edges.data())
            G[path[i + 1]][path[i]]['weight'] += capacity
            i += 1
        f += capacity
        if capacity == 0:
            break
    return f


fh = open("test.edgelist.txt", 'rb')
G = nx.read_edgelist(fh, create_using=nx.DiGraph)
# print(G.nodes.data())
# print(G.edges.data())
# print(G.nodes)
# print(bfs(G, '1'))
# print(G.edges())
#f=ford_fulkerson_bfs(G, '3', '4')
#print(f)

f = ford_fulkerson_dijkstra(G, '1', '4')
print(f)
# plt.draw()


# has some issue with creating isolated node.
