#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

fh=open("test.edgelist.txt",'rb')
G=nx.read_edgelist(fh)
print(G.nodes.data())
print(G.edges.data())


#plt.draw()
nx.draw(G)

#has some issue with creating isolated node.