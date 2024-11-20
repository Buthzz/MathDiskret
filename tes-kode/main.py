import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)])

g = nx.Graph()

g.nodes()

g.add_edge(9, 7)
g.add_edge(7, 5)
g.add_edge(7, 8)
g.add_edge(7, 6)
g.add_edge(8, 5)
g.add_edge(8, 6)
g.add_edge(6, 5)
g.add_edge(6, 4)
g.add_edge(5, 4)
g.add_edge(4, 3)
g.add_edge(4, 1)
g.add_edge(3, 1)
g.add_edge(2, 3)
g.add_edge(2, 1)

# nx.draw(g)

print("Degree centrality: ", nx.degree_centrality(g))
print("Closeness centrality: ", nx.closeness_centrality(g))
print("Beetweeness centrality: ", nx.betweenness_centrality(g))
nx.draw(g, with_labels = True)

# plt.savefig("filename.png")
plt.show()
