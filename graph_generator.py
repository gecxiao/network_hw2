#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
import time
import random
import matplotlib.pyplot as plt

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
    t1 = time.perf_counter()
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
    t2 = time.perf_counter()
    print (f"Fuld_Fulkerson+BFS uses {t2 - t1:0.4f} seconds")
    return f

def ford_fulkerson_bfs_benchmark(G, s, t):
    t1 = time.perf_counter()
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
    t2 = time.perf_counter()
    #print (f"Fuld_Fulkerson+BFS uses {t2 - t1:0.4f} seconds")
    t = t2 - t1
    t = round(t,3)
    return t


def ford_fulkerson_dijkstra(G, s, t):
    t1 = time.perf_counter()
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
    t2 = time.perf_counter()
    print (f"Fuld_Fulkerson+Dijkstra uses {t2 - t1:0.4f} seconds")
    return f

def ford_fulkerson_dijkstra_benchmark(G, s, t):
    t1 = time.perf_counter()
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
    t2 = time.perf_counter()
    #print (f"Fuld_Fulkerson+Dijkstra uses {t2 - t1:0.4f} seconds")
    t = t2-t1
    t = round(t,3)
    return t


def gen_complete_graph(n):
    G1 = nx.complete_graph(n)
    for (u, v) in G1.edges():
        G1.edges[u,v]['weight'] = random.randint(0,20)
    return G1

def gen_barbell_graph(n):
    G2 = nx.barbell_graph(n,n)
    for (u, v) in G2.edges():
        G2.edges[u, v]['weight'] = random.randint(0, 20)
    return G2

def gen_cycle_graph(n):
    G3 = nx.cycle_graph(n)
    for (u, v) in G3.edges():
        G3.edges[u, v]['weight'] = random.randint(0, 20)
    return G3

#def gen_binomial_tree(n,m):  
#    G4 = nx.balanced_tree(n,m)
#    for (u, v) in G4.edges():
#        G4.edges[u, v]['weight'] = random.randint(0, 20)
#    return G4

def gen_star_graph(n):
    G5 = nx.star_graph(n)
    for (u, v) in G5.edges():
        G5.edges[u, v]['weight'] = random.randint(0, 20)
    return G5

dijkastra_time_list = []
bfs_time_list = []
size_list = []
for i in range(100, 1000, 100):
    G = gen_complete_graph(i)
#nx.draw(G)
#time1 = ford_fulkerson_dijkstra(G, 1, 2)
    time_dijkastra = ford_fulkerson_dijkstra_benchmark(G, 1, 2)
    time_bfs = ford_fulkerson_bfs_benchmark(G,1,2)
    dijkastra_time_list.append(time_dijkastra)
    bfs_time_list.append(time_bfs)
    size_list.append(i)
    
compare_list  = [dijkastra_time_list, bfs_time_list]
labels = ['dijkastra','bfs']

for compare, label in zip(compare_list,labels):
    plt.plot(size_list, compare, label=label)
    
plt.legend()

plt.xlabel('input size')
plt.ylabel('time')
plt.title('Complete graph 1')
plt.show()
print(dijkastra_time_list)
print(bfs_time_list)
#fh = open("test.edgelist.txt", 'rb')
#G = nx.read_edgelist(fh, create_using=nx.DiGraph)
# print(G.nodes.data())
# print(G.edges.data())
# print(G.nodes)
# print(bfs(G, '1'))
#print(G.edges())
#f=ford_fulkerson_bfs(G, '3', '4')
#print(f)
#t = ford_fulkerson_bfs_benchmark(G,'1','4')
#print(t)
#f = ford_fulkerson_dijkstra(G, '1', '4')
#print(f)
#plt.draw(G)
