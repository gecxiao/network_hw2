import networkx as nx
import random
#import matplotlib.pyplot as plt
#from graph_generator import *

def gen_complete_graph(n):
    G1 = nx.complete_graph(n)
    for (u, v) in G1.edges():
        G1.edges[u,v]['weight'] = random.randint(0,20)
    return G1
#print(G1.edges.data())
#nx.draw(G1)
#plt.show()

#G11 = nx.complete_graph(50)
#for (u, v) in G11.edges():
#    G11.edges[u, v]['weight'] = random.randint(0, 20)
##print (G11.edges.data())
#
#G12 = nx.complete_graph(500)
#for (u, v) in G12.edges():
#    G12.edges[u, v]['weight'] = random.randint(0, 20)
##print (G12.edges.data())

def gen_barbell_graph(n):
    G2 = nx.barbell_graph(n,n)
    for (u, v) in G2.edges():
        G2.edges[u, v]['weight'] = random.randint(0, 20)
    return G2
#print (G2.edges.data())
#nx.draw(G2)
#plt.show()

#G21 = nx.barbell_graph(25, 25)
#for (u, v) in G21.edges():
#    G21.edges[u, v]['weight'] = random.randint(0, 20)
##print (G21.edges.data())
#
#G22 = nx.barbell_graph(25, 25)
#for (u, v) in G22.edges():
#    G22.edges[u, v]['weight'] = random.randint(0, 20)
##print (G22.edges.data())
def gen_cycle_graph(n):
    G3 = nx.cycle_graph(n)
    for (u, v) in G3.edges():
        G3.edges[u, v]['weight'] = random.randint(0, 20)
    return G3

#print (G3.edges.data())
#nx.draw(G3)
#plt.show()

#G31 = nx.cycle_graph(50)
#for (u, v) in G31.edges():
#    G31.edges[u, v]['weight'] = random.randint(0, 20)
##print (G31.edges.data())
#
#G32 = nx.cycle_graph(50)
#for (u, v) in G32.edges():
#    G32.edges[u, v]['weight'] = random.randint(0, 20)
#print (G32.edges.data())
def gen_binomial_tree(n,m):  
    G4 = nx.balanced_tree(n,m)
    for (u, v) in G4.edges():
        G4.edges[u, v]['weight'] = random.randint(0, 20)
    return G4
##print (G4.edges.data())
##nx.draw(G4)
##plt.show()
#
#G41 = nx.binomial_tree(8)
#for (u, v) in G41.edges():
#    G41.edges[u, v]['weight'] = random.randint(0, 20)
##print (G41.edges.data())
#
#G42 = nx.binomial_tree(8)
#for (u, v) in G42.edges():
#    G42.edges[u, v]['weight'] = random.randint(0, 20)
##print (G42.edges.data())

def gen_star_graph(n):
    G5 = nx.star_graph(n)
    for (u, v) in G5.edges():
        G5.edges[u, v]['weight'] = random.randint(0, 20)
    return G5
#print (G5.edges.data())
#nx.draw(G5)
#plt.show()

#G51 = nx.star_graph(100)
#for (u, v) in G51.edges():
#    G51.edges[u, v]['weight'] = random.randint(0, 20)
##print (G51.edges.data())
#
#G52 = nx.star_graph(100)
#for (u, v) in G52.edges():
#    G52.edges[u, v]['weight'] = random.randint(0, 20)
##print (G52.edges.data())

G = gen_binomial_tree(5,10)
#nx.draw(G)
#time1 = ford_fulkerson_dijkstra(G, 1, 2)
time1 = ford_fulkerson_dijkstra_benchmark(G, 1, 2)
time2 = ford_fulkerson_bfs_benchmark(G,1,2)
print(time1)
print(time2)

# not finished
complete_graph_benchmark = []
barbell_graph_benchmark = []
cycle_graph_benchmark = []
star_graph_benchmark = []

for n in range(10, 1001, 10):
    G = gen_complete_graph(n)
    time1 = ford_fulkerson_dijkstra_benchmark(G, 1, 2)
    time2 = ford_fulkerson_bfs_benchmark(G,1,2)
    complete_graph_benchmark.append((time1,time2))
    
    G1 = gen_barbell_graph(n)
    time1 = ford_fulkerson_dijkstra_benchmark(G1, 1, 2)
    time2 = ford_fulkerson_bfs_benchmark(G1,1,2)
    barbell_graph_benchmark.append((time1,time2))
    
    G2 = gen_cycle_graph(n)
    time1 = ford_fulkerson_dijkstra_benchmark(G2, 1, 2)
    time2 = ford_fulkerson_bfs_benchmark(G2,1,2)
    cycle_graph_benchmark.append((time1,time2))
    
    G3 = gen_star_graph(n)
    time1 = ford_fulkerson_dijkstra_benchmark(G3, 1, 2)
    time2 = ford_fulkerson_bfs_benchmark(G3,1,2)
    star_graph_benchmark.append((time1,time2))

#print(complete_graph_benchmark)
