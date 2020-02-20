#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
n = int(input("Enter number of nodes : "))

node_list = list(map(str, input("\nEnter the nodes(put space between two nodes): ").strip().split()))[:n]
for node in node_list:
    n = int(input("Enter number of neighbors of " + str(node) + " :"))
    neighbor_list = list(map(str, input("\nEnter the neighbors(put space between two nodes): ").strip().split()))[:n]

for n in node_list:
    for nb in neighbor_list:
        G.add_edge(n, nb)

#plt.draw()
nx.draw(G)

#has some issue with creating isolated node.
