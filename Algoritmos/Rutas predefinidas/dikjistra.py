from timeit import timeit
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_nodes_from(range(27))
G.add_edge(1, 2, weight=3)
G.add_edge(2, 3, weight=4)
G.add_edge(3, 4, weight=3)
G.add_edge(4, 5, weight=7)
G.add_edge(4, 6, weight=3)
G.add_edge(6, 7, weight=4)
G.add_edge(6, 12, weight=5)
G.add_edge(6, 11, weight=6)
G.add_edge(6, 18, weight=10)
G.add_edge(6, 24, weight=10)
G.add_edge(7, 8, weight=4)
G.add_edge(7, 10, weight=5)
G.add_edge(8, 9, weight=5)
G.add_edge(24, 26, weight=4)
G.add_edge(24, 25, weight=4)
G.add_edge(24, 27, weight=11)
G.add_edge(24, 27, weight=11)
G.add_edge(11, 12, weight=1)
G.add_edge(12, 13, weight=2)
G.add_edge(13, 17, weight=3)
G.add_edge(13, 14, weight=7)
G.add_edge(16, 17, weight=4)
G.add_edge(16, 15, weight=10)
G.add_edge(15, 14, weight=3)
G.add_edge(18, 19, weight=2)
G.add_edge(20, 18, weight=5)
G.add_edge(19, 21, weight=3)
G.add_edge(22, 21, weight=7)
G.add_edge(22, 23, weight=3)
pred, dist = nx.dijkstra_predecessor_and_distance(G, 1)
print(sorted(pred.items()))


	

	print(cuentatempo, "Algoritmo de Dikjistra")
