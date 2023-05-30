import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('data.tsv', sep='\t')

graph = nx.Graph()           # Cria o grafo
user_loc_list = data['user_loc'].tolist()
fr_loc_list = data['fr_loc'].tolist()
graph.add_nodes_from(user_loc_list)
for i in range(0, len(user_loc_list)):
    graph.add_edge(user_loc_list[i], fr_loc_list[i])
nx.draw_spectral(graph)

plt.show()
