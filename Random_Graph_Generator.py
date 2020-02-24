import networkx as nx
G1 = nx.complete_graph(100000)
print(G1.edges.data())
G2 = nx.barbell_graph(5000,5000)
G3 = nx.cycle_graph(100000)
G4 = nx.binomial_tree(100000)